import numpy as np
import cv2 as cv
def createing_rectangle(size=(500,500),pading=10,background_color=(255,255,255)):
    one=np.ones((size),dtype=np.uint8)
    one[:,:]=background_color
    x=size[0]
    y=size[1]
    one[:pading,:pading]=(0,0,255)
    one[:pading,y-pading:]=(0,255,0)
    one[x-pading:,:pading]=(255,0,0)
    one[x-pading:,y-pading:]=(0,0,0)
    cv.imshow('ones',one)
    cv.imwrite('myimage.png',one)
    cv.waitKey()
createing_rectangle((500,500,3),50,(255,255,255))