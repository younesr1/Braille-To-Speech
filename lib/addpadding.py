from PIL import Image
import numpy as np


def processImage(i):
    image = Image.open(i) #read in the image in rgb format
    matrixRep = np.asarray(image)
    numRows = np.shape(matrixRep)[0]
    numCol = np.shape(matrixRep)[1]
    
    
