import cv2 as cv
import numpy as np
import copy

image=cv.imread('sample.png',0)
image= cv.resize(image,(int(600),int(500)))
cv.imshow('Original Image',image)
image1=copy.copy(image)
image2=copy.copy(image)
image3=copy.copy(image)
mean=np.mean(image)
image1[image>mean]=255
image1[image<mean]=0
cv.imshow('1',image1)

image2[image>mean]=0
image2[image<mean]=255
cv.imshow('2',image2)

for i in range(500):
    for j in range(600):
        if image[i][j]>(mean-20) and image[i][j]<(mean+20):
            image3[i][j]=0
        else:
            image3[i][j]=255

cv.imshow('3',image3)
cv.waitKey()