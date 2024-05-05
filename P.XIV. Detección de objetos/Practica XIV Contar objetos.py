# -*- coding: utf-8 -*-
"""
Created on Fri May  3 19:05:22 2024
Este script captura video: 
  *Convierte los frames a escala de grises. 
  *Aplica un filtro Gaussiano para reducir el ruido. 
  *Detecta los bordes en la imagen utilizando el algoritmo de Canny. 
  *Encuentra los contornos de los objetos en la imagen y muestra el número de objetos encontrados en cada frame en tiempo real.
@author: Dea
"""

import numpy as np
import cv2

# Inicializa la cámara web
cap = cv2.VideoCapture('http://192.168.XXX.XXXX:XXXX/video')
##fourcc = cv2.VideoWriter_fourcc(*'X264')  
##out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    gauss = cv2.GaussianBlur(gris, (15,15), 2)
    canny = cv2.Canny(gauss, 15, 170)

    
    contornos, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contornos, -1, (73,18,177), 2)


    texto = "He encontrado {} objetos".format(len(contornos))
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

   
    cv2.imshow("Contornos", frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
