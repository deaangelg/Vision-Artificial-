# -*- coding: utf-8 -*-
"""
Este script procesa una imagen para: 
Escanea en al imagen el template para detectar en la imagen y luego dibuja en la imagen completa un rectangulo en los template que detecte. En este caso son varios. 
    
Vision artificial Marzo 2024 
Primer parcial Practica II 

@author: Dea Angel
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('Mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Moneda.jpg",0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    
templateMatching= cv2.resize(img_rgb, (400, 200))
cv2.imwrite('Template matching.png',img_rgb)

plt.imshow(cv2.cvtColor(templateMatching, cv2.COLOR_BGR2RGB))
plt.title('Template Matching')
plt.axis('off') 
plt.show()
#cv2.imshow("Template matching",templateMatching)