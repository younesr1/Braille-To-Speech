import sys
import cv2 as cv
import numpy as np
import math

def convert(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                                1, param1=100, param2=12, minRadius=gray.shape[0]//50, maxRadius=gray.shape[0]//5)

    output = np.array([[0, 0],
                        [0, 0],
                        [0, 0]])
    if circles is None:
        return None
    (delta_y, delta_x) = (img.shape[0]/3, img.shape[1]/2)
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        output[math.floor(circle[1]/delta_y)][math.floor(circle[0]/delta_x)] = 1
    return output
