import cv2 as cv

def rescaleFrame(frame, scale=0.45):
    # works for Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # works for Live Video
    # 3 references width, 4 references height
    capture.set(3,width) 
    capture.set(4,height)


# Reading Images

img = cv.imread("Photos/cat.jpg")
resize_image= rescaleFrame(img)

px = resize_image[100:300,100:200]
resize_image[100:300,100:200] = [255,0,0]
print( resize_image.shape )


cv.imshow("Cat", img)
cv.imshow("Resized Cat", resize_image)
cv.waitKey(0)
# Reading Videos
 
capture = cv.VideoCapture("Videos/cat_video.mp4")

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows