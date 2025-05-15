"""
使用LPIPS评价两个字体图片之间的相似度
"""

import torch
import lpips
import os
import numpy as np
import argparse
from PIL import Image
from skimage.metrics import structural_similarity as SSIM
import math

# 假定两个目录下的图片完全相同
# 使用lpips计算两个字体图片之间的相似度
def cal_lpips(dir1, dir2, num=20):
    img0_path_list = []
    img1_path_list = []
    for file_name in os.listdir(dir1):   # 预处理得到要比较的所有文件的路径
        img0 = os.path.join(dir1, file_name)
        img1 = os.path.join(dir2, file_name)
        img0_path_list.append(img0)
        img1_path_list.append(img1)

    assert len(img0_path_list) == len(img1_path_list) == num, f'Error. only {len(img0_path_list)} imgs'

    dist_ = []
    for i in range(len(img0_path_list)):
        img0 = lpips.im2tensor(lpips.load_image(img0_path_list[i]))
        img1 = lpips.im2tensor(lpips.load_image(img1_path_list[i]))
        if use_gpu:
            img0 = img0.cuda()
            img1 = img1.cuda()
        lpips_value = loss_fn.forward(img0, img1)
        dist_.append(lpips_value.mean().item())

    # 根据dist_的前5个最小值在整个dist_中的位置得到img0_path_list中对应的名称
    min5 = np.argsort(dist_)[:5]
    min5_name = [img0_path_list[i].split('/')[-1] for i in min5]
    print(min5_name)


    return sum(dist_) / len(img0_path_list)

# 使用MSE计算两个字体图片之间的相似度
def cal_mse(dir1, dir2, num=20):
    img0_path_list = []
    img1_path_list = []
    for file_name in os.listdir(dir1):   # 预处理得到要比较的所有文件的路径
        img0 = os.path.join(dir1, file_name)
        img1 = os.path.join(dir2, file_name)
        img0_path_list.append(img0)
        img1_path_list.append(img1)

    assert len(img0_path_list) == len(img1_path_list) == num, f'Error. only {len(img0_path_list)} imgs'

    dist_ = []
    for i in range(len(img0_path_list)):
        img0 = Image.open(img0_path_list[i]).convert('L')
        img1 = Image.open(img1_path_list[i]).convert('L')
        mse = np.mean((np.array(img0) - np.array(img1)) ** 2)
        dist_.append(mse.mean().item())

    return sum(dist_) / len(img0_path_list)

# 使用psnr计算两个字体图片之间的相似度
def cal_psnr(dir1, dir2, num=20):
    img0_path_list = []
    img1_path_list = []
    for file_name in os.listdir(dir1):   # 预处理得到要比较的所有文件的路径
        img0 = os.path.join(dir1, file_name)
        img1 = os.path.join(dir2, file_name)
        img0_path_list.append(img0)
        img1_path_list.append(img1)

    assert len(img0_path_list) == len(img1_path_list) == num, f'Error. only {len(img0_path_list)} imgs'

    dist_ = []
    for i in range(len(img0_path_list)):
        img0 = Image.open(img0_path_list[i]).convert('L')
        img1 = Image.open(img1_path_list[i]).convert('L')
        mse = np.mean((np.array(img0) - np.array(img1)) ** 2)
        if mse == 0:
            psnr = 100
        else:
            PIXEL_MAX = 255.0
            psnr = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
        dist_.append(psnr)

    return sum(dist_) / len(img0_path_list)

# 使用ssim计算两个字体图片之间的相似度
def cal_ssim(dir1, dir2, num=20):
    img0_path_list = []
    img1_path_list = []
    for file_name in os.listdir(dir1):   # 预处理得到要比较的所有文件的路径
        img0 = os.path.join(dir1, file_name)
        img1 = os.path.join(dir2, file_name)
        img0_path_list.append(img0)
        img1_path_list.append(img1)

    assert len(img0_path_list) == len(img1_path_list) == num, f'Error. only {len(img0_path_list)} imgs'

    dist_ = []
    for i in range(len(img0_path_list)):
        img0 = Image.open(img0_path_list[i]).convert('L')
        img1 = Image.open(img1_path_list[i]).convert('L')
        # 计算结构相似性指数
        ssim_value = SSIM(np.array(img0), np.array(img1), data_range=255)
        dist_.append(ssim_value)

    return sum(dist_) / len(img0_path_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target_folder', type=str, default='/root/autodl-tmp/code/target_imgs')
    parser.add_argument('--gen_folder', type=str, default='/root/autodl-tmp/code/gen_imgs/positive')
    parser.add_argument('--choice', type=str, default='lpips')
    args = parser.parse_args()

    use_gpu = True if torch.cuda.is_available() else False # Whether to use GPU

    spatial = True  # Return a spatial map of perceptual distance.
    # Linearly calibrated models (LPIPS)
    loss_fn = lpips.LPIPS(net='alex', spatial=spatial)  # Can also set net = 'squeeze' or 'vgg'
    if (use_gpu):
        loss_fn.cuda()

    for root, dirs, files in os.walk(args.gen_folder):
        for dir in dirs:
            # 判断dir是否以2_1结尾
            if not dir.endswith('2_1'):
                continue
            gen_font_dir = os.path.join(args.gen_folder, dir)
            font_name = dir.split("_")[0]
            target_font_dir = os.path.join(args.target_folder, font_name)
            if args.choice == 'lpips':
                lpips_value = cal_lpips(gen_font_dir, target_font_dir)
                print(f'{dir}: \t LPIPS:\t %.3f' % lpips_value)
            elif args.choice == 'mse':
                mse_value = cal_mse(gen_font_dir, target_font_dir)
                print(f'{dir}: \t MSE:\t %.3f' % mse_value)
            elif args.choice == 'psnr':
                psnr_value = cal_psnr(gen_font_dir, target_font_dir)
                print(f'{dir}: \t PSNR:\t %.3f' % psnr_value)
            elif args.choice == 'ssim':
                ssim_value = cal_ssim(gen_font_dir, target_font_dir)
                print(f'{dir}: \t SSIM:\t %.3f' % ssim_value)
            else:
                print('Error. No such choice.')



