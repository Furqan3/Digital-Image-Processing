import cv2 as cv
import numpy as np

image=cv.imread('sample3.png',0)

print(image.dtype)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j]>255:
            print(image[i][j])