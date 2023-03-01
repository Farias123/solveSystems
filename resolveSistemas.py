# -*- coding: utf-8 -*-
import gauss_functions

#Vitor Farias, 24/02/2023
#Esse programa resolve um sistema linear de equacao de duas incognitas, com duas equacoes, utilizando
#o metodo de Gauss Jordan para a resolucao de matrizes(escalonamento).

def sum(num):
    return num

class Matriz:
#Essa classe vai usar a matriz que criarmos com os termos obtidos da equacao
#(escalares e termos independentes), para calcular o valor de X e Y usando metodos.
    def __init__(self,novaMatriz):
        self.A = novaMatriz[0][0]
        self.B = novaMatriz[0][1]
        self.C = novaMatriz[0][2]
        self.D = novaMatriz[1][0]
        self.E = novaMatriz[1][1]
        self.F = novaMatriz[1][2]
        self.escalonado = False

    def escalonar(self):

#Esse metodo serve para escalonar uma matriz 2X3, em que sua representacao seria:
#[A B C], e se essa matriz representar um sistema:[A B |C], o sistema esta no formato: {Ax + By = C
#[D E F]                                          [D E |F]                             {Dx + Ey = F
        if self.escalonado == False:

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
            self.escalonado = True    
        return self
    
    def obterValorX(self):
        Matriz.escalonar(self)
        return self.C
    
    def obterValorY(self):
        Matriz.escalonar(self)
        return self.F

eq1 = input("Escreva a equacao numero 1: ")
eq2 = input("Escreva a equacao numero 2: ")

coefX1 = gauss_functions.obterCoefX(eq1)
coefY1 = gauss_functions.obterCoefY(eq1)
termoIndep1 = gauss_functions.obterIndep(eq1)

coefX2 = gauss_functions.obterCoefX(eq2)
coefY2 = gauss_functions.obterCoefY(eq2)
termoIndep2 = gauss_functions.obterIndep(eq2)

minhaMatriz = Matriz([[coefX1, coefY1, termoIndep1],
                      [coefX2, coefY2, termoIndep2]])

try:
    print("O valor de X é:",minhaMatriz.obterValorX(),"\nE o valor de Y é:",minhaMatriz.obterValorY())

    matrizEscalonada = [[minhaMatriz.A, minhaMatriz.B, minhaMatriz.C],
                        [minhaMatriz.D, minhaMatriz.E, minhaMatriz.F]]
               
    print("A matriz escalonada fica assim:\n",matrizEscalonada[0],"\n",matrizEscalonada[1])

except:
#Essa excecao foi criada para quando acontecer um erro de divisao por zero no escalonamento da matriz,
#que significa que a proporcao entre os multiplicadores de X e os multiplicadores de Y é a mesma.
#Se isso acontecer, significa que o sistema não é possivel e determinado.
    try:
        if coefX1/coefX2 == termoIndep1/termoIndep2:
            print("Não é possível encontrar um único resultado para esse sistema, pois ele é um SPI.")
        else:
            print("Não é possível resolver esse sistema, pois ele é um SI.")
    except:
#Essa segunda excecao foi criada para, se na segunda equacao o multiplicador de X ou o termo 
#independente forem iguais a zero, o erro de divisao por zero nao acontecer.
        if termoIndep2 == 0:
            print("Não é possível encontrar um único resultado para esse sistema, pois ele é um SPI.")
        else:
            print("Não é possível resolver esse sistema, pois ele é um SI.")