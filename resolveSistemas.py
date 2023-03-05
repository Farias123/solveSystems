import gauss_functions

#Vitor Farias, 24/02/2023
#Esse programa resolve um sistema linear de equacao de duas incognitas, com duas equacoes, utilizando
#o metodo de Gauss Jordan para a resolucao de matrizes(escalonamento).
print("This program will solve your linear system using the Gauss Jordan method.")
print("Write the equations in this notation: Ax + By = C")
print("x and y must be written in lower case.")
print("Negative numbers that are coeficient of y must be written in this notation: Ax + -By = C")
print("A, B and C are scalars and you must use the decimal separator as the dot(.):")


class Array:
#Essa classe vai usar a matriz que criarmos com os termos obtidos da equacao
#(escalares e termos independentes), para calcular o valor de X e Y usando metodos.
    def __init__(self,newArray):
        self.A = newArray[0][0]
        self.B = newArray[0][1]
        self.C = newArray[0][2]
        self.D = newArray[1][0]
        self.E = newArray[1][1]
        self.F = newArray[1][2]
        self.scaled = False

    def scale(self):

#Esse metodo serve para escalonar uma matriz 2X3, em que sua representacao seria:
#[A B C], e se essa matriz representar um sistema:[A B |C], o sistema esta no formato: {Ax + By = C
#[D E F]                                          [D E |F]                             {Dx + Ey = F
        if self.scaled == False:

#O primeiro passo para escalonar a matriz é zerar o primeiro termo da segunda linha, subtraindo na
#segunda linha, a multiplicação da primeira linha com D/A, assim o D se reduz a zero:

            self.E = self.E - self.B*self.D/self.A
            self.F = self.F - self.C*self.D/self.A
            self.D = 0; #0 resulta de D - A*D/A

#O proximo passo é passar o termo E dividindo do lado direito, para ficarmos com E resultando 1,
#ou seja, teremos então que 0x + 1y = F, portanto F corresponde ao valor de y:

            self.F = self.F/self.E
            self.E = 1; #Porque E/E = 1            

#Agora nos vamos zerar o segundo termo da primeira linha, subtraimos na primeira linha, a
#multiplicacao da segunda linha por B, assim o B se reduz a zero:

            self.C = self.C - self.B*self.F
            self.B = 0; #B-B*1 = 0            
#Nessa etapa na primeira linha, passaremos A dividindo do lado direito, para ficarmos com o
#valor de A resultando 1, teremos então que 1x + 0y = C, então C corresponde ao valor de x:
            self.C = self.C/self.A
            
            self.A = 1; #Porque A/A = 1 
            
#Pronto, nossa matriz ja esta escalonada. 
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
#Essa excecao foi criada para quando acontecer um erro de divisao por zero no escalonamento da matriz,
#que significa que a proporcao entre os multiplicadores de X e os multiplicadores de Y é a mesma.
#Se isso acontecer, significa que o sistema não é possivel e determinado.
    try:
        if coefX1/coefX2 == termIndep1/termIndep2:
            print("It's not possible to find a single result to this system, because it's indeterminate.")
        else:
            print("It's not possible to solve this system, it's an impossible system.")
    except:
#Essa segunda excecao foi criada para, se na segunda equacao o multiplicador de X ou o termo 
#independente forem iguais a zero, o erro de divisao por zero nao acontecer.
        if termIndep2 == 0:
            print("It's not possible to find a single result to this system, because it's indeterminate.")
        else:
            print("It's not possible to solve this system, it's an impossible system.")