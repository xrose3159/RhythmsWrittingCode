#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2023/03/09 21:50:30
@Author  :   Elsa 
@Version :   1.0
@Contact :   elsa_tu@qq.com
@Desc    :   None
'''

# here put the import lib
import pygame

class Settings:
    """存储所有设置的类"""
    def __init__(self):
        """初始化静态设置"""
        # 屏幕设置
        self.screen_width = 1386 # 宽 1424
        self.screen_height = 780 # 高 801
        self.bg_color = (230, 230, 230) # 背景色
        self.background = pygame.image.load('images\\bg.png') 