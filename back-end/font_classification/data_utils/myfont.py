import os
import torch
import torchvision
from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset, DataLoader, random_split
import numpy as np
from PIL import Image

def get_npy(data_dir='/root/autodl-tmp/font_classification/dataset', train_ratio=0.8):
    # 创建 ImageFolder 数据集
    dataset = ImageFolder(data_dir)

    # 计算训练集和测试集的大小
    train_size = int(len(dataset) * train_ratio)
    test_size = len(dataset) - train_size

    # 使用 random_split 函数划分数据集
    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

    # 保存训练集
    train_data = [(np.asarray(data), label) for data, label in train_dataset]
    train_images = np.array([data for data, _ in train_data])
    train_labels = np.array([label for _, label in train_data])
    np.save(os.path.join(data_dir,'train_images.npy'), train_images)
    np.save(os.path.join(data_dir, 'train_labels.npy'), train_labels)
    #
    # 保存测试集
    test_data = [(np.asarray(data), label) for data, label in test_dataset]
    test_images = np.array([data for data, _ in test_data])
    test_labels = np.array([label for _, label in test_data])
    np.save(os.path.join(data_dir,'test_images.npy'), test_images)
    np.save(os.path.join(data_dir, 'test_labels.npy'), test_labels)

    print('creating .npy done.')


class MyFont(Dataset):
    def __init__(self, root='/root/autodl-tmp/font_classification/dataset',
                 transform=None, target_transform=None, train=True):
        super(MyFont, self).__init__()
        if train:
            data_file = os.path.join(root, 'train_images.npy')
            label_file = data_path = os.path.join(root, 'train_labels.npy')
        else:
            data_file = os.path.join(root, 'test_images.npy')
            label_file = data_path = os.path.join(root, 'test_labels.npy')
        if not os.path.exists(data_file) or not os.path.exists(label_file):
            print(f'creating {data_file} and {label_file}')
            get_npy(root, 0.8)

        print(f'loading data from {data_file}...')
        self.data = np.load(data_file)
        self.targets = np.load(label_file)
        print(len(self.data), len(self.targets))
        self.transform = transform
        self.target_transform = target_transform
        # for i in range(6):
        #     print(sum(self.targets==i))

    def __getitem__(self, index):
        img, target = self.data[index], self.targets[index]

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        return len(self.data)

if __name__ == '__main__':
    _trainset = MyFont('/root/autodl-tmp/font_classification/dataset', train=True)
    train_loader = DataLoader(_trainset, 128, shuffle=True)
    print(_trainset.data[0].shape)