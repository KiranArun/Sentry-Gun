import cv2
import time
import argparse
#importing the neccessery libraries 

cv2.ocl.setUseOpenCL(False)
#disenabling opencl because it causes an error to do with teh background subtraction

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--min-area", type=int, default=200, help="minimum area")
args = vars(ap.parse_args())
#arguement parser with minimum area for it to pick up as motion

cap = cv2.VideoCapture(0)
#getting the video out from the webcam

fgbg = cv2.createBackgroundSubtractorMOG2()
#getting the background subtractor ready for use

while (1):
    ret, frame = cap.read()
    #starting the loop while  reading from the video capture
    
    fgmask = fgbg.apply(frame)
    #applying the bakground subtractor
    
    thresh = fgmask
    thresh = cv2.GaussianBlur(thresh, (21, 21), 0)
    thresh = cv2.threshold(thresh, 127, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=1)
    #making the image binary and adjusting it for the contouring
    _, cnts, _= cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #find the contours aroung the edges of the motion
    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue
        #putting the contour area through the arguement parser for minimum area
        c = max(cnts, key=cv2.contourArea)

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+ w, y + h), (0, 0, 255), 2)
        #draw the rectangle around the object

    cv2.imshow("Feed", frame)
    #show the image in a new window
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        break
    #break the loop

cap.release()
cv2.destroyAllWindows()
#stop the windows
