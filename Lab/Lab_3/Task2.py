import cv2 as cv
import numpy as np

def distance(p1,p2,choice):
    if choice==1:
      return int((((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**.5)
    elif choice==2:
      return int(np.abs((p1[0]-p2[0]))+np.abs((p1[1]-p2[1])))
    elif choice==3:
      return int(max(np.abs((p1[0]-p2[0])),np.abs((p1[1]-p2[1]))))
    else:
       print('Error! choice soulb be of (1,2,3)')


image=cv.imread('sample1.png',0)
print(f'Image size is {image.shape}')

p1=[]
p2=[]
p1.append(int(input('Enter the x axis vale of point 1:')))
while p1[-1]<0 or p1[-1]>=image.shape[0]:
   print(f'The Vlue of x is out of the Image borders\n Image x axis range is: {0}-{image.shape[0]-1}')
   p1[-1]=(int(input('Enter the x axis vale of point 1:')))
p1.append(int(input('Enter the y axis vale of point 1:')))
while p1[-1]<0 or p1[-1]>=image.shape[1]:
   print(f'The Vlue of y is out of the Image borders\n Image y axis range is: {0}-{image.shape[1]-1}')
   p1[-1]=(int(input('Enter the y axis vale of point 1:')))
p2.append(int(input('Enter the x axis vale of point 2:')))
while p2[-1]<0 or p2[-1]>=image.shape[0]:
   print(f'The Vlue of x is out of the Image borders\n Image x axis range is: {0}-{image.shape[0]-1}')
   p2[-1]=(int(input('Enter the x axis vale of point 1:')))
p2.append(int(input('Enter the y axis vale of point 2:')))
while p2[-1]<0 or p2[-1]>=image.shape[1]:
   print(f'The Vlue of 1 is out of the Image borders\n Image y axis range is: {0}-{image.shape[1]-1}')
   p2[-1]=(int(input('Enter the y axis vale of point y:')))
choice=int(input('Enter Choice of Method:\n1->Euclidean Distance\n2-> City Block Distance\n3->Chessboard Distance\nSelect:'))
while choice!=1 and choice!=2 and choice!=3:
    choice=int(input('Enter Choice of Method:\n1->Euclidean Distance\n2-> City Block Distance\n3->Chessboard Distance\nSelect:'))
    print('Error!')
mydistance=distance(p1,p2,choice)
image=cv.cvtColor(image, cv.COLOR_GRAY2RGB)
image = cv.line(image, (p1[0],p1[1]), (p2[0],p2[1]), (0,0,255),4)
cv.imshow('line',image)
print(f'Distance for Point A{p1} to Point C{p2} is {mydistance}')
cv.waitKey()