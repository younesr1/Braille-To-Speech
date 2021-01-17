from PIL import Image
import numpy as np
from cv2 import cv2

def imageToFile(input, output):
    image = cv2.imread(input)
    matrixRep = np.asarray(image)
    numRows = np.shape(matrixRep)[0]
    numCol = np.shape(matrixRep)[1]
    #now test whether that pixel is white or non white

    newMatrix = np.zeros((numRows,numCol)) #initialize an empty matrix to update
    for row in range(0,numRows):
        for col in range(0,numCol):
            if matrixRep[row][col][0] > 127 or matrixRep[row][col][1] > 127 or matrixRep[row][col][2] > 127:
                newMatrix[row,col] = 1
            else:
                newMatrix[row,col] = 0
    with open(output,mode = "w") as file:
        string = f"{numRows},{numCol},\n"
        for c in range(0,numCol):
            for r in range(0,numRows):
                string += f"{int(newMatrix[r][c])},"
        file.write(string)
    