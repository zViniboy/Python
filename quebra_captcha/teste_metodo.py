from tkinter import Image
import cv2
from PIL import Image
import numpy as np

metodos = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
]

image = cv2.imread('./bdcaptcha/captcha3.png')

image_cinza = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
image_cinza = cv2.dilate(image_cinza, np.ones((3, 4), np.uint8))
image_cinza = cv2.erode(image_cinza, np.ones((2, 2), np.uint8))

i = 0
for metodo in metodos:
    i+=1
    _,imagem_tratada = cv2.threshold(image_cinza,127,255,metodo or cv2.THRESH_OTSU)
    
    cv2.imwrite(f'./testesmetodos/imagem_tratada_{i}.png',imagem_tratada)

imagem = Image.open('./testesmetodos/imagem_tratada_4.png')
imagem = imagem.convert("P")
imagem2 = Image.new("P", imagem.size, 255)

for x in range(imagem.size[1]):
    for y in range(imagem.size[0]):
        cor_pixel = imagem.getpixel((y, x))
        if cor_pixel == 139:
            imagem2.putpixel((y, x), 0)

imagem2 = imagem2.convert('RGB')
imagem2.save('imagemfinal.png')