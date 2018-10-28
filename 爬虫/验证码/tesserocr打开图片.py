import tesserocr
from PIL import Image

image = Image.open('image.png')

result = tesserocr.image_to_text(image)
print(result)





