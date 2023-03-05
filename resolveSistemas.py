#Vitor Farias, 24/02/2023
import gauss_functions

print("This program will solve your linear system using the Gauss Jordan method.")
print("Write the equations in this notation: Ax + By = C")
print("x and y must be written in lower case.")
print("Negative numbers that are coeficient of y must be written in this notation: Ax + -By = C")
print("A, B and C are scalars and you must use the decimal separator as the dot(.):")

class Array:
    def __init__(self,newArray):
        self.A = newArray[0][0]
        self.B = newArray[0][1]
        self.C = newArray[0][2]
        self.D = newArray[1][0]
        self.E = newArray[1][1]
        self.F = newArray[1][2]
        self.scaled = False

    def scale(self):
        if self.scaled == False:
            self.E = self.E - self.B*self.D/self.A
            self.F = self.F - self.C*self.D/self.A
            self.D = 0; #0 = D - A*D/A

            self.F = self.F/self.E
            self.E = 1; #E/E = 1            

            self.C = self.C - self.B*self.F
            self.B = 0; #B-B*1 = 0            

            self.C = self.C/self.A
            self.A = 1; #A/A = 1 
             
            self.scaled = True    
        return self
    
    def getXValue(self):
        Array.scale(self)
        return self.C
    
    def getYValue(self):
        Array.scale(self)
        return self.F

eq1 = input("Write the first equation: ")
eq2 = input("Write the second equation: ")

coefX1 = gauss_functions.getCoef(eq1,"X")
coefY1 = gauss_functions.getCoef(eq1,"Y")
termIndep1 = gauss_functions.getCoef(eq1,"Indep")

coefX2 = gauss_functions.getCoef(eq2,"X")
coefY2 = gauss_functions.getCoef(eq2,"Y")
termIndep2 = gauss_functions.getCoef(eq2,"Indep")

myArray = Array([[coefX1, coefY1, termIndep1],
                 [coefX2, coefY2, termIndep2]])

try:
    print("The X value is:",myArray.getXValue(),"\nAnd the Y value is:",myArray.getYValue())

    scaledArray = [[myArray.A, myArray.B, myArray.C],
                   [myArray.D, myArray.E, myArray.F]]
               
    print("The scaled array is:\n",scaledArray[0],"\n",scaledArray[1])

except:
    try:
        if coefX1/coefX2 == termIndep1/termIndep2:
            print("It's not possible to find a single result to this system, because it's indeterminate.")
        else:
            print("It's not possible to solve this system, it's an impossible system.")
    except:
        if termIndep2 == 0:
            print("It's not possible to find a single result to this system, because it's indeterminate.")
        else:
            print("It's not possible to solve this system, it's an impossible system.")