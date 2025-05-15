'''
来自：https://github.com/charlesXu86/char_featurizer
支持输入多个汉字，输出汉字的声母、韵母、声调和四角码
是使用tf训练出来的
'''

from char_featurizer import Featurizer

featurizer = Featurizer()

data = '明'

result = featurizer.featurize(data)
print(result)

# 输出
# ([['m'], ['t'], ['q'], ['n'], ['j'], ['w']],      # 声母
# [['ing'], ['ian'], ['u'], ['i'], ['ia'], ['an']], # 韵母
# [['2'], ['1'], ['4'], ['3'], ['1'], ['2']],       # 声调
# ('6', '1', '4', '2', '3', '1'),
# ('7', '0', '0', '7', '0', '1'),
# ('0', '8', '7', '2', '2', '1'),
# ('2', '0', '3', '9', '3', '1'),
# ('0', '4', '2', '2', '2', '2'))