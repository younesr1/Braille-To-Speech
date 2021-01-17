#!/usr/bin/python3
'''
import os
def cropImage(input_path, output_path = ""):
    if not output_path:
        output_path = input_path
    os.system(f"convert {input_path} -trim {output_path}")
'''
from PIL import Image
import numpy as np
from cv2 import cv2

def processImage(i):
    #image = Image.open(i) #read in the image in rgb format. IMAGE MUST BE A JPG
    image = cv2.imread(i)
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

    return newMatrix



def cropTop(image): #iterate through the top rows looking for unneeded whitespace. Input must be from above fn
    numRow = np.shape(image)[0]
    numCol = np.shape(image)[1]
    lastWhite = 0 #the last row that is fully white

    for r in range(0,numRow):
        foundBlack = False
        for c in range(0,numCol):
            if image[r][c] == 0: #have hit a black pixel
                foundBlack = True
                break
        if foundBlack:
            break
        else:
            lastWhite += 1
    return max(0,lastWhite - 10) #the number of pixels of whitespace to keep

def cropBottom(image):
    numRow = np.shape(image)[0]
    numCol = np.shape(image)[1]
    lastWhite = numRow - 1

    while(True):
        foundBlack = False
        for col in range(0,numCol):
            if image[lastWhite][col] == 0: #have hit black pixel
                foundBlack = True
                break
        if foundBlack:
            break
        else:
            lastWhite -= 1

    return min(numRow-1,lastWhite+10)


def cropLeft(image):
    numRow = np.shape(image)[0]
    numCol = np.shape(image)[1]
    lastWhite = 0

    for col in range(0,numCol):
        foundBlack = False
        for row in range(0,numRow):
            if image[row][col] == 0: #found black
                foundBlack = True
                break
        if foundBlack:
            break
        else:
            lastWhite += 1

    return max(0,lastWhite-10)


def cropRight(image):
    numRow = np.shape(image)[0]
    numCol = np.shape(image)[1]

    lastWhite = numCol - 1
    while True:
        foundBlack = False
        for r in range(0,numRow):
            if image[r][lastWhite] == 0: #found black
                foundBlack = True
                break
    
        if foundBlack:
            break
        else:
            lastWhite -= 1
    return min(numCol-1,lastWhite+10)

def cropImage(file_path):
    image = processImage(file_path)

    rowOnes = np.ones((np.shape(image)[0],10))
    image = np.column_stack((image,rowOnes))
    image = np.column_stack((rowOnes,image))

    colOnes = np.ones((10,np.shape(image)[1]))
    image = np.row_stack((colOnes,image))
    image = np.row_stack((image,colOnes))

    #top crop
    image = image[cropTop(image):]

    #bottom crop
    image = image[0:cropBottom(image)]

    #left crop
    image = image[:,cropLeft(image):]

    #right crop
    image = image[:,0:cropRight(image)]

    newImage = Image.fromarray(image)
    #newImage.save("images/newImageCropped.tiff")
    cv2.imwrite(file_path,image*255)
    return image
