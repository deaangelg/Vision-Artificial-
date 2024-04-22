# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 00:00:48 2024

@author: Dea

Este script detecta los bordes de una imagen utilizando el algortimo Canny, donde utiliza la intensidad de gradiente del borde para detectarlos. 
"""


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('Cohete.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
# Detección de bordes utilizando el algoritmo Canny
edges = cv.Canny(img,80,150) #los bordes con intensidad de gradiente entre 100 y 200 seran bordes aceptados y mostrados, fuera de seran rechazados. 
 
# Mostrar la imagen original y la imagen de bordes
plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Imagen Original')
plt.xticks([])
plt.yticks([])


plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Detección de bordes')
plt.xticks([])
plt.yticks([])
 
plt.show()
