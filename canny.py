import numpy as np
import cv2 as cv
count = 0
img = cv.imread('tang.png',0)
img = cv.Canny(img,100,200)
cv.imshow('detected circles',img)
cv.waitKey(0)
cv.destroyAllWindows()