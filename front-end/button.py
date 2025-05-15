#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   button.py
@Time    :   2023/03/09 21:48:55
@Author  :   Elsa 
@Version :   1.0
@Contact :   elsa_tu@qq.com
@Desc    :   None
'''

# here put the import lib
import pygame.font

class Button:
    """绘制游戏开始按钮"""

    def __init__(self, ai_game, mag, left, y, width, height): # mag为要在按钮上显示的文本
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = width, height
        self.button_color = (131, 175, 155) # 设置按钮的rect对象为亮绿色
        self.text_color = (255, 255, 255) # 使文本为白色
        self.font = pygame.font.SysFont('Consolas', 40) # 指定用什么字体渲染文本，None表示使用默认字体，48为字号SimHei

        # 创建按钮的rect对象并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height) # 创建一个表示按钮的rect对象
        self.rect.left = left
        self.rect.y = y
        # self.rect.center = self.screen_rect.center # 并将其center属性设置为屏幕的center属性
        

        # 按钮的标签只需要创建一次
        # Pygame创建文本的方式为将要显示的字符串渲染为图像，调用_prep_msg()来处理
        self._prep_msg(mag)
 
    def _prep_msg(self, msg):
        """将msg渲染为图像并使其在按钮上居中"""
        # 方法font.render()将储存在msg中的文本转化为图像，并将图像储存在msg_image中
        # 方法font.render()接受一个布尔实参，指定开启还是关闭反锯齿功能（开启会使文本边缘更平滑
        # 余下的两个实参分别为文本颜色和背景色。如果没有指定背景色，Pygame渲染文本时将使用透明背景
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect() # 根据文本图像创建一个rect对象
        self.msg_image_rect.center = self.rect.center # 将其center属性设置为按钮的center属性，使文本在按钮上居中
        #self.msg_image_rect.left = 

    

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        # 调用screen.fill()来绘制表示按钮的矩形
        self.screen.fill(self.button_color, self.rect)
        # 调用screen.blit()向它传递一幅图像以及与图像相关联的rect对象
        self.screen.blit(self.msg_image, self.msg_image_rect)