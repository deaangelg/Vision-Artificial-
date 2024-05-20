# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""


@author: Dea Angel
"""

import cv2
import numpy as np

imagen=cv2.imread("mano.PNG")

# Aumentar el brillo en los canales de color para generar variantes de la imagen
imagenb1=imagen.copy()
imagenb1[:,:,0]=imagen[:,:,0]+100

imagenb2=imagen.copy()
imagenb2[:,:,1]=imagen[:,:,1]+100

imagenb3=imagen.copy()
imagenb3[:,:,2]=imagen[:,:,2]+100

# Cálculo de los valores máximos y promedios de los canales de color
B=np.max(imagen[:,:,0]) #azul
G=np.max(imagen[:,:,1]) #verde
R=np.max(imagen[:,:,2]) #rojo


b=np.mean(imagen[:,:,0])
g=np.mean(imagen[:,:,1])
r=np.mean(imagen[:,:,2])


def whitepatch(imagenW):
      m,n,c = imagen.shape
      imagenW = imagenW.astype(np.float64)
      for x in range (m):
          for y in range (n):
              
              imagenW[x,y,0]=((imagen[x,y,0]))*(255/(B*(r+g+b)))
              imagenW[x,y,1]=((imagen[x,y,1]))*(255/(G*(r+g+b)))
              imagenW[x,y,2]=((imagen[x,y,2]))*(255/(R*(r+g+b)))
             
      result = cv2.normalize(imagenW, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
      cv2.imwrite("WhiteP.jpg",imagenW)
      cv2.imwrite("WhiteN.jpg", result)
      return result


# Clasificación de píxeles original (antes de aplicar White Patch)
def clasificadorOr(imagen):
    m,n,c=imagen.shape
    imagenb=np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            
                if 9<imagen[x,y,2]<223 and 17<imagen[x,y,1]<214 and 31<imagen[x,y,0]<240:
                    imagenb[x,y]=255
    return imagenb

# Clasificación de píxeles después de aplicar White Patch
def White_cla(imagen):
    m,n,c=imagen.shape
    imagenc=np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            
            if (10 < imagen[x, y, 0] < 170) and (23< imagen[x, y, 1] < 196) and (23 < imagen[x, y, 2] < 230):
                imagenc[x,y]=255
               
    return imagenc   
Bc=np.max(imagen[:,:,0])
Gc=np.max(imagen[:,:,1])
Rc=np.max(imagen[:,:,2])
print("Valor max del canal azul (B):", Bc)
print("Valor max  del canal verde (G):", Gc)
print("Valor max del canal rojo (R):", Rc)  
bc=np.min(imagen[:,:,0])
gc=np.min(imagen[:,:,1])
rc=np.min(imagen[:,:,2])
print("Valor min del canal azul (B):", bc)
print("Valor min  del canal verde (G):", gc)
print("Valor min del canal rojo (R):", rc)         

# Concatenación de imágenes para su visualización
imFinal = np.hstack((imagen,imagenb1,imagenb2,imagenb3))
result1 = cv2.normalize(imFinal, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
originales = cv2.resize(result1, (600, 200))
cv2.imwrite("Cambio de canal Original.jpg", originales)


imagenCla1 = clasificadorOr(imagen)
imagenCla2 = clasificadorOr(imagenb1)
imagenCla3 = clasificadorOr(imagenb2)
imagenCla4 = clasificadorOr(imagenb3)
    
imFinal2 = np.hstack((imagenCla1,imagenCla2,imagenCla3,imagenCla4))
result2 = cv2.normalize(imFinal2, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
clasificada_original = cv2.resize(result2, (600, 200))
cv2.imwrite("Clasificador Original.jpg", clasificada_original)


imWhite1 = whitepatch(imagen)
imWhite2 = whitepatch(imagenb1) #azul
imWhite3 = whitepatch(imagenb2) #verde
imWhite4 = whitepatch(imagenb3) #rojo

imFinal3 = np.hstack((imWhite1,imWhite2,imWhite3,imWhite4))
result3 = cv2.normalize(imFinal3, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
whitepatch_original = cv2.resize(result3, (600, 200))
cv2.imwrite("Whitepatch.jpg", whitepatch_original)

imClaWhi1 = White_cla(imWhite1)
imClaWhi2 = White_cla(imWhite2)
imClaWhi3 = White_cla(imWhite3)
imClaWhi4 = White_cla(imWhite4)

imFinal4 = np.hstack((imClaWhi1, imClaWhi2, imClaWhi3, imClaWhi4))
result4 = cv2.normalize(imFinal4, dst=None, alpha=0, beta=255,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
White_cla = cv2.resize(result4, (600, 200))
cv2.imwrite("Clasificador adapatado.jpg", White_cla)
    
cv2.imshow("original", originales)
cv2.imshow("imagen clasificada", clasificada_original)
cv2.imshow("imagen whitepatch",whitepatch_original)
cv2.imshow("WhitePatch clasificado",White_cla)
cv2.waitKey(0)
cv2.destroyAllWindows()
