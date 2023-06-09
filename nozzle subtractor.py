import cv2

# Load the images
image_nozzle_part = cv2.imread("C:/Users/jesus/Downloads/Panorama Attempt/2023-06-07-134454.jpg")
image_nozzle_alone = cv2.imread("C:/Users/jesus/Downloads/Background/2023-06-07-134210.jpg")

# Align the two images
# Your code for alignment using feature matching and transformation matrix

# Subtract the image with the nozzle alone from the image with the nozzle and the part
subtracted_image = cv2.subtract(image_nozzle_part, image_nozzle_alone)

# Save or further process the subtracted image
cv2.imwrite('subtracted_image.jpg', subtracted_image)
