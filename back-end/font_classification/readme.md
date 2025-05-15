```
.
|-- __pycache__
|-- api.py   # 分类时调用的api，classify函数输入图片，返回类别
|-- data_ttf_txt  # 目录，存放了222个ttf文件，以及对应的221个txt文件，似乎有一个没有正确生成
|-- data_utils   # 目录，存放了跟data相关的util函数
    |-- __init__.py
    |-- __pycache__
    |   |-- myfont.cpython-37.pyc
    |   |-- ttf_utils.cpython-37.pyc
    |   `-- ttf_utils.cpython-39.pyc
    |-- get_chars_from_ttf.py # 将args.root_dir下的ttf文件都生成txt文件
    |-- imagefolder_dataset.py
    |-- my_logger.py 
    |-- myfont.py
    |-- temp.py  # 删除文件数少于100的目录及其所有内容
    |-- temp1.py # 将某个目录下的ttf文件都移动到另一个目录
    |-- temp2.py # 将ttf文件归类到另一个文件夹
    |-- test.txt
    |-- train.txt
    |-- ttf2png.py  # ttf2png
    |-- ttf_dataset.py  # 定义dataset
    `-- ttf_utils.py   # ttf_utils
|-- dataset    # 存放数据集
    |-- 0   # 
    |-- 1
    |-- 2
    |-- 3
    |-- 4
    |-- 5
    |-- readme.txt
    |-- test_images.npy
    |-- test_labels.npy
    |-- train_images.npy
    `-- train_labels.npy
|-- my_logger.py
|-- result  # 目录，存放结果
    |-- resnet18_Accurancy\ and\ Loss.jpg
    |-- resnet18_checkpoints
    |-- resnet18_log.txt
    `-- resnet18_test.txt
|-- test.py   # 测试
`-- train.py  # 训练
```

