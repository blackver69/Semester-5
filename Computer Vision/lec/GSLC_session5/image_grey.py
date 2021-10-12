
from tkinter import *
import cv2
import numpy as np 
import matplotlib.pyplot as plt

img=cv2.imread('image/image4.jpg')

scale_percent=50

h=img.shape[0]
w=img.shape[1]
width=int(w*scale_percent/100)
height=int(h*scale_percent/100)

dim=(width,height)

img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.waitKey(0)

gray_counter=np.zeros(256,dtype=int)

for i in range(height):
    for j in range(width):
        gray_counter[gray[i][j]]+=1

# plt.figure(1)
# plt.plot(gray_counter,'g',label='camera')
# plt.legend(loc='upper right')
# plt.ylabel('quantity')
# plt.xlabel('intensity')
# cv2.imshow("Original",img)
# cv2.imshow("Gray", gray)
# plt.show()


plt.figure(1,(16,8))
plt.subplot(1,2,1)
plt.plot(gray_counter,'g',label='before')
plt.legend(loc='upper right')
plt.ylabel('quantity')
plt.xlabel('intensity')
# plt.show()


img1=cv2.imread('image/image4.jpg',0)
img1=cv2.resize(img1,dim,interpolation=cv2.INTER_AREA)
equ=cv2.equalizeHist(img1)
equ_counter=np.zeros(256,dtype=int)

for i in range(height):
    for j in range(width):
        equ_counter[equ[i][j]]+=1


plt.subplot(1,2,2)
plt.plot(equ_counter,'b',label='After')
plt.legend(loc='upper right')
plt.ylabel('quantity')
plt.xlabel('intensity')
plt.show()


res=np.hstack((gray,equ))
cv2.imshow('Image',res)
cv2.waitKey