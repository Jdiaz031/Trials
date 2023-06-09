import cv2 as cv
import os
import matplotlib.pyplot as plt
from pathlib import PurePath
sift=cv.SIFT_create()
bf=cv.BFMatcher(cv.NORM_L1, crossCheck=True)
matches=str()

def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            print("Loading images...")
            image = cv.imread(os.path.join(folder_path, filename))
            images.append(image)
    print("All images were loaded. There were "+str(len(images))+" images.")
    return images
def gray_kp_conversion(images):
    grays=[]
    kps=[]
    for i in images:
        print("Converting to gray image...")
        gray=cv.cvtColor(i,cv.COLOR_BGR2GRAY)
        grays.append(gray)
        print("Converted to gray image. Now calculating keypoints...")
        kp=sift.detect(gray,None)
        kps.append(kp)
    print("Keypoints calculated and Images Converted to Gray.")
    return grays,kps

def drawkp(grays,kps,images):
    addalls=[]
    for gray,kp,image in zip(grays,kps,images):
        print("Drawing keypoints...")
        addall0=cv.drawKeypoints(gray,kp,image)
        addalls.append(addall0)
    print("All keypoints drawn.")
    return addalls

def kpanddect(addalls):
    kp1=[]
    dects=[]
    for i in addalls:
        print("Detecting and Computing Keypoints and Descriptors...")
        kp2,dect=sift.detectAndCompute(i,None)
        kp1.append(kp2)
        dects.append(dect)
    print("All Keypoints and Descriptors were Detected and Computed.")
    return kp1,dects

def matching(dects):
    matches=[]
    for dect in dects:
        print("Detecting Matches...")
        match=bf.match(dect,dect)
        matches.extend(match)
    assorted=sorted(matches,key=lambda x:x.distance)
    print("Matches are completed.")
    return assorted


folder_path = input("What is the folder pathway? ")
images=load_images(folder_path)
grays,kps=gray_kp_conversion(images)
addalls=drawkp(grays,kps,images)
kpl,dects=kpanddect(addalls)
assorted=matching(dects)
