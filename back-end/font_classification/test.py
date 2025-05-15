import torchvision
import torchvision.transforms as transforms
import torch
from torch.utils.data import DataLoader
import os
import sys
import argparse

# logger
from my_logger import  set_logger
sys.path.append('/root/autodl-tmp/font_classification/data_utils')
from myfont import MyFont

# 指定GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '0'


def test():
    model.eval()
    correct = 0
    total = 0
    test_acc = 0
    with torch.no_grad():
        for batch_idx, (inputs, targets) in enumerate(testloader):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

        test_acc = correct / total
        mylogger.info(f'Test Accurancy: {test_acc:.3f}')


if __name__ == '__main__':
    # 设置超参
    parser = argparse.ArgumentParser(description='Classify Test')
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--data_dir', type=str, default='/root/autodl-tmp/font_classification/dataset')
    parser.add_argument('--num_class', type=int, default=6, help='num of class')
    parser.add_argument('--net', type=str, default='resnet18')
    parser.add_argument('--save_dir', type=str, default='/root/autodl-tmp/font_classification/result', help='save path of results')
    parser.add_argument('--checkpoint', type=str, default='/root/autodl-tmp/font_classification/result/resnet18_checkpoints/best.pth')

    args = parser.parse_args()

    # 设置logger
    mylogger = set_logger('test', f'{args.save_dir}/{args.net}_test.txt')

    # 设置相关参数
    device = torch.device('cuda:0') if torch.cuda.is_available() else 'cpu'
    mylogger.info(args)
    mylogger.info(f"Use {device} for testing")

    mylogger.info('==> Preparing data..')
    # 定义数据预处理
    transform_test = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor()])

    # 加载数据集
    testset = MyFont(args.data_dir, transform_test, train=False)
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=args.batch_size, shuffle=False, num_workers=4)

    # 加载模型
    mylogger.info('==> Building model..')
    if args.net == 'resnet18':
        model = torchvision.models.resnet18(weights=None)
        num_features = model.fc.in_features
        model.fc = torch.nn.Linear(num_features, args.num_class)
    elif args.net == 'resnet34':
        model = torchvision.models.resnet34(weights=None)
        num_features = model.fc.in_features
        model.fc = torch.nn.Linear(num_features, args.num_class)
    elif args.net == 'resnet50':
        model = torchvision.models.resnet50(weights=None)
        num_features = model.fc.in_features
        model.fc = torch.nn.Linear(num_features, args.num_class)
    model = model.to(device)
    mylogger.info(model)

    # 加载之前训练的参数
    assert os.path.exists(args.checkpoint), 'Error: no checkpoint found!'
    mylogger.info("=> loading checkpoint '{}'".format(args.checkpoint))
    checkpoint = torch.load(args.checkpoint)
    model.load_state_dict(checkpoint['net'])

    # 测试
    mylogger.info(f'Begin test')
    test()