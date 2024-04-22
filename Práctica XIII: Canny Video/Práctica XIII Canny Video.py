# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:07:06 2024

@author: Usuario
Script para capturar video desde una cámara, aplicar el filtro Canny
y mostrar el resultado en tiempo real. Presione 'q' para salir.

"""

import cv2
cap=cv2.VideoCapture(0)
 
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit() 
    
while True:
    f,frame=cap.read()
    frame=cv2.Canny(frame,50,100)
    if f==True:
        cv2.imshow("Canny",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()