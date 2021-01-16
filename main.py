#!/usr/bin/python3
import cv2 as cv
import numpy as np
from lib.vision import BrailleToMatrix
from lib.speech.speaker import Speaker
from lib.dictionary.english import Translator
from lib.vision.Cropper import cropImage

filename = "a.png"
cropImage(filename)

braille = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
matrix = BrailleToMatrix.convert(braille)
translator = Translator()

speaker = Speaker("en")
speaker.speak(translator.findChar(matrix).englishChar)
speaker.save("output2.mp3")

