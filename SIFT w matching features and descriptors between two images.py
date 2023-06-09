import cv2 
import matplotlib.pyplot as plt
from pathlib import PurePath

#img1=input("What is the pathway to the first image? ")
#img2=input("What is the pathway to the second image? ")

#img1=img1.replace("\\","/")
#img2=img2.replace("\\","/")
#img1=img1.replace('"',"'")
#img2=img2.replace('"',"'")

# read images
#print(img1)
#print(img2)
img1 = cv2.imread('C:/Users/jesus/Downloads/Panorama Attempt/2023-06-07-134451.jpg')
img2 = cv2.imread('C:/Users/jesus/Downloads/Panorama Attempt/2023-06-07-134454.jpg')

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp1 = sift.detect(gray1,None)
kp2= sift.detect(gray2,None)
img1=cv2.drawKeypoints(gray1,kp1,img1)
img2=cv2.drawKeypoints(gray2,kp2,img2)
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

#feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:10000], img2, flags=2)
plt.imshow(img3),plt.show()
