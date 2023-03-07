import cv2 as cv
import numpy as np
image=cv.imread('sample.png',0)
image= cv.resize(image,(int(600),int(500)))
cv.imshow('Original Image',image)

image2=np.array(255-image)
cv.imshow('Inverted Image',image2)

c=255/(np.log(1+np.max(image)))
image3=np.array(c*np.log(image+1))
image3=np.array(image3,np.uint8)
cv.imshow('Log Transformation',image3)
cv.waitKey()