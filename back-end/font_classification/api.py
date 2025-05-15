import torchvision
import torchvision.transforms as transforms
import torch
from torch.utils.data import DataLoader
from PIL import Image
import os
import sys
import argparse
import fnmatch
import numpy as np

# 指定GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

def get_tensor(data, transform):
    img_tensor = []
    file_paths = []

    if os.path.isfile(data) and (os.path.splitext(data)[1] == '.png'):
        # print(f'loading png from file: {data}')
        file_paths.append(data)
        img = Image.open(data)
        img_tensor.append(transform(img))
    elif os.path.isdir(data): 
        # print(f'loading pngs from directory: {data}')
        for root, dirs, files in os.walk(data):
            for filename in files:
                if fnmatch.fnmatch(filename, "*.png"):
                    png_path = os.path.join(root, filename)
                    file_paths.append(png_path)
                    img = Image.open(png_path)
                    img_tensor.append(transform(img))
                    
    assert len(file_paths) > 0, f'No png found in {data}!'
    if len(img_tensor) == 1:
        img_tensor = torch.unsqueeze(img_tensor[0], 0)
    else:
        img_tensor = torch.stack(img_tensor, dim=0)
    # print(img_tensor.shape)
    return file_paths, img_tensor

def build_model(net, num_class):
    # 加载模型
    # print('==> Building model..')
    if net == 'resnet18':
        model = torchvision.models.resnet18(weights=None)
    elif net == 'resnet34':
        model = torchvision.models.resnet34(weights=None)
    elif net == 'resnet50':
        model = torchvision.models.resnet50(weights=None)
    num_features = model.fc.in_features
    model.fc = torch.nn.Linear(num_features, num_class)
    return model


def classify(data, num_class = 6, net = 'resnet18', only=False, checkpoint =
    '/root/autodl-tmp/code/font_classification/result/resnet18_checkpoints/best.pth'):
    """
    :data: 要识别的图片的路径/文件夹路径
    :param num_class: 类别数量
    :net: 网络架构
    :only: 仅当data为文件夹路径时有效，only为True表示文件夹中的所有图片属于相同的类别
    :checkpoint: 预训练模型的位置
    :return: 类别
    """
    # 设置相关参数
    device = torch.device('cuda:0') if torch.cuda.is_available() else 'cpu'

    # 定义数据预处理
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=3),  # 将单通道的灰度图转换为三通道的彩色图
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor()
    ])

    # 得到要处理的所有图片路径，并转换为 tensor
    file_paths, img_tensor = get_tensor(data, transform)

    # 构造模型并加载之前训练的参数
    model = build_model(net, num_class).to(device)
    assert os.path.exists(checkpoint), 'Error: no checkpoint found!'
    checkpoint = torch.load(checkpoint)
    model.load_state_dict(checkpoint['net'])

    # 测试
    model.eval()
    with torch.no_grad():
        img_tensor = img_tensor.to(device)
        outputs = model(img_tensor)
        pred_labels = outputs.argmax(dim=1).cpu().numpy()
    class_names = ['圆体', '手写体——普通手写体', '手写体——有笔锋的手写体', '楷书', '行书', '黑体']
    pred_class = [class_names[i] for i in pred_labels]
    # for i, path in enumerate(file_paths):
    #     print(path, '\t', pred_class[i])
    if only:
        pred_labels = np.argmax(np.bincount(pred_labels))
    return pred_labels

def select_ttf(class_index):
    """
    :class_index: 类别数的下标
    :return: 随机返回该类别数中的一个字体文件的位置
    """
    return 0

if __name__ == '__main__':
    data = '/root/autodl-tmp/font_classification/tempdataset'
    classify(data)