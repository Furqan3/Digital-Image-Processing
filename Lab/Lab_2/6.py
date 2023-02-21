import numpy as np
import cv2 as cv

def distance_map(image,formula):
    centre=[int(image.shape[0]/2)+1,int(image.shape[1]/2)+1]
    if formula=='Euclidian_Distance':
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
               image[i][j]=((centre[0]-i)**2+(centre[1]-j)**2)**.5
               if ((centre[0]-i)**2+(centre[1]-j)**2)**.5>255:
                   image[i][j]=255
    
    elif formula=='City_Distance':
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
               image[i][j]=np.abs((centre[0]-i))+np.abs((centre[1]-j))
               if np.abs((centre[0]-i))+np.abs((centre[1]-j))>255:
                   image[i][j]=255

    elif formula=='Chessboard_Distance':
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if np.abs((centre[0]-i))>np.abs((centre[1]-j)):
                    image[i][j]=np.abs((centre[0]-i))
                    if np.abs((centre[0]-i))>255:
                        image[i][j]=255 
                else:
                    image[i][j]=np.abs((centre[1]-j))
                    if np.abs((centre[1]-j))>255:
                        image[i][j]=255 
    else:
        print('Error! You are allowed to select the given choices!')
        return None
    cv.imshow('image',image)
    cv.waitKey()
choice=input('Enter Your choice(Chessboard_Distance,City_Distance,Euclidian_Distance):')
x=int(input('Enter Number of rows:'))
y=int(input('Enter Number of column:'))
image=np.zeros((x,y),np.uint8)
distance_map(image,choice)