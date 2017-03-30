# importing the neccessery libraries 
import cv2
import time
import argparse

# disenabling opencl because it causes an error to do with the background subtraction
cv2.ocl.setUseOpenCL(False)

# able to set min area of object for different places
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--min-area", type=int, default=200, help="minimum area")
args = vars(ap.parse_args())

# capture the ideo from the webcam
cap = cv2.VideoCapture(0)

# this is the background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# start the main loop which runs everything
while (1):
	# read the frame from the capture
    ret, frame = cap.read()
    
    # apply the background subtractor
    thresh = fgbg.apply(frame)
    
    # now we need to apply filters to the frame
    # we first blur it, then turn it into binary and then dilate it which removes some noise
    thresh = cv2.GaussianBlur(thresh, (21, 21), 0)
    thresh = cv2.threshold(thresh, 127, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=1)
    
    # now we need to find the contours of the frame we applied the filters to using opencv's findContours
    _, cnts,_= cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# check that the contour area is bigger  then the  min we set  earlier
    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue

		# if i  want one box to appear on the largest contour use this line
        #c = max(cnts, key=cv2.contourArea)

		# draw the rectangle around the object
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+ w, y + h), (0, 0, 255), 2)

	# show the image in a new window
    cv2.imshow("Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # breakif q is pressed
    if key == ord("q"):
        break

# clean up
cap.release()
cv2.destroyAllWindows()
