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

def main():
    img = cv2.imread("a01 - Original.bmp")
    if img is None:
        print(f"Erro ao abrir a imagem")
        sys.exit()
        
    img = img.astype (np.float32) / 255
    
    ingenuo(img, 13)
    
    cv2.imshow('teste', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
    
