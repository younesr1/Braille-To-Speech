#!/usr/bin/python3
import sys
import cv2 as cv
import numpy as np
from lib.vision import BrailleToMatrix
from lib.speech.speaker import Speaker
from lib.dictionary.english import Translator
from lib.vision.Cropper import cropImage

def main(argv):
    default_file = "images/a.png"
    image_path = argv[0] if len(argv) > 0 else default_file
    cropImage(image_path)

    matrices = BrailleToMatrix.convertWithJulia(image_path)

    translator = Translator()
    speaker = Speaker("en-gb", False)
    for matrix in matrices:
        speaker.speak(translator.findChar(matrix).englishChar)

    speaker.save("recordings/out.mp3")

if __name__ == "__main__":
    main(sys.argv[1:])
