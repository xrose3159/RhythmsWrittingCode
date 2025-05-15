import os
import shutil

# 源文件夹路径
src_folder = 'C:\\Users\\86183\\Downloads'

# 目标文件夹路径
dst_folder = 'C:\\Users\\86183\\Documents\\计算机设计大赛\\font_clasification\\data1'

# 遍历源文件夹中的所有文件和子目录
for root, dirs, files in os.walk(src_folder):
    for file_name in files:
        # 检查文件是否以.ttf结尾
        if file_name.endswith('.ttf'):
            # 构造源文件的完整路径
            src_file = os.path.join(root, file_name)
            # 构造目标文件的完整路径
            dst_file = os.path.join(dst_folder, file_name)
            # 移动文件
            shutil.move(src_file, dst_file)
