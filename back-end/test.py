"""
将字体分类、OCR、选择下一字以及字体生成全部结合起来
执行流程：
送入一张图片后，使用ocr识别出该字，然后选择下一字（可选）
得到10个字之后，对这10个字进行分类，选出最合适的那个字体，然后使用mxfont生成目标字。
如果没有selectNext，则假设用户写的10个字为'一二三四五六七八九十'
"""
from OCR_and_SelectNext.ocr import ocr
from OCR_and_SelectNext.get_other_chars import select_next
from font_classification.api import classify, select_ttf
from font_classification.data_utils.ttf2png import ttf2png
from mxfont.eval import eval_ckpt, my_eval_ckpt
import argparse
import os
class_names = ['圆体', '手写体——普通手写体', '手写体——有笔锋的手写体', '楷书', '行书', '黑体']
dist = {'0':['mini-jian-katong',
             'YeZiGongChangRuiYunNongKaiShu-2',
             'ZiXinFangMengTi-2',
             'MaoKenZhuYuanTi-MaokenZhuyuanTi-2',
             'XiangHeNiZhuangGeManHuai-2'],
        '1':['JiGeiDongTianDeQingShi-2',
              'AaXiaoHuLi（JianFan）-2',
              'AaYueRanTi-2',
              'AaZiTiGuanJiaTianZhen-2',
              'SentySnowMountain'],
        '2':['SanJiWangShuKaiShu-2',
             'AaQianLiJiangShanXiaoLiShu-2',
             'DiPaiTi-2',
             'HanChengQingFengYue-2',
             'HanChengTanFaSheYingBiKaiShu-2'],
        '3':['WoYuJianNiHeJuChunQiu-2',
             'MaShanZheng-Regular',
             'SanJiQiChuanKaiShu-2',
             'SanJiXinWeiBeiJian-2',
             'source'],
        '4':['SanJiZhongYunXiuXingKai-2',
             'MiaoBiShengHua-2',
             'ShenHaiBuJiNiXin-2',
             'YeZiGongChangYouLongXingKai-2',
             'YeZiGongChangZuiHanJiangXingCao-2'],
        '5':['SanJiHuaXinJianTi-2',
             'AaShanHeHeiWei-2',
             'ChaoZiSheMiaoXiuCaiJinBangJianFan-Shan(REEJI-CHAO-JinbangGBT-Flash)-2',
             'HYDaBaiTuW-2',
             'LongZhuTi-Regular-2'],
        'default':'/root/autodl-tmp/code/data_ttf_txt/MaShanZheng-Regular.ttf'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--select_next', type=int, default=1)
    parser.add_argument('--classify', type=int, default=1)
    parser.add_argument('--sample_font_name', default='ZuoYeXingChenQiaShiNi-2')
    parser.add_argument('--sample_chars', type=str, default='一二三四五六七八九十甲')
    parser.add_argument('--source_font_name', default='YaHei')
    parser.add_argument('--ttf_txt_dir', default='/root/autodl-tmp/code/train_final')
    parser.add_argument('--img_folder', default='/root/autodl-tmp/code/ref_imgs')
    parser.add_argument('--result_dir', default='/root/autodl-tmp/code/gen_imgs')
    parser.add_argument('--num_imgs', type=int, default=10)
    args = parser.parse_args()
    print('args: ', args)

    # # img_folder存储ref images
    # img_folder = os.path.join(args.img_folder, f'{args.sample_font_name}_{args.select_next}')
    # if args.select_next:
    #     img_folder = os.path.join(args.img_folder, f'{args.sample_font_name}_1')
    # else:
    #     if args.sample_chars == '一二三四五六七八九十甲':
    #         img_folder = os.path.join(args.img_folder, f'{args.sample_font_name}_0_1_10')
    #     elif args.sample_chars == '一一一一一一一一一一甲':
    #         img_folder = os.path.join(args.img_folder, f'{args.sample_font_name}_0_all_1')
    #     else:
    #         img_folder = os.path.join(args.img_folder, f'{args.sample_font_name}_default')

    # ref font
    ref_font_path = os.path.join(args.ttf_txt_dir, f'{args.sample_font_name}.ttf')
    assert os.path.exists(ref_font_path), f'No {args.sample_font_name}.ttf in {args.ttf_txt_dir}'

    # 生成ref images，并存储到img_folder
    # texts = ''
    # next_char = args.sample_chars[0]
    # for i in range(args.num_imgs):
    #     print(f'next char(char{i}): ', next_char)
    #
    #     ttf2png(ref_font_path, img_folder, next_char)
    #     texts += next_char
    #
    #     # 实际应用时需要使用OCR
    #     # img_path = os.path.join(img_folder, f'{next_char}.png')
    #     # char = ocr(img_path)
    #     # texts += char
    #     # print('OCR result: ', char)
    #     print('texts: ', texts)
    #
    #     if args.select_next:
    #         next_char = select_next(texts)
    #         if next_char in texts:
    #             next_char = select_next(texts)
    #     else:
    #         next_char = args.sample_chars[i+1]
    #
    # assert len(texts) == args.num_imgs, f'len(texts) is {len(texts)}, but expected num_imgs is {args.num_imgs}'

    # 得到source font路径
    if args.classify:
        class_index = classify(img_folder, only=True)
        print(f'\nclassify result: {class_index} ({class_names[class_index]})')
        source_font = dist[f'{class_index}'][0]
        source_font = os.path.join(args.ttf_txt_dir, f'{source_font}.ttf')
    else:
        source_font = os.path.join(args.ttf_txt_dir, f'{args.source_font_name}.ttf')

    # 根据ref images和source font生成图片
    print(args.img_folder, "\n", source_font, "\n", args.result_dir);
    my_eval_ckpt(args.img_folder, source_font, args.result_dir) # 注意args.img_folder里面没有图片，里面是图片文件夹