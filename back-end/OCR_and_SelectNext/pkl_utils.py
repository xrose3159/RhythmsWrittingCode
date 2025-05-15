"""
来自https://github.com/howl-anderson/four_corner_method
是直接查表得到的，输入单个汉字，输出汉字的四角码
调用方法：
python ./query.py 民
or
from four_corner_method import FourCornerMethod
fcm = FourCornerMethod()
result = fcm.query('名')
print(result)
"""

import pickle
import os
from collections import defaultdict

def convert_key(key, num=10):
    counters = [key.count(str(i)) for i in range(num)]
    # 将计数器转换为字符串格式并拼接
    result = "".join([f"{counters[i]}" for i in range(num)])
    assert len(result) == 10, f'Error, len(result)=={len(result)}'
    return result

def change_dict(data_dict):
    """
    data_dict: dict, {four_corner: char}
    将四角码转换成10位的向量，第i位代表数字i在四角码中出现的次数
    e.g. "48955" -> '0000120011'
    """
    new_dict = {}
    for k, v in data_dict.items():
        new_key = convert_key(k)
        if new_key in new_dict:
            new_dict[new_key] = new_dict[new_key] + v
        else:
            new_dict[new_key] = v
    return new_dict

def tran_pkl(src_path = 'four_corner_method/data/rev_data.pkl',
              dest_path = 'four_corner_method/data/tran_rev_data.pkl'):
    """
    将rev_data.pkl：{four_corner: char}
    转换为
    tran_rev_data.pkl：{vector(10bits): char}
    """
    with open(src_path, 'rb') as fd:
        data = pickle.load(fd)

    if not os.path.exists(dest_path):
        new_dict = change_dict(data)
        with open(dest_path, 'wb') as f:
            pickle.dump(new_dict, f)
        print('Tran done.')

def rev_pkl(src_path = 'four_corner_method/data/data.pkl',
              dest_path = 'four_corner_method/data/rev_data.pkl'):
    """
    将data.pkl：{char: four_corner}
    转换为
    rev_data.pkl：{four_corner: char}
    """
    with open(src_path, 'rb') as fd:
        data = pickle.load(fd)

    if not os.path.exists(dest_path):
        new_dict = defaultdict(list)
        for k, v in data.items():
            new_dict[v].append(k)
        with open(dest_path, 'wb') as f:
            pickle.dump(new_dict, f)
        print('Rev done.')

def comm_pkl(src_path='four_corner_method/data/data.pkl',
             dest_path='four_corner_method/data/common_data.pkl',
             txt_path='common.txt'):
    with open(src_path, 'rb') as fd:
        data = pickle.load(fd)
    with open(txt_path, 'r') as f:
        keys = f.read()
    if not os.path.exists(dest_path):
        new_dict = {k: data[k] for k in keys if k in data}
        with open(dest_path, 'wb') as f:
            pickle.dump(new_dict, f)
        print('Common chars done.')

# if __name__ == "__main__":
    # 从data.pkl -> rev_data.pkl
    # path1 = 'four_corner_method/data/data.pkl'
    # path2 = 'four_corner_method/data/rev_data.pkl'
    # path3 = 'four_corner_method/data/tran_rev_data.pkl'
    # rev_pkl(path1, path2)
    # tran_pkl(path2, path3)
    # with open(path1, 'rb') as fd:
    #     data1 = pickle.load(fd)
    # with open(path2, 'rb') as fd:
    #     data2 = pickle.load(fd)
    # with open(path3, 'rb') as fd:
    #     data3 = pickle.load(fd)
    # print('OK!')

    # # 得到common pkl
    # path1 = 'four_corner_method/data/data.pkl'
    # path2 = 'four_corner_method/data/common_data.pkl'
    # path3 = 'four_corner_method/data/rev_common_data.pkl'
    # path4 = 'four_corner_method/data/tran_rev_common_data.pkl'
    # txt_path = 'common.txt'
    # comm_pkl(path1, path2, txt_path)
    # rev_pkl(path2, path3)
    # tran_pkl(path3, path4)
    # with open(path2, 'rb') as fd:
    #     data1 = pickle.load(fd)
    # with open(path3, 'rb') as fd:
    #     data2 = pickle.load(fd)
    # with open(path4, 'rb') as fd:
    #     data3 = pickle.load(fd)
    # print('OK!')