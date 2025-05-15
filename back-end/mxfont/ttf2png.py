import argparse
import os
from PIL import Image, ImageFont, ImageDraw
from datasets.ttf_utils import read_font, render
from datasets import get_filtered_chars


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ttf_path', type=str, default='/root/autodl-tmp/mxfont/data/ttfs/train/ZCOOLKuaiLe-Regular.ttf')
    parser.add_argument('--img_save_folder', type=str, default='/root/autodl-tmp/mxfont/data/images/test1/ZCOOLKuaiLe_35chars')
    parser.add_argument('--text', type=str, default='泷檎涠圄落复街尊宇日俱增仙仁众余倚光冷净初别劝匆历卓坦壤宙姿你好哇我是神奇宝贝乐了滴水')

    args = parser.parse_args()
    font = read_font(args.ttf_path)

    # get the available characters of .ttf file (.txt)
    txt_path = args.ttf_path.replace(".ttf", ".txt")
    if not os.path.exists(txt_path):
        print(f'creating {txt_path}...')
        avail_chars = get_filtered_chars(args.ttf_path)
        with open(txt_path, "w") as f:
            f.write("".join(avail_chars))
    with open(txt_path) as f:
        chars = f.read()

    # get the intersection of the available characters of .ttf file and args.text
    char_filter = list(set(chars).intersection(list(args.text)))
    print('char_filter: ', char_filter)

    # transform the specific characters of .ttf file to png
    if not os.path.isdir(args.img_save_folder):
        os.makedirs(args.img_save_folder)
    for char in char_filter:
        img = render(font, char)
        img.save(os.path.join(args.img_save_folder, f'{char}.png'))
    print('transform done.')


if __name__ == '__main__':
    main()