import cv2 as cv

# DOĞRU ÇALIŞMIYO

img = cv.imread("Photos/messi.jpg")
cv.imshow("Messi", img)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow("Messi2", img)


cv.waitKey(0)

