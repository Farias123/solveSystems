def obterCoefX(eq):
#Essa funcao vai percorrer os caracteres da equacao e pegar um por um ate que chegue no x, ela
#entao retornara o valor do coeficiente multiplicador de X. 
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
#Essa funcao vai percorrer os caracteres da equacao depois do sinal de soma e pegar um por um
#ate que chegue no y, ela entao retornara o valor do coeficiente multiplicador de Y. 
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
#Essa funcao vai percorrer os caracteres da equacao depois do sinal de igualdade e pegar um por um
#ate que chegue ao fim da equacao, ela entao retornara o valor do termo independente. 
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