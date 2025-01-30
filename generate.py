import qrcode
from PIL import Image

data = input("Введите ссылку: ")
img = qrcode.make(data)
img.save('qrcode.png')
Image.open('qrcode.png').show()
