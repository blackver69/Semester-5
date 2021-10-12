import cv2

img=cv2.imread('logo.jpg')#load image

img[1:150,1:100]=[150,150,150]  #modif BGR values
img[1:150,100:200]=[0,0,0] #modif BGR values
img[1:150,200:300]=[255,255,255] #modif BGR values

img[150:,1:300,2]=0 #modif R values
img[1:550,300:650,1]=0 #modif G values
img[150:,650:,0]=0 #modif B values

cv2.imshow('logo',img) #show image
cv2.waitKey(0)