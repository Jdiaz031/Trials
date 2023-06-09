import cv2 as cv
import os

def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            image = cv.imread(os.path.join(folder_path, filename))
            images.append(image)
    return images

def stitch_images(images):
    stitcher = cv.Stitcher_create(cv.Stitcher_SCANS)
    stitcher.setPanoConfidenceThresh(0.6)  # Adjust confidence threshold if needed
    status, stitched_image = stitcher.stitch(images)
    if status == cv.Stitcher_OK:
        return stitched_image
    else:
        return None

folder_path = input("What is the folder pathway? ")
print(folder_path)
images = load_images(folder_path)
stitched_image = stitch_images(images)

if stitched_image is not None:
    cv.namedWindow('Stitched Image', cv.WINDOW_NORMAL)
    cv.imshow('Stitched Image', stitched_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Image stitching failed.")

output_path = input("Enter the output file path: ")
cv.imwrite(output_path, stitched_image)
print("Stitched image saved successfully.")
