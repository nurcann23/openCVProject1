import cv2
import numpy as np


    
image = cv2.imread('Photos/karekod.png')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create SIFT Feature Detector object
sift = cv2.SIFT_create()

# Detect key points
keypoints = sift.detect(gray, None)
print("Number of keypoints Detected: ", len(keypoints))

# Draw rich key points on input image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - SIFT', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
