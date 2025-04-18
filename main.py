import numpy as np
import cv2
import sys

def ingenuo(img, windowSize):
    rows, cols, channels = img.shape
    altura, largura = windowSize, windowSize
    img2 = img.copy()
    
    for row in range(altura // 2, rows - altura // 2):
        for col in range(largura // 2, cols - largura // 2):
            soma = 0
            for x in range(row - (altura // 2), row + (altura // 2)):
                for y in range(col - (largura // 2), col + (largura // 2)):
                    soma += img[x, y]
            img2[row, col] = soma / (altura * largura)
            
    cv2.imshow('teste_blur', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def segmentacao(img, windowSize):
    rows, cols, channels = img.shape
    img_s = img.copy()
    img_s2 = img.copy()
    altura, largura = windowSize, windowSize
    
    for row in range(rows):
        for col in range(largura // 2, cols - largura // 2):
            soma = 0
            for x in range(col - (largura // 2), col + (largura // 2)):
                soma += img[row, x]
            img_s[row,col] = soma / altura
    cv2.imshow('segmentacao_parte1', img_s)
    
    for col in range(largura // 2, cols - (largura // 2)):
        for row in range(altura // 2, rows - altura // 2):
            soma = 0
            for x in range(row - (altura // 2), row + (altura // 2)):
                soma += img_s[x, col]
            img_s2[row,col] = soma / altura
    cv2.imshow('segmentacao_parte2', img_s2)
    
def integral(img, windowSize):
    rows, cols, channels = img.shape
    img_integral = img.copy()
    img_blur = img.copy()
    
    
    for row in range(rows):
        for col in range(1, cols):
            img_integral[row, col] = img[row, col] + img_integral[row, col-1]
        
    for row in range(1, rows):
        for col in range(cols):
            img_integral[row, col] = img_integral[row, col] + img_integral[row-1, col]
    
    w_size = windowSize // 2
    for row in range(windowSize // 2, rows - windowSize // 2):
        for col in range(windowSize // 2, cols - windowSize // 2):
            val = ((img_integral[row+w_size, col+w_size] -
                   img_integral[row+w_size, col-w_size] -
                   img_integral[row-w_size, col+w_size] +
                   img_integral[row-w_size,col-w_size]) / (windowSize*windowSize))
            
            img_blur[row,col] = val
            
    cv2.imshow('img_blur', img_blur)
    

def main():
    img = cv2.imread("a01 - Original.bmp")
    if img is None:
        print(f"Erro ao abrir a imagem")
        sys.exit()
        
    img = img.astype (np.float32) / 255
    
    integral(img, 13)
    
    cv2.imshow('teste', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
    
