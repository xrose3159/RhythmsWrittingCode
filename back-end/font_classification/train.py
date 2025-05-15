import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import torch
import torch.nn as nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt
import os
import sys
import argparse
import time
import math
# logger
from my_logger import  set_logger
sys.path.append('/root/autodl-tmp/font_classification/data_utils')
from myfont import MyFont

# 指定GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

# Training
def train(epoch):
    model.train()
    train_loss = 0
    correct = 0
    total = 0
    train_acc = 0
    # 开始迭代每个batch中的数据
    for batch_idx, (inputs, targets) in enumerate(trainloader):
        inputs, targets = inputs.to(device), targets.to(device)
        # print(inputs.shape)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        # 计算损失
        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

    train_acc = correct / total
    total_train_acc.append(train_acc)
    total_loss.append(train_loss)

    state = {
        'net': model.state_dict(),
        'acc': train_acc,
        'epoch': epoch,
    }
    save_model_path = os.path.join(args.save_dir, f'{args.net}_checkpoints')
    if epoch % args.save_freq == 0:
        if not os.path.isdir(save_model_path):
            os.makedirs(save_model_path)
        torch.save(state, os.path.join(save_model_path, f'{epoch}.pth'))
    if epoch == args.epochs - 1:
        torch.save(state, os.path.join(save_model_path, f'final.pth'))

    mylogger.info(f'[INFO] Epoch_{epoch+1}: Train: Loss: {loss.item():.4f}, Train Accuracy: {train_acc:.4f}')


# eval
def eval(epoch):
    global best_acc
    model.eval()
    eval_loss = 0
    correct = 0
    total = 0
    eval_acc = 0
    with torch.no_grad():
        for batch_idx, (inputs, targets) in enumerate(valloader):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            eval_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

        eval_acc = correct / total
        mylogger.info(f'Epoch_{epoch + 1}: Eval Accurancy: {eval_acc:.3f}')

    total_eval_acc.append(eval_acc)

    # 保存权重文件
    acc = 100. * correct / total
    if acc > best_acc:
        mylogger.info('Saving model...')
        state = {
            'net': model.state_dict(),
            'acc': acc,
            'epoch': epoch,
        }
        save_model_path = os.path.join(args.save_dir, f'{args.net}_checkpoints')
        if not os.path.isdir(save_model_path):
            os.makedirs(save_model_path)
        torch.save(state, os.path.join(save_model_path, f'best.pth'))
        best_acc = acc


# def test():
#     model.eval()
#     correct = 0
#     total = 0
#     test_acc = 0
#     with torch.no_grad():
#         for batch_idx, (inputs, targets) in enumerate(testloader):
#             inputs, targets = inputs.to(device), targets.to(device)
#             outputs = model(inputs)
#             _, predicted = outputs.max(1)
#             total += targets.size(0)
#             correct += predicted.eq(targets).sum().item()
#
#         test_acc = correct / total
#         mylogger.info(f'Test Accurancy: {test_acc:.3f}')


if __name__ == '__main__':
    # 设置超参
    parser = argparse.ArgumentParser(description='Classify Train')
    parser.add_argument('--epochs', type=int, default=200)
    # parser.add_argument('--start_epoch', type=int, default=0)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--data_dir', type=str, default='/root/autodl-tmp/font_classification/dataset')
    parser.add_argument('--num_class', type=int, default=6, help='num of class')
    parser.add_argument('--net', type=str, default='resnet18')
    parser.add_argument('--lr', default=0.001, type=float, help='learning rate')
    parser.add_argument('--resume', '-r', action='store_true', help='resume from checkpoint')
    parser.add_argument('--checkpoint', type=str)
    parser.add_argument('--save_freq', type=int, default=10)
    parser.add_argument('--save_dir', type=str, default='/root/autodl-tmp/font_classification/result', help='save path of results')
    parser.add_argument('--T_max', type=int, default=100)

    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
    args.checkpoint = os.path.join(args.save_dir, f'{args.net}_checkpoints/best.pth')

    # 设置logger
    mylogger = set_logger('train', f'{args.save_dir}/{args.net}_log.txt')

    # 设置相关参数
    device = torch.device('cuda:0') if torch.cuda.is_available() else 'cpu'
    mylogger.info(args)
    mylogger.info(f"Use {device} for training")
    best_acc = 0  # best eval accuracy
    start_epoch = 0  # start from epoch 0 or last checkpoint epoch

    mylogger.info('==> Preparing data..')
    # 定义数据预处理
    transform_train = transforms.Compose(
        [transforms.RandomResizedCrop(224),
         transforms.RandomHorizontalFlip(),
         transforms.ToTensor()])

    transform_test = transforms.Compose(
        [transforms.Resize(256),
         transforms.CenterCrop(224),
         transforms.ToTensor()])

    # 加载数据集
    _trainset = MyFont(args.data_dir, transform_train, train=True)
    # testset = MyFont(args.data_dir, transform_test, train=False)

    # 将训练集划分为训练集和验证集
    train_ratio = 0.8
    train_size = int(len(_trainset) * train_ratio)
    val_size = len(_trainset) - train_size
    trainset, valset = torch.utils.data.random_split(_trainset, [train_size, val_size])
    mylogger.info(f'train data: {len(_trainset.data)}')
    mylogger.info(f'train: {len(trainset)}, validation: {len(valset)}')
    # mylogger.info(f'testdata: {len(testset.data)}')

    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=args.batch_size, shuffle=True, num_workers=4)
    valloader = torch.utils.data.DataLoader(
        valset, batch_size=args.batch_size, shuffle=False, num_workers=4)
    # testloader = torch.utils.data.DataLoader(
    #     testset, batch_size=args.batch_size, shuffle=False, num_workers=4)

    # print(trainloader.dataset.shape)

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

    # DP训练
    if device == 'cuda':
        model = torch.nn.DataParallel(model)
        cudnn.benchmark = True

    # 加载之前训练的参数
    if args.resume:
        # Load checkpoint.
        mylogger.info("=> loading checkpoint '{}'".format(args.checkpoint))
        assert os.path.isdir('checkpoint'), 'Error: no checkpoint directory found!'
        checkpoint = torch.load(args.checkpoint)
        model.load_state_dict(checkpoint['net'])
        best_acc = checkpoint['acc']
        start_epoch = checkpoint['epoch']
    else:
        mylogger.info("=> no checkpoint found at '{}'".format(args.checkpoint))

    # 设置损失函数与优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=args.lr,
                          momentum=0.9, weight_decay=5e-4)

    # 余弦退火有序调整学习率
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.T_max)

    # ReduceLROnPlateau（自适应调整学习率）
    # scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10)

    # 记录training和eval的acc
    total_eval_acc = []
    total_train_acc = []
    total_loss = []

    # 记录训练时间
    start_time = time.time()

    # 开始训练
    for epoch in range(start_epoch, args.epochs):
        train(epoch)
        eval(epoch)
        # 动态调整学习率
        scheduler.step()
        # ReduceLROnPlateau（自适应调整学习率）
        # scheduler.step(loss_val)

    # 数据可视化
    plt.figure()
    plt.plot(range(args.epochs), total_train_acc, label='Train Accurancy')
    plt.plot(range(args.epochs), total_eval_acc, label='Eval Accurancy')
    plt.plot(range(args.epochs), total_loss, label='train loss')
    plt.xlabel('Epoch')
    plt.ylabel('Accurancy and Loss')
    plt.title(f'{args.net}_Accurancy and Loss')
    plt.legend()
    plt.savefig(f'{args.save_dir}/{args.net}_Accurancy and Loss.jpg')  # 自动保存plot出来的图片
    plt.show()

    # 输出best_acc
    mylogger.info(f'Finished training')
    mylogger.info(f'Best Acc: {best_acc:.4f}%')

    # 计算本次运行时间
    end_time = time.time()
    seconds = end_time - start_time
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    mylogger.info("%02d:%02d:%02d" % (h, m, s))

    # # 测试
    # mylogger.info(f'-----------------------------------')
    # mylogger.info(f'Begin test')
    # test()
