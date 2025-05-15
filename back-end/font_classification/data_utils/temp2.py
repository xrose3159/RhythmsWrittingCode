import os

src_dir = '/root/autodl-tmp/font_classification/dataset_img'
dst_dir = '/root/autodl-tmp/font_classification/dataset/5'

for folder_name in os.listdir(src_dir):
    folder_path = os.path.join(src_dir, folder_name)
    if os.path.isdir(folder_path):
        dst_folder_path = os.path.join(dst_dir, folder_name)
        if os.path.exists(dst_folder_path):
            print(dst_folder_path)
            os.system(f'rm {dst_folder_path}/*')
            os.system(f'mv {folder_path}/* {dst_folder_path}')
        # else:
            # print('sb')
            # os.system(f'mv {folder_path} {dst_dir}')
