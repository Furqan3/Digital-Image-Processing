import cv2 as cv
import numpy as np
import copy

def gama(image,g):
    image=np.divide(image,255)
    gimage=255*(np.power(image,g))
    return np.array(gimage,np.uint8)


image=cv.imread('sample.png',0)
image= cv.resize(image,(int(600),int(500)))
cv.imshow('Original Image',image)
cv.imshow('0.2 gama Image',gama(image,.2))
cv.imshow('0.5 gama Image',gama(image,.5))
cv.imshow('1.2 gama Image',gama(image,1.2))
cv.imshow('1.8 gama Image',gama(image,1.8))
cv.waitKey()