"""
MX-Font
Copyright (c) 2021-present NAVER Corp.
MIT license
"""

import argparse
from pathlib import Path

import torch
import sys
sys.path.append('/root/autodl-tmp/code/mxfont')
from utils import refine, save_tensor_to_image
from datasets import get_test_loader
from models import Generator
from sconf import Config
from train import setup_transforms

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f'\nusing {device.type}')

def my_eval_ckpt(data_dir, source_font, result_dir,
            config_path='/root/autodl-tmp/code/mxfont/cfgs/eval.yaml',
            weight='/root/autodl-tmp/code/mxfont/final_result/checkpoints/800000.pth',
            gen_chars_file='/root/autodl-tmp/code/mxfont/data/chn_gen.json'):
    cfg = Config(config_path, default="/root/autodl-tmp/code/mxfont/cfgs/defaults.yaml")
    # print(type(cfg['dset']['test']), cfg['dset']['test'])
    # print(cfg['dset']['test']['data_dir'])
    cfg['dset']['test']['data_dir'] = data_dir
    cfg['dset']['test']['source_font'] = source_font
    cfg['dset']['test']['gen_chars_file'] = gen_chars_file
    img_dir = Path(result_dir)
    img_dir.mkdir(parents=True, exist_ok=True)

    trn_transform, val_transform = setup_transforms(cfg)

    g_kwargs = cfg.get('g_args', {})
    # gen = Generator(1, cfg.C, 1, **g_kwargs).cuda()
    gen = Generator(1, cfg.C, 1, **g_kwargs).to(device)

    weight = torch.load(weight, map_location=device)
    if "generator_ema" in weight:
        weight = weight["generator_ema"]

    gen.load_state_dict(weight)

    # for param in gen.parameters():
    #     print(param.shape)
    # print("Total number of paramerters in gen is {}  ".format(sum(x.numel() for x in gen.parameters())))

    test_dset, test_loader = get_test_loader(cfg, val_transform)
    print('len(test_loader): ', len(test_loader))

    for batch in test_loader:
        # style_imgs = batch["style_imgs"].cuda()
        style_imgs = batch["style_imgs"].to(device)
        # char_imgs = batch["source_imgs"].unsqueeze(1).cuda()
        char_imgs = batch["source_imgs"].unsqueeze(1).to(device)

        out = gen.gen_from_style_char(style_imgs, char_imgs).to(device)
        fonts = batch["fonts"]
        chars = batch["chars"]
        for image, font, char in zip(refine(out), fonts, chars):
            (img_dir / font).mkdir(parents=True, exist_ok=True)
            path = img_dir / font / f"{char}.png"
            save_tensor_to_image(image, path)
    print('Generation Done.')

# 使用配置文件的版本
def eval_ckpt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_paths", nargs="+", help="path to config.yaml", default='/root/autodl-tmp/code/mxfont/cfgs/eval.yaml')
    parser.add_argument("--weight", help="path to weight to evaluate.pth", default='/root/autodl-tmp/code/mxfont/final_result/checkpoints/800000.pth')
    parser.add_argument("--result_dir", help="path to save the result file", default='/root/autodl-tmp/code/result_temp')
    args, left_argv = parser.parse_known_args()
    print(f'args: \n{args} \nleft_argv: \n {left_argv}')

    cfg = Config(args.config_paths, default="/root/autodl-tmp/code/mxfont/cfgs/defaults.yaml")
    cfg.argv_update(left_argv)
    print(f'cfg:')
    print(cfg)
    img_dir = Path(args.result_dir)
    img_dir.mkdir(parents=True, exist_ok=True)

    trn_transform, val_transform = setup_transforms(cfg)

    g_kwargs = cfg.get('g_args', {})
    # gen = Generator(1, cfg.C, 1, **g_kwargs).cuda()
    gen = Generator(1, cfg.C, 1, **g_kwargs).to(device)

    weight = torch.load(args.weight, map_location=device)
    if "generator_ema" in weight:
        weight = weight["generator_ema"]

    gen.load_state_dict(weight)

    # for param in gen.parameters():
    #     print(param.shape)
    print("Total number of paramerters in gen is {}  ".format(sum(x.numel() for x in gen.parameters())))

    test_dset, test_loader = get_test_loader(cfg, val_transform)
    print('len(test_loader): ', len(test_loader))

    for batch in test_loader:
        # style_imgs = batch["style_imgs"].cuda()
        style_imgs = batch["style_imgs"].to(device)
        # char_imgs = batch["source_imgs"].unsqueeze(1).cuda()
        char_imgs = batch["source_imgs"].unsqueeze(1).to(device)

        out = gen.gen_from_style_char(style_imgs, char_imgs).to(device)
        fonts = batch["fonts"]
        chars = batch["chars"]
        for image, font, char in zip(refine(out), fonts, chars):
            (img_dir / font).mkdir(parents=True, exist_ok=True)
            path = img_dir / font / f"{char}.png"
            save_tensor_to_image(image, path)
    print('Generation Done.')


if __name__ == "__main__":
    my_eval_ckpt('/root/autodl-tmp/code/ref_imgs/zhizhi',
                 '/root/autodl-tmp/code/train_final/JiZiJingDianWeiTiJianFan-Shan-GEETYPE-WeiTiGBT-Flash-2.ttf',
                 ' /root/autodl-tmp/code/gen_imgs/zhizhi')
