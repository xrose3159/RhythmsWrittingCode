'''
来自https://github.com/howl-anderson/four_corner_method
是直接查表得到的，输入单个汉字，输出汉字的四角码
调用方法：
python ./query.py 民
or
from four_corner_method import FourCornerMethod
fcm = FourCornerMethod()
result = fcm.query('名')
print(result)
'''

import pickle

def rev_query(input_four_corner, path = '/root/autodl-tmp/code/OCR_and_SelectNext/four_corner_method/data/rev_data.pkl'):
    """输入四角码查询汉字"""
    with open(path, 'rb') as fd:
        data = pickle.load(fd)

    return data.get(input_four_corner)

def query(input_char, path = '/root/autodl-tmp/code/OCR_and_SelectNext/four_corner_method/data/data.pkl'):
    """输入汉字查询四角码"""
    with open(path, 'rb') as fd:
        data = pickle.load(fd)

    return data.get(input_char)

# if __name__ == "__main__":
    # # 输入汉字查询四角码
    # input_char = sys.argv[1]
    # input_char = '民'
    # result = query(input_char)

    # # 输入四角码查询汉字
    # input_four_corner = '77747'
    # result = rev_query(input_four_corner)
    # print(result)