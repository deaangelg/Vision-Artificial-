# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:59:16 2024
@author: Dea
Este script aplica diferentes filtros (Prewitt, Sobel, Roberts) de detección de bordes a una imagen en escala de grises y muestra los resultados.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage 

img = cv2.imread('original1.jpg', cv2.IMREAD_GRAYSCALE)

# Filtro Prewitt
# Definir los kernels para la detección de bordes horizontal y vertical
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
# Aplicar los filtros de convolución horizontal y vertical
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)

# Filtro Sobel
# Aplicar el filtro Sobel en dirección x e y para detectar bordes
img_sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
img_sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
img_sobel = img_sobelx + img_sobely

# Filtro Roberts
# Definir los kernels para la detección de bordes con el filtro Roberts
roberts_cross_v = np.array([[1, 0],[0, -1]])
roberts_cross_h = np.array([[0, 1],[-1, 0]])


img2 = cv2.imread('original1.jpg',0).astype('float64') 

img2 /= 255.0
vertical = ndimage.convolve(img2, roberts_cross_v)
horizontal = ndimage.convolve(img2, roberts_cross_h)
edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
edged_img *= 255

plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 4, 2)
plt.imshow(img_prewittx, cmap='gray')
plt.title('Filtro Prewitt')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 4, 3)
plt.imshow(img_sobel, cmap='gray')
plt.title('Filtro Sobel')
plt.xticks([])
plt.yticks([])
plt.subplot(1, 4, 4)
plt.imshow(edged_img, cmap='gray')
plt.title('Filtro Roberts')
plt.xticks([])
plt.yticks([])

plt.show()

