#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   file.py
@Time    :   2022/12/23 08:54:56
@Author  :   Elsa 
@Version :   1.0
@Contact :   elsa_tu@qq.com
@Desc    :   None
'''

# here put the import lib
import tkinter
from tkinter import filedialog
import os

class GetFilePath:
    """获取用户所选文件路径的类"""
    def getpath():
        """获取文件路径"""
        # 获取选择文件路径
        # 实例化
        root = tkinter.Tk()
        root.withdraw()
        # 获取文件夹路径
        # FolderPath=filedialog.askdirectory(title='Please choose a directory')  #看情况自己使用
        f_path = filedialog.askopenfilename(title='Please choose your TTF')
        # print('FolderPath:',FolderPath)
        # print(type(f_path))
        print('获取的文件地址: ', f_path)
        return f_path
    
    def FileSave():
        pwd = os.getcwd()
        r = tkinter.filedialog.asksaveasfilename(title='Please choose a directory',
                                                initialdir=pwd,
                                                initialfile='GlyphIQ.ttf', filetypes=[("TTF", "*.ttf"), ('All files', '*')])
        print(r)
        return r
    
    def ChooseFile():
        pwd = os.getcwd()
        r = tkinter.filedialog.askopenfilenames(title='Please choose your files')
        print(r)
        return r

