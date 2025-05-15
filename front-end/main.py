import sys 
import pygame 
import time


from button import Button
from settings import Settings
from rect import Rect
from get_user_input import GetInput
from get_file_path import GetFilePath
from testinputbox import TextBox

class Demo:
    """管理资源和行为的类"""

    def __init__(self):
        pygame.init() # 初始化
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # pygame.display.set_mode()来创建一个显示窗口
        pygame.display.set_caption("智易字坊") # 对生成的windows窗口设置标题 
        self.text_box = TextBox(578, 67, 785, 63)
        self.button1 = Button(self, "文件", 2, 2, 72, 42) # 创建文件按钮
        self.button2 = Button(self, "生成", 629, 609, 127, 150) # 创建生成按钮
        self.button3 = Button(self, "1", 203, 675, 85, 88) # 创建方块1按钮
        self.button4 = Button(self, "2", 300, 675, 85, 88) # 创建方块2按钮
        self.button5 = Button(self, "3", 392, 675, 85, 88) # 创建方块3按钮
        self.button6 = Button(self, "4", 487, 675, 85, 88) # 创建方块4按钮
        self.button7 = Button(self, "PDF", 40, 105, 148, 36) # 创建文件按钮
        self.button8 = Button(self, "sf", 40, 105, 148, 36) # 创建书法按钮
        self.button9 = Button(self, "S", 653, 181, 82, 81) 

    def run_game(self): # 事件循环
        """主循环"""
        while True:
            # self.input_box.draw(self.screen)
            # self._update_screen()
            self._check_events()
            # self._update_input_box()
            
            # self._pic()
            # self._update_screen()
            # self._pic()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get(): # 函数pygame.event.get()返回一个列表，其中包含它在上一次被调用后发生的所有事件
            # self.input_box.handle_event(event)  
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # 按键
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN: # 无论单击屏幕什么地方都会检测到MOUSEBUTTONDOWN
                mouse_pos = pygame.mouse.get_pos() # 所以使用pygame.mouse.get_pos()，它返回一个元组，包含单击时鼠标的x,y坐标
                print(mouse_pos)
                self._check_button(mouse_pos) # 将值传递给方法_check_button()

    def _check_button(self, mouse_pos):
        """在单击按钮时做出不同回应"""
        button_clicked1 = self.button1.rect.collidepoint(mouse_pos)
        button_clicked2 = self.button2.rect.collidepoint(mouse_pos)
        button_clicked3 = self.button3.rect.collidepoint(mouse_pos)
        button_clicked4 = self.button4.rect.collidepoint(mouse_pos)
        button_clicked5 = self.button5.rect.collidepoint(mouse_pos)
        button_clicked6 = self.button6.rect.collidepoint(mouse_pos)
        button_clicked7 = self.button7.rect.collidepoint(mouse_pos)
        button_clicked8 = self.button8.rect.collidepoint(mouse_pos)
        button_clicked9 = self.button9.rect.collidepoint(mouse_pos)
        # rect1 = Rect(self, 203, 675, 85, 88) # 203, 675
        if button_clicked1:
            print("文件")

        if button_clicked2:
            print("生成")
            self._draw_pic(783, 148, 'font\\豫.png') # 1
            self._draw_pic(933, 147, 'font\\章.png') # 2
            self._draw_pic(1081, 148, 'font\\故.png') # 3
            self._draw_pic(1231, 148, 'font\\郡.png') # 4
            self._draw_pic(783, 300, 'font\\洪.png') # 5
            self._draw_pic(934, 299, 'font\\都.png') # 6
            self._draw_pic(1081, 298, 'font\\新.png') # 7
            self._draw_pic(1231, 299, 'font\\府.png') # 8
            pygame.display.flip()

        if button_clicked3:
            print("1")
            # self._update_screen()
            rect1 = Rect(self, 203, 675, 85, 88) # 203, 675
            rect1.draw_rect()
            pygame.display.flip()
            # time.sleep(1000)

        if button_clicked4:
            print("2")
            # self._update_screen()
            rect1 = Rect(self, 300, 675, 85, 88) # 203, 675
            rect1.draw_rect()
            pygame.display.flip()
            # time.sleep(1000)

        if button_clicked5:
            print("3")
            # self._update_screen()
            rect1 = Rect(self, 392, 675, 85, 88) # 203, 675
            rect1.draw_rect()
            pygame.display.flip()
            # time.sleep(1000)

        if button_clicked6:
            print("4")
            # self._update_screen()
            rect1 = Rect(self, 487, 675, 85, 88) # 203, 675
            rect1.draw_rect()
            pygame.display.flip()
            # time.sleep(1000)

        if button_clicked7:
            print("PDF")
            directory_path = GetFilePath.FileSave()
            GetInput.showmsg("生成的TTF文件已经保存在指定目录下\n请查收")

        if button_clicked8: # 书法
            print("sf")
            directory_path = GetFilePath.ChooseFile()
            time.sleep(1)
            self._draw_pic(205, 679, 'shufa\\2.png')
            self._draw_pic(301, 679, 'shufa\\3.png')
            self._draw_pic(394, 679, 'shufa\\5.png')
            self._draw_pic(489, 679, 'shufa\\7.png')
            pygame.display.flip()
            GetInput.showmsg("导入成功！")
            time.sleep(1)
            self._draw_pic(652, 179, 'shufa\\11.png')
            self._draw_pic(654, 286, 'shufa\\22.png')
            self._draw_pic(654, 392, 'shufa\\33.png')
            self._draw_pic(654, 498, 'shufa\\44.png')
            self._draw_pic(779, 463, 'png\\yuan.png')
            pygame.display.flip()
        
        if button_clicked9:
            print("S")
            self._draw_pic(713, 237, 'png\\选中对号.png')
            pygame.display.flip()
            time.sleep(10)

    
    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_a:
            self._draw_pic(205, 676, 'png\\切.png')
            pygame.display.flip()
            time.sleep(0.5)
            self._draw_pic(876, 556, 'png\\xia1.png')
            pygame.display.flip()

        elif event.key == pygame.K_s:
            self._update_screen()
            self._draw_pic(205, 676, 'png\\切.png')
            self._draw_pic(301, 676, 'png\\议.png')
            pygame.display.flip()
            time.sleep(0.5)
            self._draw_pic(876, 556, 'png\\xia2.png')
            pygame.display.flip()

        elif event.key == pygame.K_d:
            self._update_screen()
            self._draw_pic(205, 676, 'png\\切.png')
            self._draw_pic(301, 676, 'png\\议.png')
            self._draw_pic(394, 676, 'png\\意.png')
            pygame.display.flip()
            time.sleep(0.5)
            self._draw_pic(876, 556, 'png\\xia3.png')
            pygame.display.flip()

        elif event.key == pygame.K_f:
            self._update_screen()
            self._draw_pic(205, 676, 'png\\切.png')
            self._draw_pic(301, 676, 'png\\议.png')
            self._draw_pic(394, 676, 'png\\意.png')
            self._draw_pic(489, 676, 'png\\康.png')
            pygame.display.flip()
            time.sleep(1.5) 
            self._draw_pic(652, 179, 'png\\智1.png')
            self._draw_pic(654, 286, 'png\\智2.png')
            self._draw_pic(654, 392, 'png\\智3.png')
            self._draw_pic(654, 498, 'png\\智4.png')
            self._draw_pic(779, 463, 'png\\yuan.png')
            pygame.display.flip()

        elif event.key == pygame.K_q:
            # 按Q键结束
            sys.exit()

    def _draw_pic(self, image_x, image_y, path):
        """绘制PNG"""
        image = pygame.image.load(path)
        image_width, image_height = image.get_size()
        self.screen.blit(image, (image_x, image_y))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        
        self.screen.fill(self.settings.bg_color) # 调用方法fill()使这种背景色填充屏幕，用于处理surface，只接受一个实参：颜色
        self.screen.blit(self.settings.background, (0, 0)) # 背景图片填充屏幕
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = Demo()
    ai._update_screen()
    ai.run_game()