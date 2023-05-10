"""
2023/05/01  python 3.11
用pillow包操作图片
"""
from PIL import Image, ImageFilter

image = Image.open("images/girl.png")
print(f"{image.format},{image.size},{image.mode}")
# image.show()

# 裁切图片
img1 = image
rect = (80,20, 310, 360 )   # 只能给四个参数
# img1.crop(rect).show()

# 缩略图
img2 = image
size = (128,128)
img2.thumbnail(size)
# img2.show()

# 滤镜
img3 = image
img3.filter(ImageFilter.CONTOUR).show()

