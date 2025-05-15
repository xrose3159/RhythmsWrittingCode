import argparse
import os
from PIL import Image, ImageFont, ImageDraw
import sys
sys.path.append('/root/autodl-tmp/code/font_classification/data_utils')
from ttf_utils import get_filtered_chars, read_font, render
import os
import random
import re

def ttf2png(ttf_path, save_folder, text):
    font = read_font(ttf_path)
    # get the available characters of .ttf file (.txt)
    txt_path = ttf_path.replace(".ttf", ".txt")
    if not os.path.exists(txt_path):
        print(f'creating {txt_path}...')
        avail_chars = get_filtered_chars(ttf_path)
        with open(txt_path, "w") as f:
            f.write("".join(avail_chars))
    with open(txt_path) as f:
        chars = f.read()

    # get the intersection of the available characters of .ttf file and args.text
    if text is None:
        char_filter = list(random.sample(set(chars), 400))
    else:
        char_filter = list(set(chars).intersection(list(text)))
    char_filter = [char for char in char_filter if 0x4E00 <= ord(char) <= 0x9FA5]
    # print(f'char_filter: {len(char_filter)}, {char_filter}')

    # transform the specific characters of .ttf file to png
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for char in char_filter:
        img = render(font, char)
        img.save(os.path.join(save_folder, f'{char}.png'))
    # print(f'Transform done. Images in {save_folder}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ttf_path', type=str,
                        default='/root/autodl-tmp/code/train_final/04281520.ttf')
    parser.add_argument('--ttf_folder', type=str,
                        default=None)
    parser.add_argument('--img_save_folder', type=str, default='/root/autodl-tmp/code/ref_imgs_target')
    parser.add_argument('--text', type=str, default='吴勿只绘毁燃估阳莫设')

    args = parser.parse_args()

    # 遍历目录下的所有文件
    if args.ttf_folder:
        for root, dirs, files in os.walk(args.ttf_folder):
            for file in files:
                # 判断文件后缀名是否为.ttf
                if os.path.splitext(file)[1] == '.ttf':
                    ttf_path = os.path.join(root, file)
                    save_folder = os.path.join(args.img_save_folder, os.path.splitext(file)[0])
                    print(file)
                    print(save_folder)
                    ttf2png(ttf_path, save_folder, args.text)
    elif args.ttf_path:
        print("ttf_path: ", args.ttf_path)
        ttf_name = os.path.basename(args.ttf_path)
        save_folder = os.path.join(args.img_save_folder, os.path.splitext(ttf_name)[0])
        print("save_folder: ", save_folder)
        ttf2png(args.ttf_path, save_folder, args.text)