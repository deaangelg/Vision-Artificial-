# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:16:32 2024

@author: Dea

Práctica V11: Transformaciones Básicas de Imágenes con OpenCV

Este script carga una imagen, aplica diferentes transformaciones como traslación,
rotación, escalado y recorte, y muestra y guarda las imágenes transformadas.
"""

import cv2
import numpy as np
 
image = cv2.imread ('ternurin.PNG')


ancho = image.shape[1] #columnas
alto = image.shape[0] # filas
######## Traslación
M = np.float32([[1,0,100],[0,1,100]])# Definir la matriz de traslación, traslado 100 en X y 100 en y 
imageOut_traslacion = cv2.warpAffine(image,M,(ancho,alto)) # Aplicar traslación a la imagen
######## Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),180,1) #Rotacion de 180 grados
imageOut_rotacion = cv2.warpAffine(image,M,(ancho,alto))
########  Escalando una imagen
imageOut_escala = cv2.resize(image,(350,225), interpolation=cv2.INTER_CUBIC) 
######## Recortar una imagen
imageOut_recorte = image[100:354,140:476]

         
cv2.imshow('Original',image)     
cv2.imshow('Traslacion',imageOut_traslacion)
cv2.imshow('Rotacion',imageOut_rotacion)
cv2.imshow('Escala',imageOut_escala)
cv2.imshow('Recorte',imageOut_recorte)

cv2.imwrite("Traslacion.jpg", imageOut_traslacion)
cv2.imwrite("Rotacion.jpg", imageOut_rotacion)
cv2.imwrite("Escala.jpg", imageOut_escala)
cv2.imwrite("Recorte.jpg", imageOut_recorte)
cv2.waitKey(0)
cv2.destroyAllWindows()