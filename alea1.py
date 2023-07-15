# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:32:49 2021

@author: Jorge Gersenowies
"""

import random
import matplotlib.pyplot as plt

import cv2
import imutils



A= ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
#A= ['/content/drive/MyDrive/Colab Notebooks/UNO.jpg','/content/drive/MyDrive/Colab Notebooks/DOS.jpg','/content/drive/MyDrive/Colab Notebooks/TRES.jpg','/content/drive/MyDrive/Colab Notebooks/CUATRO.jpg','/content/drive/MyDrive/Colab Notebooks/CINCO.jpg']

random.shuffle(A)

imagen1=cv2.imread(A[0])
imagen2=cv2.imread(A[1])
imagen3=cv2.imread(A[2])
imagen4=cv2.imread(A[3])
imagen5=cv2.imread(A[4])

imagen1 = imutils.resize(imagen1, height=300)
imagen2 = imutils.resize(imagen2, height=300)
imagen3 = imutils.resize(imagen3, height=300)
imagen4 = imutils.resize(imagen4, height=300)
imagen5 = imutils.resize(imagen5, height=300)


concaten01 = cv2.hconcat([imagen1,imagen2,imagen3,imagen4,imagen5])


cv2.imshow('concaten', concaten01)
cv2.waitKey(0)
cv2.destroyAllWindows()

