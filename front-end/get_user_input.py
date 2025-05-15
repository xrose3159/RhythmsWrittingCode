#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_user_input.py
@Time    :   2022/12/23 18:03:21
@Author  :   Elsa 
@Version :   1.0
@Contact :   elsa_tu@qq.com
@Desc    :   None
'''

# here put the import lib
import tkinter as tk
from tkinter import messagebox

class GetInput:
    """显示弹窗获取用户输入"""
    def getinput2(text1, text2):
        """"""
        # 创建窗口
        root = tk.Tk()
        # 创建标签
        tk.Label(root, text=text1).grid(row=0)
        tk.Label(root, text=text2).grid(row=1)
        # 创建文本框
        e1 = tk.Entry(root)
        e2 = tk.Entry(root)
        # 布局
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        # 创建按钮
        tk.Button(root, text='OK', command=root.quit).grid(row=3, column=1, sticky=tk.W+tk.E, padx=10, pady=10)

        # 开始事件循环
        root.mainloop()

        # 获取文本框中输入的内容
        id = e1.get()
        password = e2.get()
        root.destroy() # 关闭root窗口

        # 返回输入的内容
        return id, password

    def getinput1(text):
        """"""
        root = tk.Tk()
        tk.Label(root, text=text).grid(row=0)
        e1 = tk.Entry(root)
        e1.grid(row=0, column=1)
        tk.Button(root, text='OK', command=root.quit).grid(row=2, column=1, sticky=tk.W+tk.E, padx=10, pady=10)
        root.mainloop()
        id = e1.get()
        root.destroy() # 关闭root窗口
        return id

    def showmsg(message):
        """消息弹窗"""
        question=tk.Tk()
        question.withdraw()
        messagebox.showinfo("提示",message)