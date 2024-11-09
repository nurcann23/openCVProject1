import cv2 as cv
import numpy as np

img = cv.imread("Photos/duman.jpg")
resize_image= cv.resize(img, (int(img.shape[1] * 0.40), int(img.shape[0] * 0.40)), interpolation=cv.INTER_AREA)

cv.imshow("Duman", resize_image)

# Converting to grayscale
gray = cv.cvtColor(resize_image, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
print( gray.shape )

# Blur
blur = cv.GaussianBlur(resize_image, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image 
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("Dilated", dilated)

# Opening the image
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(resize_image, cv.MORPH_CLOSE, kernel)
cv.imshow("Opening", opening)

cv.waitKey(0)