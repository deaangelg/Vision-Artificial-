# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:37:48 2024

@author: Dea

Este script aplica ruido gaussiano y ruido sal y pimienta a una imagen original. Despues aplica varios filtros de procesamiento de imágenes, incluyendo el filtro gaussiano, de media, mediana, mínimo y máximo, para mejorar la calidad de la imagen o reducir el ruido. Como resultado, genera un total de 12 imágenes: 2 imágenes con ruido y 10 imágenes que muestran el efecto de los filtros aplicados a una de las imágenes con ruido.

"""


import cv2
import numpy as np

img_original= cv2.imread("snoopy.jpg")
imagen = cv2.resize(img_original,(280,210))
img_Gauss = cv2.GaussianBlur(imagen, (17,17), 0)

def sal_pimienta(imagen, prob):
    img_sp = imagen.copy()
    
    sal = np.ceil(prob * imagen.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(sal)) for i in imagen.shape]
    img_sp[tuple(coords)] = 255

    pimienta = np.ceil(prob * imagen.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(pimienta)) for i in imagen.shape]
    img_sp[tuple(coords)] = 0
    
    return img_sp

img_salpimienta = sal_pimienta(imagen, 0.3)
#-----------------------------------------------------


#Filtro de Gauss aplicado a imagenes con ruido 
filtro_gauss1=cv2.GaussianBlur(img_Gauss,(15,15),0)
filtro_gauss2=cv2.GaussianBlur(img_salpimienta,(15,15),0)

#Filtro de media aplicado a imagenes con ruido 
kernel = np.ones((3,3),np.float32)/9
media1 = cv2.filter2D(img_Gauss,-1,kernel)
media2 = cv2.filter2D(img_salpimienta,-1,kernel)

#Filtro de mediana aplicado a imagenes con ruido
mediana1 = cv2.medianBlur(img_Gauss, 3)
mediana2 = cv2.medianBlur(img_salpimienta,3)

#Filtro de minimo aplicado a imagenes con ruido 
kernel2 = np.ones((3,3),np.uint8)
minimo1 = cv2.erode(img_Gauss, kernel2)
minimo2 = cv2.erode(img_salpimienta, kernel2)

#Filtro de maximo aplicado a imagenes con ruido 
kernel = np.ones((3,3),np.uint8)
maximo1 = cv2.dilate(img_Gauss, kernel)
maximo2 = cv2.dilate(img_salpimienta, kernel)


Filtros_Gauss = np.hstack((filtro_gauss1,media1,mediana1,minimo1,maximo1))
Filtros_salpimienta = np.hstack((filtro_gauss2,media2,mediana2,minimo2,maximo2))


cv2.imwrite("Ruido Gauss.jpg", img_Gauss)
cv2.imshow("Ruido Gauss",img_Gauss)
cv2.imwrite("Ruido Sal y Pimienta.jpg", img_salpimienta)
cv2.imshow("Ruido sal y pimienta",img_salpimienta)

cv2.imshow("Filtros (Gauss)",Filtros_Gauss)
cv2.imshow("Filtros (Sal y Pimienta )",Filtros_salpimienta)
cv2.imwrite("Filtros (Ruido Gaussioano).jpg",Filtros_Gauss)
cv2.imwrite("Filtros (Sal y Pimienta).jpg", Filtros_salpimienta)


cv2.waitKey(0)
cv2.destroyAllWindows()