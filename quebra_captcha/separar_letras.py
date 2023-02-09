import glob,cv2,os

arquivos = glob.glob('ajeitado/*')
for arquivo in arquivos:
    imagem = cv2.imread(arquivo)
    imagem = cv2.cvtColor(imagem,cv2.COLOR_RGB2GRAY)

    #preto branco
    _, nova_imagem = (cv2.threshold(imagem,0,255,cv2.THRESH_BINARY_INV))

    #contorno letras
    contornos, _ = cv2.findContours(nova_imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regiao_letras = []

    #filtrar letrar pelo contorno
    for contorno in contornos:
        (x,y,l,a) = cv2.boundingRect(contorno)
        area = cv2.contourArea(contorno)

        if area > 80:
            regiao_letras.append((x,y,l,a))

    if len(regiao_letras) != 6 :
        continue

    #desenhar contorno; seperar letras

    imagem_final = cv2.merge([imagem]*3)

    i=0
    for retangulo in regiao_letras:
        x,y,l,a = retangulo
        imagem_letra = imagem[y-2:y+a+2, x-2:x+l+2]
        i+=1
        nome_arquivo = os.path.basename(arquivo).replace(".png",f"letra{i}.png")
        cv2.imwrite(f'letras/{nome_arquivo}',imagem_letra)
        cv2.rectangle(imagem_final, (x-2,y-2), (x+l+2, y+a+2), (0,255,0), 2)
    nome_arquivo = os.path.basename(arquivo)
    cv2.imwrite(f"identificado/{nome_arquivo}",imagem_final)