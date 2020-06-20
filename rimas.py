def rima(pal1,pal2):
    conta=0
    flag = 1
    print("Palavra1: ",pal1,"Cumprimento palavra1: ",len(pal1))
    print("Palavra2: ",pal2,"Cumprimento palavra2: ",len(pal2))
    for c,d in zip(reversed(pal1),reversed(pal2)):
        if(c==d and flag == 1):
            conta+=1
        else:
            flag = 0
    if(conta <= 1):
        print("nao rima")
    elif(conta >= 3):
        print("rima perfeita")


def aliteracao(verso):
    verseTreated = verseTreatment(str(verso))
    for palavra in verseTreated:
        if(isOneLetter(palavra) != True and isVogal(palavra[0])!= True):
            if(isAliteracao(palavra,verseTreated) >= 3):
                return "Verso tem aliteração na consoante: " + palavra[0]
    return ("Não tem aliteração")

def isAliteracao(palavra,verso):
    auxLetter = palavra[0].lower()
    conta = 0
    for p in verso:
        print("p: " , p)
        if(p[0].lower() == auxLetter):
            conta += 1
    print("conta: ",conta)
    return conta    


def verseTreatment(verso):
    verso = verso.strip(",")
    return verso.split(" ")


def isOneLetter(palavra):
    if(len(palavra)==1):
        return True
    else:
        return False

def isVogal(letra):
    lowered = letra.lower()
    if lowered in "aeiou":
        return True
    else:
        return False