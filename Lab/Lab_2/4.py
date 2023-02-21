import numpy as np
import cv2 as cv
def flipp(image):
    one=np.ones((image.shape[0],image.shape[1]),dtype=np.uint8)
    for i in range(1, image.shape[0]):
        for j in range(1,image.shape[1]):
            one[i][j]=image[-i][-j]
    cv.imshow('img',one)
    return one
def flippx(image):
    one=np.ones((image.shape[0],image.shape[1]),dtype=np.uint8)
    for i in range(1, image.shape[0]):
        for j in range(1,image.shape[1]):
            one[i][j]=image[i][-j]
    cv.imshow('Flip Hirizentaly',one)
def flippy(image):
    one=np.ones((image.shape[0],image.shape[1]),dtype=np.uint8)
    for i in range(1, image.shape[0]):
        for j in range(1,image.shape[1]):
            one[i][j]=image[-i][-j]
    cv.imshow('Flip Virtically and horaizentaly',one)
image=cv.imread('sample.png',0)
def flippz(image):
    one=np.ones((image.shape[0],image.shape[1]),dtype=np.uint8)
    for i in range(1, image.shape[0]):
        for j in range(1,image.shape[1]):
            one[i][j]=image[-i][j]
    cv.imshow('Flip Virtically',one)
image=cv.imread('sample.png',0)
cv.imshow('original',image)
flippx(image)
flippy(image)
flippz(image)
cv.waitKey()