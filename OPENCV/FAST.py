import cv2
import numpy as np


image = cv2.imread('Photos/karekod.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Create FAST Detector object
fast = cv2.FastFeatureDetector_create()

# Obtain Key points, by default non max suppression is On
keypoints = fast.detect(gray, None)
print("Number of keypoints Detected: ", len(keypoints))

# Draw rich keypoints on input image
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - FAST', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
