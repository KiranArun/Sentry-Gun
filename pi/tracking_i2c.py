import numpy as np
import cv2
import time
import argparse
import smbus
import time
bus = smbus.SMBus(1)

address = 0x04

def writenum(value):
    bus.write_byte(address,value)
    return -1


ap = argparse.ArgumentParser()
ap.add_argument("-a", "--min-area", type=int, default=100, help="minimum area")
args = vars(ap.parse_args())
cap = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG()

while (1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    thresh = fgmask
    thresh = cv2.GaussianBlur(thresh, (21, 21), 0)
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+ w, y + h), (0, 0, 255), 2)
        cv2.circle(frame, (x + w / 2, y + h / 2), 2, (0, 255, 0), -1)

        a = (x + w) / 2
        writenum(a)
        print(a)

        b = (y + h) / 2 + 100
        writenum(b)
        print(b)
        
        
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()
