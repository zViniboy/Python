import cv2,os,glob
import numpy as np
from PIL import Image

def tratar_imagens(pasta_origem,pasta_destino='ajeitado'):
    arquivos = glob.glob(f"{pasta_origem}/*")
    for arquivo in arquivos:
        image = cv2.imread(arquivo)
        image_cinza = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image_cinza = cv2.dilate(image_cinza, np.ones((3, 4), np.uint8))
        image_cinza = cv2.erode(image_cinza, np.ones((2, 2), np.uint8))
        _,imagem_tratada = cv2.threshold(image_cinza, 127, 255, cv2.THRESH_TOZERO or cv2.THRESH_OTSU)
        nome_arquivo = os.path.basename(arquivo)
        cv2.imwrite(f'{pasta_destino}/{nome_arquivo}', imagem_tratada)

    arquivos = glob.glob(f"{pasta_destino}/*")
    for arquivo in arquivos:
        imagem = Image.open(arquivo)
        imagem = imagem.convert("P")
        imagem2 = Image.new("P", imagem.size, 255)

        for x in range(imagem.size[1]):
            for y in range(imagem.size[0]):
                cor_pixel = imagem.getpixel((y, x))
                if cor_pixel == 139:
                    imagem2.putpixel((y, x), 0)

        nome_arquivo = os.path.basename(arquivo)
        imagem2 = imagem2.convert('RGB')
        imagem2.save(f'{pasta_destino}/{nome_arquivo}')

if __name__ == '__main__':
    tratar_imagens('bdcaptcha')