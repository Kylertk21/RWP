import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv.line(frame, (0,0), (width, height), (255, 0, 0), 10)
    img = cv.line(img, (0,height), (width, 0), (255, 0, 0), 10)
    img = cv.rectangle(img, (0,0), (width, height), (128,128,128), 5)
    img = cv.circle(img, (300,300), 60, (0,0,255), -1)
    font = cv.FONT_HERSHEY_DUPLEX
    img = cv.putText(img, 'Testing', (200, height - 10), font, 4, (255,0,0), 3, cv.LINE_AA)
    

    cv.imshow('frame', img)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()