import numpy as np
import cv2 as cv
def createing_rectangle(size=(500,500),pading=10,background_color=(255,255,255),stock_color=0):
    one=np.ones((size),dtype=np.uint8)
    one[:,:]=background_color
    x=size[0]
    y=size[1]
    one[:,:pading]=stock_color
    one[:,y-pading:]=stock_color
    one[:pading,:]=stock_color
    one[x-pading:,:]=stock_color
    cv.imshow('ones',one)
    cv.imwrite('myimage.png',one)
    cv.waitKey()
createing_rectangle((500,500,3),10,(255,255,255),(0,0,0))