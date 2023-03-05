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