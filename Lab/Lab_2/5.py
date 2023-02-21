import numpy as np
import cv2 as cv
def flipp(image):
    for i in range(0, image.shape[0]):
        image[-i,:],image[i,:]=image[i,:],image[-i,:]
    return image
image=cv.imread('sample.png',0)
cv.imshow('original',image)
cv.waitKey()
flipimg=flipp(image)
cv.imshow('img',flipimg)
cv.waitKey()