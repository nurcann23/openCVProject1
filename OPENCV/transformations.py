import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
resized_imaged = cv.resize(img, (298, 295))

cv.imshow("Cat", resized_imaged)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(resized_imaged, 100, 100)
cv.imshow("Translated", translated)


# Rotation
def rotate(img,angle,rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)


cv.waitKey(0)