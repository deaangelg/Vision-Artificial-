# -*- coding: utf-8 -*-
""
import cv2
import numpy as np

# Aquí leemos la imagen con la que vamos a trabajar
imagen = cv2.imread("pelota.PNG")

# Obtenemos las dimensiones de la imagen
m, n, c = imagen.shape

# Creamos una imagen en blanco y negro y la guardamos como Imagenz
# con las mismas dimensiones pero de un canal (Escala de grises)
imagenb = np.zeros((m, n))
cv2.imwrite("imagenz.jpg", imagenb)
#asignamos color blanco a los colores que cumplen las condiciones
for x in range(m):
    for y in range(n):
       
            #if (77 < imagen[x, y, 0] < 217) and (80 < imagen[x, y, 1] < 209) and (146 < imagen[x, y, 2] < 246):
            #if (46< imagen[x, y, 0] < 134) and (106< imagen[x, y, 1] < 253) and (65 < imagen[x, y, 2] < 140):
           # if (168 < imagen[x, y, 0] < 247) and (168< imagen[x, y, 1] < 245) and (168 < imagen[x, y, 2] < 249):
             #if (130 < imagen[x, y, 0] < 220) and (53< imagen[x, y, 1] < 199) and (31 < imagen[x, y, 2] < 171):
            
                 #if (31 < imagen[x, y, 0] < 178) and (53< imagen[x, y, 1] < 207) and (50 < imagen[x, y, 2] < 240):
            #if (218 < imagen[x, y, 0] < 224) and (17< imagen[x, y, 1] < 229) and (138 < imagen[x, y, 2] < 128):
            #if (218 < imagen[x, y, 0] < 229) and (169< imagen[x, y, 1] < 180) and (140< imagen[x, y, 2] < 159):
            #if (28 < imagen[x, y, 0] < 244) and (9< imagen[x, y, 1] < 234) and (31< imagen[x, y, 2] < 252):
            #if (18 < imagen[x, y, 0] < 244) and (13< imagen[x, y, 1] < 139) and (10< imagen[x, y, 2] < 87):
            if (10 < imagen[x, y, 0] < 87) and (13< imagen[x, y, 1] < 139) and (18< imagen[x, y, 2] < 244):
              
                imagenb[x, y] = 255
                
imagen_final = cv2.resize(imagenb, (400,350))
#Mostramos la imagen clasificada 
cv2.imshow('Clasificada', imagen_final)
cv2.imwrite("clasificada.jpg", imagen_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
