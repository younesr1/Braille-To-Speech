import numpy as np

class Letter:
    def __init__(self,matrixRep,english):
        self.matrixRep = matrixRep
        self.englishChar = english
    def __repr__(self):
        return f"The braille representation of '{self.englishChar}' is: \n{self.matrixRep}"

a = Letter(np.array([[1,0],[0,0],[0,0]]),"a")
b = Letter(np.array([[1,0],[1,0],[0,0]]),"b")
c = Letter(np.array([[1,1],[0,0],[0,0]]),"c")
d = Letter(np.array([[1,1],[0,1],[0,0]]),"d")
e = Letter(np.array([[1,0],[0,1],[0,0]]),"e")
f = Letter(np.array([[1,1],[1,0],[0,0]]),"f")
g = Letter(np.array([[1,1],[1,1],[0,0]]),"g")
h = Letter(np.array([[1,0],[1,1],[0,0]]),"h")
i = Letter(np.array([[0,1],[1,0],[0,0]]),"i")
j = Letter(np.array([[0,1],[1,1],[0,0]]),"j")
k = Letter(np.array([[1,0],[0,0],[1,0]]),"k")
l = Letter(np.array([[1,0],[1,0],[1,0]]),"l")
m = Letter(np.array([[1,1],[0,0],[1,0]]),"m")
n = Letter(np.array([[1,1],[0,1],[1,0]]),"n")
o = Letter(np.array([[1,0],[0,1],[1,0]]),"o")
p = Letter(np.array([[1,1],[1,0],[1,0]]),"p")
q = Letter(np.array([[1,1],[1,1],[1,0]]),"q")
r = Letter(np.array([[1,0],[1,1],[1,0]]),'r')
s = Letter(np.array([[0,1],[1,0],[1,0]]),"s")
t = Letter(np.array([[0,1],[1,1],[1,0]]),"t")
u = Letter(np.array([[1,0],[0,0],[1,1]]),"u")
v = Letter(np.array([[1,0],[1,0],[1,1]]),"v")
w = Letter(np.array([[0,1],[1,1],[0,1]]),"w")
x = Letter(np.array([[1,1],[0,0],[1,1]]),"x")
y = Letter(np.array([[1,1],[0,1],[1,1]]),"y")
z = Letter(np.array([[1,0],[0,1],[1,1]]),"z")

listOfLetters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


def getChar(char): #essentially a dictionary
    asciiRep = ord(char)
    return listOfLetters[asciiRep-97]

def findChar(matrix): #this function matches a matrix representation to a specific letter
    #may need to rework code here so that it agrees with a numpy array
    for letter in listOfLetters:
        match = True
        for i in range(0,3):
            for x in range(0,2):
                if(not letter.matrixRep[i][x] == matrix[i][x]):
                    match = False
        
        if match:
            return letter
