'''
来自https://github.com/howl-anderson/four_corner_method
是直接查表得到的，输入单个汉字，输出汉字的四角码
本目录下大部分文件都是来自这个github仓库
'''
from four_corner_method import FourCornerMethod

fcm = FourCornerMethod()
result = fcm.query('名')

print(result)

# 输出
# 77747