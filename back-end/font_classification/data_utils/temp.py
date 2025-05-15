import os
import shutil

# 根目录路径
root_folder = '/root/autodl-tmp/font_classification/dataset'

# 递归遍历根目录中的所有目录
for root, dirs, files in os.walk(root_folder):
    for dir_name in dirs:
        # 构造目录的完整路径
        dir_path = os.path.join(root, dir_name)
        # 统计目录中的文件数
        file_count = len(os.listdir(dir_path))
        # 如果文件数少于100，则删除目录及其所有内容
        if file_count < 100:
            print(f"Deleting directory {dir_path} with {file_count} files.")
            shutil.rmtree(dir_path)
