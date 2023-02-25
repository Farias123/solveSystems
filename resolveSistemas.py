#Vitor Farias, 24/02/2023
#Esse programa resolve um sistema linear de equação de duas incógnitas, com duas equações, utilizando
#o método de Gauss Jordan para a resolução de matrizes(escalonamento).
print("Esse programa vai resolver seu sistema linear usando o método de Gauss Jordan.")
print("Escreva as equações na notação: Ax + By = C")
print("O x e o y devem ser escritos em letra minúscula.")
print("Números negativos coeficientes de y devem ser escritos na notação: Ax + -By = C")
print("A, B e C são escalares e você deve usar o separador decimal como ponto:")

def obterCoefX(eq):
#Essa função vai percorrer os caracteres da equação e pegar um por um até que chegue no x, ela
#então retornará o valor do coeficiente multiplicador de X. 
    coefX = ' '
    for a in eq:
        if a != 'x':
            coefX += str(a)
        else:
            break
    if coefX == ' ':
        coefX = 1
    elif coefX == ' -':
        coefX = -1
    else:
        coefX = float(coefX)
    return coefX

def obterCoefY(eq):
#Essa função vai percorrer os caracteres da equação depois do sinal de soma e pegar um por um
#até que chegue no y, ela então retornará o valor do coeficiente multiplicador de Y. 
    contSomas = 0
    coefY = ''
    for a in eq:
        if contSomas == 0:
            if a == '+':
                contSomas += 1
        elif a != 'y':
            coefY += str(a)
        else:
            break
    if coefY == ' ':
        coefY = 1
    elif coefY == ' -':
        coefY = -1
    else:
        coefY = float(coefY)
    return coefY

def obterIndep(eq):
#Essa função vai percorrer os caracteres da equação depois do sinal de igualdade e pegar um por um
#até que chegue ao fim da equação, ela então retornará o valor do termo independente. 
    foiIgual = False
    termoIndep = ''
    for a in eq:
        if foiIgual == False:
            if a == '=':
                foiIgual = True
        else:
            termoIndep += str(a)
    termoIndep = float(termoIndep)
    return termoIndep

class Matriz:
#Essa classe vai usar a matriz que criarmos com os termos obtidos da equação
#(escalares e termos independentes), para calcular o valor de X e Y usando métodos.
    def __init__(self,novaMatriz):
        self.A = novaMatriz[0][0]
        self.B = novaMatriz[0][1]
        self.C = novaMatriz[0][2]
        self.D = novaMatriz[1][0]
        self.E = novaMatriz[1][1]
        self.F = novaMatriz[1][2]
        self.escalonado = False

    def escalonar(self):
#Esse método serve para escalonar uma matriz 2X3, em que sua representação seria:
#[A B C], e se essa matriz representar um sistema:[A B |C], o sistema está no formato: {Ax + By = C
#[D E F]                                          [D E |F]                             {Dx + Ey = F
        if self.escalonado == False:
#O primeiro passo para escalonar a matriz é zerar o primeiro termo da segunda linha, subtraindo na
#segunda linha, a multiplicação da primeira linha com D/A, assim o D se reduz a zero:
            self.E = self.E - self.B*self.D/self.A
            self.F = self.F - self.C*self.D/self.A
            self.D = 0; #0 resulta de D - A*D/A
#O próximo passo é passar o termo E dividindo do lado direito, para ficarmos com E resultando 1,
#ou seja, teremos então que 0x + 1y = F, portanto F corresponde ao valor de y:
            self.F = self.F/self.E
            self.E = 1; #Porque E/E = 1            
#Agora nós vamos zerar o segundo termo da primeira linha, subtraímos na primeira linha, a
#multiplicação da segunda linha por B, assim o B se reduz a zero:
            self.C = self.C - self.B*self.F
            self.B = 0; #B-B*1 = 0            
#Nessa etapa na primeira linha, passaremos A dividindo do lado direito, para ficarmos com o
#valor de A resultando 1, teremos então que 1x + 0y = C, então C corresponde ao valor de x:
            self.C = self.C/self.A
            self.A = 1; #Porque A/A = 1 
#Pronto, nossa matriz já está escalonada. 
            self.escalonado = True    
        return self
    
    def obterValorX(self):
        Matriz.escalonar(self)
        return self.C
    
    def obterValorY(self):
        Matriz.escalonar(self)
        return self.F

eq1 = input("Escreva a equação número 1: ")
eq2 = input("Escreva a equação número 2: ")

coefX1 = obterCoefX(eq1)
coefY1 = obterCoefY(eq1)
termoIndep1 = obterIndep(eq1)

coefX2 = obterCoefX(eq2)
coefY2 = obterCoefY(eq2)
termoIndep2 = obterIndep(eq2)

minhaMatriz = Matriz([[coefX1, coefY1, termoIndep1],
                      [coefX2, coefY2, termoIndep2]])

try:
    print("O valor de X é:",minhaMatriz.obterValorX(),"\nE o valor de Y é:",minhaMatriz.obterValorY())

    matrizEscalonada = [[minhaMatriz.A, minhaMatriz.B, minhaMatriz.C],
                        [minhaMatriz.D, minhaMatriz.E, minhaMatriz.F]]
               
    print("A matriz escalonada fica assim:\n",matrizEscalonada[0],"\n",matrizEscalonada[1])

except:
#Essa exceção foi criada para quando acontecer um erro de divisão por zero no escalonamento da matriz,
#que significa que a proporção entre os multiplicadores de X e os multiplicadores de Y é a mesma.
#Se isso acontecer, significa que o sistema não é possível e determinado.
    try:
        if coefX1/coefX2 == termoIndep1/termoIndep2:
            print("Não é possível encontrar um único resultado para esse sistema, pois ele é um SPI.")
        else:
            print("Não é possível resolver esse sistema, pois ele é um SI.")
    except:
#Essa segunda exceção foi criada para, se na segunda equação o multiplicador de X ou o termo 
#independente forem iguais a zero, o erro de divisão por zero não acontecer.
        if termoIndep2 == 0:
            print("Não é possível encontrar um único resultado para esse sistema, pois ele é um SPI.")
        else:
            print("Não é possível resolver esse sistema, pois ele é um SI.")