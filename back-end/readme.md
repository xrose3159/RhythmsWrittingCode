#  笔韵智枢项目后端

<img src="https://img.shields.io/badge/Python-≥3.9-blue" alt="python"> 

## 环境搭建

1. 安装 Python（≥3.9）和 pip

2. 安装项目依赖

   ```shell
   pip install -r requirements.txt
   ```



## 代码结构


```
.
├── font_classification   # 源字体数据优化
│   ├── api.py
│   ├── dataset
│   ├── data_ttf_txt
│   ├── data_utils
│   ├── my_logger.py
│   ├── __pycache__
│   ├── readme.md
│   ├── result
│   ├── test.py
│   └── train.py
├── mxfont    # 字体生成
│   ├── cfgs
│   ├── data
│   ├── datasets
│   ├── eval.py
│   ├── final_result
│   ├── get_chars_from_ttf.py
│   ├── inference.ipynb
│   ├── LICENSE
│   ├── models
│   ├── NOTICE
│   ├── readme.md
│   ├── trainer
│   ├── train.py
│   ├── ttf2png
│   ├── ttf2png.py
│   └── utils
├── OCR_and_SelectNext    # 参考字数据优化
│   ├── common.txt
│   ├── data
│   ├── dev_requirements.txt
│   ├── four_corner_1.py
│   ├── four_corner_2.py
│   ├── four_corner_method
│   ├── get_other_chars.py
│   ├── Makefile
│   ├── MANIFEST.in
│   ├── ocr.py
│   ├── parse.py
│   ├── pkl_utils.py
│   ├── query.py
│   ├── README.md
│   ├── readme_OCR_and_SelectNext.md
│   └── setup.py
├── convert_color.py    # 将彩色图片转换为灰度图片
├── eval.py    # 评价指标
├── readme.md  
├── shell.py    # 脚本文件
├── test.py   # 字体生成
└── ttf2png.py
```









