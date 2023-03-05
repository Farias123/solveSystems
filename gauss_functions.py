def getCoefX(eq):
#Essa funcao vai percorrer os caracteres da equacao e pegar um por um ate que chegue no x, ela
#entao retornara o valor do coeficiente multiplicador de X. 
    return 


def getCoefY(eq):
#Essa funcao vai percorrer os caracteres da equacao depois do sinal de soma e pegar um por um
#ate que chegue no y, ela entao retornara o valor do coeficiente multiplicador de Y. 
    return 

def getIndep(eq):
#Essa funcao vai percorrer os caracteres da equacao depois do sinal de igualdade e pegar um por um
#ate que chegue ao fim da equacao, ela entao retornara o valor do termo independente. 
    return 

def getCoef(eq,definer):
    if definer == "X":
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
    
    elif definer == "Y":
        sumHappened = False
        coefY = ''
        for a in eq:
            if sumHappened == False:
                if a == '+':
                    sumHappened = True
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
    
    elif definer == "Indep":
        equalsHappened = False
        termIndep = ''
        for a in eq:
            if equalsHappened == False:
                if a == '=':
                    equalsHappened = True
            else:
                termIndep += str(a)
        termIndep = float(termIndep)
        return termIndep