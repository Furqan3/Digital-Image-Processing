import cv2 as cv
import numpy as np
import copy
import matplotlib.pyplot as plt

image=cv.imread('sample.png',0)
image= cv.resize(image,(int(600),int(500)))
# image=[[0, 1, 5],[0,2,3],[3,1,2]]
#print(image)
histogram=np.array(range(0,256),np.uint32)*0
# image=np.array(image,np.uint8)
#co#unter = 0
#print(image.shape[0])
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        histogram[image[i][j]]=histogram[image[i][j]]+1
 #       counter = counter +1
#print(histogram)
#print(counter)
x=np.array(range(0,256),np.uint8)
#histogram=np.array(histogram,np.uint8)
print(np.sum(histogram),' ',image.shape,' ',np.size(image))

plt.plot(x,histogram)
plt.show()
