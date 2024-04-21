# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:33:53 2024
Este script aplica detección de bordes horizontales y verticales a una imagen en escala de grises.
@author: Dea
"""

import cv2
import numpy as np


imagen = cv2.imread("patron.jpg", 0)
imagen1 = cv2.resize(imagen, (500, 500))
kernel_horizontal = np.array([[1, 1, 1],[0, 0, 0],[-1, -1, -1]])
kernel_vertical = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
m, n = imagen1.shape

# Imágenes filtradas para bordes horizontales y verticales
filtrada_horizontal = np.zeros_like(imagen1)
filtrada_vertical = np.zeros_like(imagen1)

# Aplicar los kernels para detectar bordes horizontales y verticales
for x in range(m-2):
    for y in range(n-2):
        res_horizontal = np.sum(imagen1[x:x+3, y:y+3] * kernel_horizontal)
        res_vertical = np.sum(imagen1[x:x+3, y:y+3] * kernel_vertical)
        
        if abs(res_horizontal) > 70: #umbral de deteccion, se puede modificar este valor para obtener mejor deteccion del los bordes
            filtrada_horizontal[x, y] = 255
        if abs(res_vertical) > 100:
            filtrada_vertical[x, y] = 255

combinada = cv2.bitwise_or(filtrada_horizontal, filtrada_vertical)


cv2.imshow("patron", imagen1)
cv2.imshow("Bordes Horizontales", filtrada_horizontal)
cv2.imwrite("Bordes horizontales.jpg",filtrada_horizontal)

cv2.imshow("Bordes Verticales", filtrada_vertical)
cv2.imwrite("Bordes verticales.jpg", filtrada_vertical)

cv2.imshow("Detecciond de bordes", combinada)
cv2.imwrite("Deteccion de bordes.jpg", combinada)



cv2.waitKey()
cv2.destroyAllWindows()


#Tarea: calcular gradiente Gy mostrar bordes horizontales)

#kernel de promedio #Algoritmo Canny 
