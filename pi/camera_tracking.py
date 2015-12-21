import numpy as np
import cv2
# importing openCV.
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--min-area", type=int, default=100, help="minimum area")
args = vars(ap.parse_args())
# making an arguement for the minimun size of object it has found.

cap = cv2.VideoCapture(0)
# cap now equals the function to get the capture from the camera.

time.sleep(2)

fgbg = cv2.BackgroundSubtractorMOG()
# fgbg now equals the function to remove the background which is also the first frame of the video.

while (1):
    ret, frame = cap.read()
    # each frame now goes through this loop.
    
    fgmask = fgbg.apply(frame)
    # aplying the background subtractor to find what is in the frame which is not in the original first frame.

    thresh = fgmask
    thresh = cv2.GaussianBlur(thresh, (21, 21), 0)
    thresh = cv2.threshold(thresh, 127, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    # making the frame into binary so the object moving is white with the background black.
    (cnts,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # finding the contours of the edges of the object moving.

    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue
    # going through the argument i made earlier so only objects bigger then the minimum area, are recognised.

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+ w, y + h), (0, 0, 255), 2)
        # draws a rectangle around the object.
        cv2.circle(frame, (x + w / 2, y + h / 2), 2, (0, 255, 0), -1)
        # draws a circle in the middle of object, also where the bb gun is going to be pointed.
        print (x + w / 2, y + h / 2)
        # prints the exact co-ordinates of the circle.


    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("fgmask", fgmask)
    # shows the frames of the feed from the camera with tracking, the one with the background subtracted and the binary one.
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    # so i can break the cycle by pressing q.

cap.release()
cv2.destroyAllWindows()
# releases and destroys all the windows which are open after the loop has ended.
