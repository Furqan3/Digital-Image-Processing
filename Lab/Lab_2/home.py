import numpy as np
import cv2 as cv


def borders(size):
    one=np.zeros(size,np.uint8)
    one[int(size[0]/2)-int(size[0]/10):int(size[0]/2)+int(size[1]/10),int(size[1]/2)-int(size[0]/10):int(size[1]/2)+int(size[1]/10)]=255
    return one

def corner(size):
    x=int(size[0]/10)
    y=int(size[1]/10)
    one=np.ones(size,np.uint8)*255
    one[:x,:y]=0    
    one[:x,size[1]-y:]=0    
    one[size[0]-x:,:y]=0    
    one[size[0]-x:,size[1]-y:]=0    
    return one

def grid(size):
    one=np.ones(size,np.uint8)*255
    
    for i in range(int(size[0]/10),size[0],int(size[0]/4)):
       one[i:i+10,:]=0
       one[:,i:i+10]=0

    return one

x=int(input('Enter number of rows:'))
y=int(input('Enter number of colums:'))

cv.imshow('Image With centre white',borders((x,y)))
cv.imshow('Image With Corner',corner((x,y)))
cv.imshow('Image with grid',grid((x,y)))
cv.waitKey()