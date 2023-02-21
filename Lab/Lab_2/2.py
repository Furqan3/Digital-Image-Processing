import numpy as np
import cv2 as cv
def decrease_intesity(image,level):

    if level==4:
        for i in range(image.shape[0]):
         for j in range(image.shape[1]):
             if image[i][j]>=0 and image[i][j]<64:
                 image[i][j]=0
             elif image[i][j]>=64 and image[i][j]<128:
                 image[i][j]=85
             elif image[i][j]>=128 and image[i][j]<192:
                 image[i][j]=170
             else:
                 image[i][j]=255
    elif level==8:
        for i in range(image.shape[0]):
         for j in range(image.shape[1]):
             if image[i][j]>=0 and image[i][j]<32:
                 image[i][j]=0
             elif image[i][j]>=32 and image[i][j]<64:
                 image[i][j]=36
             elif image[i][j]>=64 and image[i][j]<64:
                 image[i][j]=72
             elif image[i][j]>=64 and image[i][j]<96:
                 image[i][j]=108
             elif image[i][j]>=96 and image[i][j]<128:
                 image[i][j]=144
             elif image[i][j]>=128 and image[i][j]<160:
                 image[i][j]=180
             elif image[i][j]>=160 and image[i][j]<192:
                 image[i][j]=216
             else:
                 image[i][j]=255
    elif level==16:
        for i in range(image.shape[0]):
         for j in range(image.shape[1]):
             if image[i][j]>=0 and image[i][j]<16:
                 image[i][j]=0
             elif image[i][j]>=16 and image[i][j]<32:
                 image[i][j]=24
             elif image[i][j]>=32 and image[i][j]<48:
                 image[i][j]=40
             elif image[i][j]>=48 and image[i][j]<64:
                 image[i][j]=56
             elif image[i][j]>=64 and image[i][j]<80:
                 image[i][j]=72
             elif image[i][j]>=80 and image[i][j]<96:
                 image[i][j]=88
             elif image[i][j]>=96 and image[i][j]<112:
                 image[i][j]=104
             elif image[i][j]>=112 and image[i][j]<128:
                 image[i][j]=120
             elif image[i][j]>=128 and image[i][j]<144:
                 image[i][j]=136
             elif image[i][j]>=144 and image[i][j]<160:
                 image[i][j]=152
             elif image[i][j]>=160 and image[i][j]<176:
                 image[i][j]=168
             elif image[i][j]>=176 and image[i][j]<192:
                 image[i][j]=184
             elif image[i][j]>=192 and image[i][j]<208:
                 image[i][j]=200
             elif image[i][j]>=208 and image[i][j]<224:
                 image[i][j]=216
             else:
                 image[i][j]=255
    elif level==2:
        for i in range(image.shape[0]):
         for j in range(image.shape[1]):
             if image[i][j]>=0 and image[i][j]<128:
                 image[i][j]=0
            
             else:
                 image[i][j]=255
    else:
        print('Errir! Bits should be onle(2,4,8,16)')
    return image
image=cv.imread('gradient.png',0 )
x=int(input('Enter bits(2,4,8,16)'))
cv.imshow('Original',image)
image2=decrease_intesity(image,x)    
cv.imshow('img',image2)
cv.waitKey()