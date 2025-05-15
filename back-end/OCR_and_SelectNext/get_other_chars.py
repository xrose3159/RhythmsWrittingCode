"""
输入n张汉字的图片，输出一张与这些汉字不相同的字
"""
import os
from PIL import Image
import os
import sys
import argparse
import numpy as np
import fnmatch
import pickle
import random
import sys
sys.path.append('/root/autodl-tmp/code/OCR_and_SelectNext')
from ocr import ocr
from query import query, rev_query
from pkl_utils import convert_key


def euclidean_distance(vector1, vector2):
    """
    :param vector1: 向量1
    :param vector2: 向量2
    :return: distance between vector1 and vector2
    """
    assert len(vector1) == len(vector2)
    square_diff = [(float(x) - float(y)) ** 2 for x, y in zip(vector1, vector2)]
    distance = sum(square_diff)
    return distance

def str2list(str):
    return [int(i) for i in str]

def calculate_center(vectors):
    """
    :param vectors: a vectors list
    :return: center vector of vectors(a list)
    """
    num_vectors = len(vectors)  # 向量的总数
    num_dimensions = len(vectors[0])  # 向量的维度

    # 将所有向量按照相同的维度顺序进行排列
    vectors = [str2list(vec) for vec in vectors]
    vectors = np.array(vectors)
    center = list(vectors.mean(axis=0))
    return center

def select_next(texts, pkl_path='/root/autodl-tmp/code/OCR_and_SelectNext/four_corner_method/data/tran_rev_common_data.pkl',
                     random_num=10):
    """
    :param texts: 输入的一串汉字
    :param path: 常用字的 向量：汉字 字典的路径
    :param random_num: 在常用字字典中随机选取的向量数量
    :return: 与这些汉字结构不同的汉字
    """
    if texts=='':
        return '甲'
    # 得到这一串汉字的四角码和向量列表
    four_corner_codes = [query(char) for char in texts if char is not '']
    vectors = [convert_key(code) for code in four_corner_codes]
    # print('vectors: ', vectors)

    # 计算向量的中心点
    center = calculate_center(vectors)
    # print('center: ', center)

    # 加载常用字的 向量：汉字 字典
    with open(pkl_path, 'rb') as fd:
        data = pickle.load(fd)

    random_keys = random.sample(list(data.keys()), k=random_num)
    distances = [euclidean_distance(center, random_keys[i]) for i in range(random_num)]
    max_index = distances.index(max(distances))
    options = data[random_keys[max_index]]
    # print('optional chars: ', options)
    # print('option: ', options[0])
    return options[0]


# if __name__ == '__main__':
#     data_dir = '/root/autodl-tmp/ocr_and_seg/temp_dataset'
#     # 加载png图片并使用ocr得到文本
#     print(f'loading pngs from directory: {data_dir}')
#     texts = []
#     for root, dirs, files in os.walk(data_dir):
#         for filename in files:
#             if fnmatch.fnmatch(filename, "*.png"):
#                 png_path = os.path.join(root, filename)
#                 texts.append(ocr(png_path))
#     print('texts: ', texts)
#     option = get_another_char(data_dir)


