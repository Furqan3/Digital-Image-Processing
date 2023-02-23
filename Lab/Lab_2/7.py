import numpy as np
import cv2 as cv
import time as sec

def resize(image):
    x=int(image.shape[0]/4)
    y=int(image.shape[1]/4)
    one=np.ones((x,y),np.uint8)
    for i in range(0,image.shape[0],4):
        for j in range(0,image.shape[1],4):
            one[int(i/4)][int(j/4)]=int(image[i][j])
    return one

def increase(image):
    x=int(image.shape[0]*4)
    y=int(image.shape[1]*4)
    one=np.ones((x,y),np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            one[4*i:4*(i+1), 4*j:4*(j+1)] = image[i, j]
           
    return one

image=cv.imread('sample.png',0)
cv.imshow('Original',image)
image2=resize(image)
cv.imshow('Small Size',image2)
image3=increase(image2)
cv.imshow('Large Size',image3)
cv.waitKey()

