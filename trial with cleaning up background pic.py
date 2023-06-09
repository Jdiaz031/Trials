import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('C:/Users/jesus/Downloads/Panorama Attempt/2023-06-07-134319.jpg')
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.imread('C:/Users/jesus/Downloads/Panorama Attempt/Background/2023-06-07-134128.jpg')
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

def mse(gray1,gray2):
    h,w=gray1.shape
    diff=cv2.subtract(gray1,gray2)
    err=np.sum(diff**2)
    mse=err/(float(h*w))
    return mse, diff

error, diff=mse(gray1,gray2)
print("Image matching Error between the two images:",error)

for i in diff:
    if diff.all==255:
        diff[i]=0
    else:
        diff[i]=255

newimg=diff
cv2.imshow("Drip",newimg)

#newimg=cv2.cvtColor(newimg,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Drip",newimg)
#plt.imshow(newimg),plt.show()

# Create a background subtractor object using MOG2 algorithm
fgbg = cv2.createBackgroundSubtractorMOG2()


# Apply background subtraction to the current frame
fgmask = fgbg.apply(newimg)
    
# Display the foreground mask
plt.imshow(fgmask),plt.show()
