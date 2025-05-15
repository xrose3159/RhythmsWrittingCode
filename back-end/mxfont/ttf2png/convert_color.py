from PIL import Image
import os

# 设置图片所在目录
path = "/root/autodl-tmp/mxfont/data/images/zhizhi"

for filename in os.listdir(path):
    # 只处理 PNG 图像
    if filename.endswith(".png"):
        image = Image.open(os.path.join(path, filename))
        # 将颜色模式更改为 8 位
        image = image.convert("P", palette=Image.ADAPTIVE, colors=256)
        # 保存图像
        image.save(os.path.join(path, filename))