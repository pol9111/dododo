import pytesseract
from PIL import Image
# from tesseract import image_to_string

image = Image.open("image.png")
text = pytesseract.image_to_string(image)
print("机器识别后的验证码为：" + text)






