import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv.rotate(smaller_frame, cv.ROTATE_180) #Top Left
    image[height//2:, :width//2] = smaller_frame #Bottom Left
    image[:height//2, width//2:] = cv.rotate(smaller_frame, cv.ROTATE_180) #Top Right
    image[height//2:, width//2:] = smaller_frame #Bottom Right

    cv.imshow('frame', image)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()