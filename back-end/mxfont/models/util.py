import torch
import torch.nn as nn
import torch.nn.functional as F

class Expert(nn.Module):
    def __init__(self, input_shape, feature_dim):
        super(Expert, self).__init__()
        c, h, w = input_shape
        self.shared_cnn = nn.Sequential(
            nn.Conv2d(c, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1))
        )
        self.fc_content = nn.Linear(128, feature_dim)
        self.fc_style = nn.Linear(128, feature_dim)

    def forward(self, x):
        x = self.shared_cnn(x)
        x = x.view(x.size(0), -1)
        fc = self.fc_content(x)
        fs = self.fc_style(x)
        return fc, fs

class Experts(nn.Module):
    def __init__(self, num_experts, input_shape, feature_dim):
        super(Experts, self).__init__()
        self.experts = nn.ModuleList([Expert(input_shape, feature_dim) for _ in range(num_experts)])

    def forward(self, x):
        fc_list, fs_list = [], []
        for expert in self.experts:
            fc, fs = expert(x)
            fc_list.append(fc)
            fs_list.append(fs)
        return fc_list, fs_list


class FeatureClassifier(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(FeatureClassifier, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        return self.fc(x)


class FontGenerator(nn.Module):
    def __init__(self, feature_dim, output_shape, num_experts):
        super(FontGenerator, self).__init__()
        self.feature_dim = feature_dim
        self.num_experts = num_experts
        input_dim = feature_dim * 2 * num_experts
        c, h, w = output_shape

        self.fc = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, c * h * w),
            nn.Tanh()
        )
        self.output_shape = output_shape

    def forward(self, features):
        combined = torch.cat([torch.cat([fs, fc], dim=-1) for fs, fc in features], dim=-1)
        x = self.fc(combined)
        return x.view(x.size(0), *self.output_shape)


class Discriminator(nn.Module):
    def __init__(self, input_shape, num_classes):
        super(Discriminator, self).__init__()
        c, h, w = input_shape
        self.conv = nn.Sequential(
            nn.Conv2d(c, 32, kernel_size=3, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.LeakyReLU(0.2),
            nn.Flatten()
        )
        self.fc = nn.Linear((h // 4) * (w // 4) * 64, num_classes)

    def forward(self, x):
        features = self.conv(x)
        return self.fc(features)


def classification_loss(pred, target):
    return F.cross_entropy(pred, target)

def hinge_adversarial_loss(real_pred, fake_pred):
    real_loss = torch.mean(F.relu(1.0 - real_pred))
    fake_loss = torch.mean(F.relu(1.0 + fake_pred))
    return real_loss + fake_loss

def generator_adv_loss(fake_pred):
    return -torch.mean(fake_pred)

def feature_matching_loss(real_feat, fake_feat):
    return F.l1_loss(real_feat, fake_feat)

def reconstruction_loss(x_recon, x_target):
    return F.mse_loss(x_recon, x_target)

