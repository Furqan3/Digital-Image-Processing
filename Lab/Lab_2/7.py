import numpy as np
import cv2 as cv

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
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]-1):
            one[i*4][j*4]=image[i][j]
            a=image[i][j+1]
            b=image[i][j]
            x=int((a+b)/2)
            one[(i*4)+3][(j*4)+3]=a
            one[(i*4)+2][(j*4)+2]=x
            one[(i*4)+1][(j*4)+1]=b
    return one

image=cv.imread('sample.png',0)
cv.imshow('Original',image)
image2=resize(image)
cv.imshow('Small Size',image2)
image3=increase(image2)
cv.imshow('Large Size',image3)
cv.waitKey()