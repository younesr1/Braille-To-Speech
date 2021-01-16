import english
import numpy as np

def testChar():
    direction = input("Input a lower case letter or type 'quit' to quit: ")
    while direction != "quit":
        print(english.getChar(direction))
        print("")
        direction = input("Input a lower case letter or type 'quit' to quit: ")

def testMatrixToEnglish():
    direction = input("Input a matrix in the form r1c1 r1c2 r2c1 r2c2 r3c1 r3c2 or type 'quit' to quit: ")
    while direction != "quit":
        lister = direction.split()
        matrix = np.array([[int(lister[0]),int(lister[1])],[int(lister[2]),int(lister[3])],[int(lister[4]),int(lister[5])]])
        answer = english.findChar(matrix)
        if answer == None:
            print("That is not a braille letter.")
        else:
            print(answer)
        direction = input("Input a matrix in the form r1c1 r1c2 r2c1 r2c2 r3c1 r3c2 or type 'quit' to quit: ")


def tester():
    direction = input("To test the matrix to letter function, type 'm'. To test char to letter type 'c': ")

    if direction == "c":
        testChar()
    else:
        testMatrixToEnglish()

tester()