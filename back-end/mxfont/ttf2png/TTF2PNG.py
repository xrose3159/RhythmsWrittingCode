import os

from PIL import Image, ImageFont, ImageDraw, ImagePalette

def ttf2png(text, TTFpath, PNGpath):
    """"""
    os.mkdir(PNGpath)
    font = ImageFont.truetype(TTFpath, 90, encoding='unic') # 打开一个TTF字体文件并设置字体大小
    for i,char in enumerate(text):
        image = Image.new('RGB', (128, 128), (255, 255, 255)) # 新建一个RGB图片 尺寸为128x128像素 背景色为白色
        # image = image.convert("P", palette=Image.ADAPTIVE, colors=256) # 将颜色模式更改为8位
        image = image.quantize(colors=256)
        draw = ImageDraw.Draw(image) # 创建一个 ImageDraw 对象 用来在图片上进行绘制
        text_width, text_height = draw.textsize(char, font=font)
        x = (128 - text_width) / 2
        y = (128 - text_height) / 2
        draw.text((x, y), char, font=font, fill=(0, 0, 0))
        image.save(f'{PNGpath}/{char}.png')

def main():
    """主函数"""
    text = "圄檎泷涠"
    #text = "一其画北丹习你高动建莎夹吻峙度闹尾杨注拧采恋诓"
    TTFpath = "./test1.ttf"
    PNGpath = "./test1"
    ttf2png(text=text, TTFpath=TTFpath, PNGpath=PNGpath)

if __name__ == "__main__":
    main()
