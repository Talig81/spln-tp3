import re
import unidecode

vogals = ["a", "e", "i", "o", "u"]
vogalsAcentos = ["à", "á", "é", "í", "õ", "ô", "ú", "â", "ê"]


def rima(pal1, pal2):
    conta = 0
    flag = 1
    rev1 = reversed(pal1)
    rev2 = reversed(pal2)
    for c, d in zip(rev1, rev2):
        if(c == d and flag == 1):
            conta += 1
        else:
            break
    if(conta <= 1):
        print("nao rima")
    if(conta == 2):
        print("cenas")
    elif(conta >= 3):
        print("rima perfeita")


def rimaRica(pal1, pal2):
    pal1Decoded = unidecode.unidecode(pal1)
    pal2Decoded = unidecode.unidecode(pal2)
    word1Lowered = pal1Decoded.lower()
    word2Lowered = pal2Decoded.lower()
    print(pal1Decoded + "   " + pal2Decoded)
    if(pal1Decoded[0] == pal2Decoded[0]):
        with open("datasets/divisaosilabica_"+pal2Decoded[0]+".csv") as f:
            readfile = f.read()
            matches = re.search(rf"(\b{word1Lowered}\b), (\(.+\)), (.+)", readfile, re.MULTILINE)
            matches2 = re.search(rf"(\b{word2Lowered}\b), (\(.+\)), (.+)", readfile, re.MULTILINE)
            return matchesRica(matches,matches2,pal1Decoded,pal2Decoded)
    else:
        with open("datasets/divisaosilabica_"+pal1Decoded[0]+".csv") as f1:
            with open("datasets/divisaosilabica_"+pal2Decoded[0]+".csv") as f2:
                readfile1 = f1.read()
                readfile2 = f2.read()
                matches = re.search(rf"(\b{word1Lowered}\b), (\(.+\)), (.+)", readfile1, re.MULTILINE)
                matches2 = re.search(rf"(\b{word2Lowered}\b), (\(.+\)), (.+)", readfile2, re.MULTILINE)
                return matchesRica(matches,matches2,pal1Decoded,pal2Decoded)

def matchesRica(matches, matches2,pal1Decoded,pal2Decoded):
    if(matches == None and matches2 == None):
        if (ifVerbo(pal1Decoded) == True and ifVerbo(pal2Decoded) == True):
            return 1
        else:
            return 0
    elif (matches == None):
        if (ifVerbo(pal1Decoded) ==True and matches2.group(3)=="(verbo)"):
            return 1
        else:
            return 0
    elif (matches2 == None):
        if (ifVerbo(pal2Decoded) ==True and matches.group(2)=="(verbo)"):
            return 1
        else:
            return 0
    elif (matches.group(2) == matches2.group(2)):
        return 1
    else:
        return 2


def ifVerbo(pal):
    with open("datasets/verbos_"+pal[0]+".txt") as f:
        readfile = f.read()
        wordLowered = pal.lower()
        matches = re.search(rf"(\b{wordLowered}\b), (\(.+\)), (.+)", readfile,re.MULTILINE)
        if(matches == None):
            return False
        else:
            return True


def aliteracao(verso):
    verseTreated = verseTreatment(str(verso))
    for palavra in verseTreated:
        if(isOneLetter(palavra) != True and isVogal(palavra[0]) != True):
            if(isAliteracao(palavra, verseTreated) >= 3):
                return "Verso tem aliteração na consoante: " + palavra[0]
    return 0

def isAliteracao(palavra, verso):
    auxLetter = palavra[0].lower()
    conta = 0
    for p in verso:
        if(p[0].lower() == auxLetter):
            conta += 1
    return conta


def verseTreatment(verso):
    verso = verso.strip(",")
    return verso.split(" ")


def isOneLetter(palavra):
    if(len(palavra) ==1):
        return True
    else:
        return False


def isVogal(letra):
    lowered = letra.lower()
    if lowered in "aeiou":
        return True
    else:
        return False
