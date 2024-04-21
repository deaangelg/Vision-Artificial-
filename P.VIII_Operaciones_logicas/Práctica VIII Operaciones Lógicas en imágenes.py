# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:17:28 2024

@author: Dea

Este script crea dos imágenes, aplica operaciones de bitwise (AND, OR, NOT, XOR) entre ellas
y muestra y guarda las imágenes resultantes.
"""

import cv2 
import numpy as np 

img1=np.zeros((600,600), dtype=np.uint8)
img1[200:400,200:400]=255#creacion de cuadrado en blanco
img2=np.zeros((600,600), dtype=np.uint8)
img2=cv2.circle(img2,(300,300),125,(255),-1)#radio de circulo 125, y con centro en las coordenadas  300,300, relleno de blanco (-1)


# Aplicar operaciones de bitwise entre img1 y img2
AND= cv2.bitwise_and(img1,img2)
OR=cv2.bitwise_or(img1,img2)
NOT=cv2.bitwise_not(img1)
XOR= cv2.bitwise_xor(img1,img2)

# Mostrar y guardar las imágenes resultantes
cv2.imshow("img1",img1)
cv2.imwrite("img1.jpg",img1)

cv2.imshow("img2",img2)
cv2.imwrite("img2.jpg",img2)

cv2.imshow("AND", AND)
cv2.imwrite("AND.jpg",AND)

cv2.imshow("OR",OR)
cv2.imwrite("OR.jpg",OR)

cv2.imshow("NOT",NOT)
cv2.imwrite("NOT.jpg",NOT)

cv2.imshow("XOR",XOR)
cv2.imwrite("XOR.jpg",XOR)


cv2.waitKey(0)
cv2.destroyAllWindows()