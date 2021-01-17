#!/usr/bin/python3
import sys
sys.path.append("../../")
import cv2 as cv
import numpy as np
from lib.vision import BrailleToMatrix

filename = "Confettis-Braille_letter.png"
character = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
matrix = BrailleToMatrix.convert(character)
print(matrix)
