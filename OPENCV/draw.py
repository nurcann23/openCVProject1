import cv2 as cv 
import numpy as np

e1 = cv.getTickCount()

# Blank yerine img de seçebiliriz fark etmez.
blank = np.zeros((500,500,3), dtype="uint8") 
# cv.imshow("Blank", blank)


# 1. Paint the image a certain colour
""" blank[200:300, 300:400] = 0,255,0
cv.imshow("Green", blank) """


# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
#cv.imshow("Rectangle", blank)


# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255),thickness=3)
#cv.imshow("Circle", blank)


# 4. Draw a Line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
#cv.imshow("Line", blank)

# 5. Draw a Polygon 
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(blank,[pts],True,(255,0,0))
#cv.imshow("Polygon", blank)


# 6. Write Text
cv.putText(blank, "HEYY", (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow("Text", blank)

e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time)
cv.waitKey(0)

