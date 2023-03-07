import cv2 as cv
import numpy as np
import copy

image=cv.imread('sample.png',0)
image= cv.resize(image,(int(600),int(500)))
cv.imshow('Original Image',image)
image2=copy.copy(image)
for i in range(500):
    for j in range(600):
        if image[i][j]>100 and image[i][j]<200:
            image2[i][j]=210
cv.imshow('Sliced  Image',image2)
cv.waitKey()