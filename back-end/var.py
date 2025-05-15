import torch
import torch.nn as nn
import torch.nn.functional as F


class VQVAEEncoder(nn.Module):
    def __init__(self, in_channels=3, hidden_dim=128):
        super(VQVAEEncoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels, hidden_dim, 4, stride=2, padding=1),  # -> 112x112
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim, 4, stride=2, padding=1),   # -> 56x56
            nn.ReLU(),
            nn.Conv2d(hidden_dim, hidden_dim, 1),                         # -> 56x56
        )

    def forward(self, x):
        return self.encoder(x)

class VectorQuantizer(nn.Module):
    def __init__(self, num_embeddings=512, embedding_dim=128, commitment_cost=0.25):
        super(VectorQuantizer, self).__init__()
        self.embedding_dim = embedding_dim
        self.num_embeddings = num_embeddings
        self.commitment_cost = commitment_cost

        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.embedding.weight.data.uniform_(-1/self.num_embeddings, 1/self.num_embeddings)

    def forward(self, z):
        # z: [B, C, H, W]
        z_flattened = z.permute(0, 2, 3, 1).contiguous().view(-1, self.embedding_dim)
        distances = (
            torch.sum(z_flattened**2, dim=1, keepdim=True) 
            - 2 * torch.matmul(z_flattened, self.embedding.weight.t()) 
            + torch.sum(self.embedding.weight**2, dim=1)
        )

        encoding_indices = torch.argmin(distances, dim=1).unsqueeze(1)
        encodings = torch.zeros(encoding_indices.size(0), self.num_embeddings, device=z.device)
        encodings.scatter_(1, encoding_indices, 1)

        quantized = torch.matmul(encodings, self.embedding.weight).view(z.shape)
        commitment_loss = self.commitment_cost * F.mse_loss(quantized.detach(), z)
        embedding_loss = F.mse_loss(quantized, z.detach())

        quantized = z + (quantized - z).detach()  # Straight-Through Estimator

        return quantized, encoding_indices.view(z.shape[0], z.shape[2], z.shape[3]), commitment_loss + embedding_loss

class VQVAEDecoder(nn.Module):
    def __init__(self, out_channels=3, hidden_dim=128):
        super(VQVAEDecoder, self).__init__()
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(hidden_dim, hidden_dim, 4, stride=2, padding=1),  # -> 112x112
            nn.ReLU(),
            nn.ConvTranspose2d(hidden_dim, hidden_dim, 4, stride=2, padding=1),  # -> 224x224
            nn.ReLU(),
            nn.Conv2d(hidden_dim, out_channels, 1),
            nn.Tanh()  # [-1, 1] 范围
        )

    def forward(self, x):
        return self.decoder(x)


class TokenTransformer(nn.Module):
    def __init__(self, vocab_size, seq_len, d_model=512, num_layers=6, nhead=8):
        super(TokenTransformer, self).__init__()
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Parameter(torch.randn(1, seq_len, d_model))
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead)
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        # x: [B, L]
        x = self.token_embed(x) + self.pos_embed[:, :x.size(1), :]
        x = self.transformer(x)
        return self.fc_out(x)


class FontGeneratorAutoregressive(nn.Module):
    def __init__(self, vocab_size=512, token_shape=(56, 56)):
        super(FontGeneratorAutoregressive, self).__init__()
        self.encoder = VQVAEEncoder()
        self.vq = VectorQuantizer(num_embeddings=vocab_size)
        self.decoder = VQVAEDecoder()

        seq_len = token_shape[0] * token_shape[1]
        self.transformer = TokenTransformer(vocab_size, seq_len)

        self.token_shape = token_shape

    def forward(self, x):
        z = self.encoder(x)
        quantized, tokens, vq_loss = self.vq(z)
        logits = self.transformer(tokens.view(tokens.size(0), -1))
        recon = self.decoder(quantized)
        return recon, logits, vq_loss

    def generate(self, input_tokens):
        logits = self.transformer(input_tokens)
        pred_tokens = torch.argmax(logits, dim=-1)
        pred_tokens = pred_tokens.view(-1, *self.token_shape)
        embedding = self.vq.embedding(pred_tokens)
        embedding = embedding.permute(0, 3, 1, 2)  # B, C, H, W
        return self.decoder(embedding)
