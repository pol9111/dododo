import tesserocr
from PIL import Image

image = Image.open('captcha.jpg')
# 转化为灰度图像
image = image.convert('L')
# image = image.convert('1')
# image.show()

# 二值化处理
threshold = 4 # 指定阈值
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()

result = tesserocr.image_to_text(image)
print(result)







