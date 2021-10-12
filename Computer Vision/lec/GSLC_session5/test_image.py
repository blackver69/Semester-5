import cv2
import numpy as np 
img=cv2.imread("image/image4.jpg",0)
scale_percent=90

width=int(img.shape[1]*scale_percent/100)
height=int(img.shape[0]*scale_percent/100)

dim=(width,height)

img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
equ=cv2.equalizeHist(img)

res=np.hstack((img,equ))
cv2.cv2.imshow('image',res)

cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()
