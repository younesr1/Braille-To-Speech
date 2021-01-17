import sys
import cv2 as cv
import numpy as np
import math


def main(argv):

    default_file = 'smarties.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print(
            'Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    #gray = cv.medianBlur(gray, 5)

    #rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,
                              1, param1=100, param2=12, minRadius=gray.shape[0]//50, maxRadius=gray.shape[0]//5)

    output = np.array([[0, 0],
                       [0, 0],
                       [0, 0]])
    if circles is not None:
        (delta_y, delta_x) = (src.shape[0]/3, src.shape[1]/2)
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            output[math.floor(circle[1]/delta_y)
                   ][math.floor(circle[0]/delta_x)] = 1
            cv.circle(src, (circle[0], circle[1]), circle[2], (255, 0, 255), 1)

        print(output)
    else:
        print("NO CIRCLES FOUND", output)

    cv.imshow("detected circles", src)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
