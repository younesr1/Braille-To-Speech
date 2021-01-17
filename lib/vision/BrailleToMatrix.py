import os
import sys
import cv2 as cv
import numpy as np
import math
import re
import time
from .RawImgData import imageToFile

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


def convertWithJulia(img_path):
    # run julia script
    vision_folder = "lib/vision/"
    julia_script = vision_folder + "BrailleToMatrix.jl"
    data_file = vision_folder+"outputfFile.txt"
    imageToFile(img_path, data_file)
    os.system(f"chmod a+x {julia_script}")
    tic = time.perf_counter()
    os.system(f"./{julia_script} {data_file} temp.txt >/dev/null")
    toc = time.perf_counter()
    print(tic- toc)
    # parse the output
    out = []
    f = open("temp.txt", "r")
    for line in f:
        line = line.rstrip()
        data = [int(s) for s in re.findall(r'\b\d+\b', line)]
        out.append(np.array([[data[0], data[1]],
                             [data[2], data[3]],
                             [data[4], data[5]]]))
    os.system(f"rm -f temp.txt {data_file}")
    return out
