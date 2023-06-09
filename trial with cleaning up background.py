import cv2
cap = cv2.VideoCapture(0) # Read video stream from default camera

# Create a background subtractor object using MOG2 algorithm
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Apply background subtraction to the current frame
    fgmask = fgbg.apply(frame)
    
    # Display the foreground mask
    cv2.imshow('Foreground Mask', fgmask)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video stream and destroy all windows
cap.release()
cv2.destroyAllWindows()
