#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   rect.py
@Time    :   2023/03/10 17:08:34
@Author  :   Elsa 
@Version :   1.0
@Contact :   elsa_tu@qq.com
@Desc    :   None
'''

# here put the import lib
import pygame

class Rect:
    """绘制边框"""
    def __init__(self, ai_game, x, y, width, height): # mag为要在按钮上显示的文本
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置矩形边框的尺寸和位置
        self.rect_x = x
        self.rect_y = y
        self.rect_width = width
        self.rect_height = height

        # 设置颜色
        self.WHITE = (153, 46, 46) # 211, 217, 240 (184, 81, 81)

    def draw_rect(self):
        # 绘制矩形边框
        pygame.draw.rect(self.screen, self.WHITE, (self.rect_x, self.rect_y, self.rect_width, self.rect_height), 2)
        # pygame.display.flip()
        print("OK")