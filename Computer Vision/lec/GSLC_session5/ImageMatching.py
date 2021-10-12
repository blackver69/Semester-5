from textwrap import indent
import cv2
import numpy as np
import glob
img1=cv2.imread("image/image9.jpg")
img2=cv2.imread("choose/image9.jpg")

if(img1.shape==img2.shape):
    print("similar")
    diff=cv2.subtract(img1,img2)

    b,g,r=cv2.split(diff)

    if(cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0):
        print("equal")
    else:
        print("not equal")

sift=cv2.xfeatures2d.SIFT_create()
kp_1, desc_1= sift.detectAndCompute(img1,None)
kp_2, desc_2= sift.detectAndCompute(img2,None)

print("kp1 : {}\n".format(len(kp_1)))
print("kp2 : {}\n".format(len(kp_2)))

index_params=dict(algorithm=0,trees=5)
search_param=dict()
flann=cv2.FlannBasedMatcher(index_params,search_param)
matches=flann.knnMatch(desc_1,desc_2,k=2)
good_point=[]

for m,n in matches:
    if(m.distance<0.6*n.distance):
        good_point.append(m)

num_keypoints=0

if(len(kp_1)<=len(kp_2)):
    num_keypoints=len(kp_1)
else:
    num_keypoints=len(kp_2)

print("good matches :{}".format(good_point))

print("Percentase :{}".format(len(good_point)/num_keypoints*100))
result=cv2.drawMatches(img1,kp_1,img2,kp_2,good_point,None)
cv2.imshow("result",cv2.resize(result,None,fx=0.4,fy=0.4))
cv2.imwrite("feature_matching.jpg",result)


cv2.imshow("image1",cv2.resize(img1,None,fx=0.4,fy=0.4))
cv2.imshow("image2",cv2.resize(img2,None,fx=0.4,fy=0.4))

cv2.waitKey(0)
cv2.destroyAllWindows()