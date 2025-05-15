import os
import sys
sample_fonts = ['TianShiBaoDiaoTiJian-1',
                'AaWeiTaNingMengCha-2',
                'AaShanHeHeiWei-2']
positive_fonts = ['JiZiJingDianWeiTiJianFan-Shan-GEETYPE-WeiTiGBT-Flash-2',
                  'JiZiJingDianXiYuanJianFan-Shan-GEETYPE-XiYuanGBT-Flash-2',
                  'No.176-ShangShouLuBanSongTi-2']
negative_fonts = ['JiZiJingDianXiYuanJianFan-Shan-GEETYPE-XiYuanGBT-Flash-2',
                  'No.176-ShangShouLuBanSongTi-2',
                  'JiZiJingDianWeiTiJianFan-Shan-GEETYPE-WeiTiGBT-Flash-2']

# 得到所有参考字
# for j in range(3):
#     os.system(f"python ttf2png.py --ttf_path select_next 1 --classify 0 --sample_font_name {sample_fonts[j]} --num_imgs 10")
#     os.system(f"python test.py --select_next 1 --classify 0 --sample_font_name {sample_fonts[j]} --num_imgs 10")
#     os.system(f"python test.py --select_next 1 --classify 0 --sample_font_name {sample_fonts[j]} --num_imgs 10")

# # 补全不足10个图片的目录
# from font_clasification.data_utils.ttf2png import ttf2png
# sample_font_path = '/root/autodl-tmp/code/data_ttf_txt/ShenHaiLiDeXingChen-2.ttf'
# img_folder = '/root/autodl-tmp/code/ref_imgs/ShenHaiLiDeXingChen-2_1'
# ttf2png(sample_font_path, img_folder, '圆')

# 生成unicode码
# text = "全国大学生计算机设计大赛"
# unicode_list = []
# for i in text:
#     unicode_list.append(hex(ord(i)))
# print(unicode_list)
# for i in range(3):
#     os.system(f"python ttf2png.py --ttf_path /root/autodl-tmp/code/train_final/{sample_fonts[i]}.ttf --text {text}")
# for i in range(3):
#     os.system(f"python ttf2png.py --ttf_path /root/autodl-tmp/code/train_final/{positive_fonts[i]}.ttf --text {text}")
# for i in range(3):
#     os.system(f"python ttf2png.py --ttf_path /root/autodl-tmp/code/train_final/{negative_fonts[i]}.ttf --text {text}")

# 生成字
# _img_folder = '/root/autodl-tmp/code/ref_imgs'
# for i in range(3):
#     img_folder = os.path.join(_img_folder, sample_fonts[i])
#     os.system(
#         f"python test.py  --classify 0 --select_next 1 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --source_font_name {positive_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/positive")
#     os.system(
#         f"python test.py  --classify 0 --select_next 1 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --source_font_name {negative_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/negative")
# for i in range(3):
#     img_folder = os.path.join(_img_folder, sample_fonts[i])
#     os.system(
#             f"python test.py  --classify 0 --select_next 0 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --source_font_name {positive_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/positive")
#     os.system(
#             f"python test.py  --classify 0 --select_next 0 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --source_font_name {negative_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/negative")
# for i in range(3):
#     img_folder = os.path.join(_img_folder, sample_fonts[i])
#     os.system(
#         f"python test.py  --classify 0 --select_next 1 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/default")
#     os.system(
#         f"python test.py  --classify 0 --select_next 0 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/default")
# for i in range(3):
#     img_folder = os.path.join(_img_folder, sample_fonts[i])
#     os.system(f"python test.py  --classify 0 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --source_font_name {sample_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/same")

_img_folder = '/root/autodl-tmp/code/ref_imgs'
for i in range(3):
    img_folder = os.path.join(_img_folder, f'custom')
    os.system(
        f"python test.py  --classify 0 --select_next 1 --img_folder {img_folder} --sample_font_name {sample_fonts[i]} --source_font_name {positive_fonts[i]} --num_imgs 10 --result_dir /root/autodl-tmp/code/gen_imgs/{i}")

# # 创建全1的目录
# import shutil
# for i in range(5):
#     src_path = f'/root/autodl-tmp/code/ref_imgs/{sample_fonts[i]}/{sample_fonts[i]}_0_1_10/一.png'
#     dst_path = f'/root/autodl-tmp/code/ref_imgs/{sample_fonts[i]}/{sample_fonts[i]}_0_all_1'
#     for j in range(10):
#         dest_path = os.path.join(dst_path, f'{j}.png')
#         shutil.copy(src_path, dest_path)







