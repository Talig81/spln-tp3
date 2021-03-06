import rimas as rimas
import re
import unidecode
import dataminer3 as dataminer3 

vogals = ["a","e","i","o","u"]
vogalsAcentos = ["à","á","é","í","õ","ô","ú","â","ê"]


class Verso:
    def __init__(self, body: str):
        self.body = body
    def __repr__(self):
        return self.body

class Estrofe:
    def __init__(self, body: str):
        self.body = body

    def __repr__(self):
        return "represento isto: " + self.body

    @property
    def n_versos_label(self):
        n_versos = self.n_versos
        if n_versos == 1:
            return 'monóstico'
        elif n_versos == 2:
            return 'dístico'
        elif n_versos == 3:
            return 'terceto'
        elif n_versos == 4:
            return 'quadra'
        elif n_versos == 5:
            return 'quintilha'
        elif n_versos == 6:
            return 'sextilha'
        elif n_versos == 7:
            return 'septilha'
        elif n_versos == 8:
            return 'oitava'
        elif n_versos == 9:
            return 'nona'
        elif n_versos == 10:
            return 'decima'
        elif False:
            ...
        else:
            return 'é irregular'

    @property
    def n_versos(self):
        c = 0
        for i in self.versos:
            c+=1
        return c

    @property
    def versos(self):
        versos = []
        for line in self.body.split('\n'):
            versos.append(Verso(line))
        return versos


class Poema:
    def __init__(self, body: str):
        self.body = body

    @property
    def n_estrofes(self):
        return len(list(self.estrofes))

    @property
    def estrofes(self):
        c = []
        for line in self.body.split('\n\n'):
            c.append(Estrofe(line.strip()))
        return c
    @property
    def estruturaFixa(self):
        c = []
        for estrofe in self.estrofes:
            c.append(estrofe.n_versos)
        c.pop()
        if len(c) == 4:
            if(c[0] == 4 and c[1]==4 and c[2] == 3 and c[3]==3):
                return "é um Soneto"
            elif (c[0] == 8 and c[1]==8 and c[2] == 8 and (c[3]==4 or c[3]==5)):
                return "é uma Balada"
            else:
                return "não tem estrutura fixa"
        elif len(c) == 7:
            if(c[0] == 6 and c[1]== 6 and c[2] == 6 and c[3]== 6 and c[4] == 6 and c[5]==6 and c[6] == 3):
                return "é uma Sextina"
            else:
                return "não tem estrutura fixa"
        elif len(c)==3:
                if(c[0] == 5 and c[1]== 3 and c[2] == 5):
                    return "é um Rondó"
                elif(c[0] == 4 and c[1]==4 and c[2] == 5):
                    return "é um Rondel"
                else:
                    return "não tem estrutura fixa"
        elif len(c)==1:
            if(c[0]==3):
                return "é um Haicai"
            else:
                return "não tem estrutura fixa"
        else:
            return 0

def contaEstrofes(poema):
    for values in poema.split("\n\n"):
        contaestrofes+=1
    return contaestrofes

def contaMetrica(verso):
    conta = 0
    words = re.findall(r"[\w']+",verso)
    for w in words:
        firstLetter = unidecode.unidecode(w[0]).lower()
        print("letter before: " + w[0] + " after: " + firstLetter)
        if(firstLetter == 'y' or len(w) == 1):
            contaMetricaManual(w)
        with open("datasets/divisaosilabica_"+firstLetter+".csv") as f:
            readfile = f.read()
            wordLowered = w.lower()
            matches = re.search(rf"(\b{wordLowered}\b), (\(.+\)), (.+)",readfile,re.MULTILINE)
            if(matches == None):
                conta += (contaMetricaManual(w))
            else:
                conta += (contaSilaba(matches.group(3)))
    return conta           

def contaSilaba(palavra):
    conta = 1
    for p in palavra:
        if(p == '·'):
            conta += 1
    return conta     

def contaMetricaManual(verso):
    if len(verso) < 3:
        return 1
    elif len(verso) > 5 and len(verso) < 8:
        return 3
    elif len(verso) > 7:
        return 4
    else:
        return 2

#def infoVersos(verso):

def verificaAlit(verso):
    if(rimas.aliteracao(verso) != 0):
        print(rimas.aliteracao(verso))

def main():
    with open('poema2.txt') as f:
        iterator = 0
        secondIterator = 1
        line = f.readline()
        poema = Poema(f.read())
        treated = poema.body
        (scheme, allSilabas) = dataminer3.funcaoSilabas(poema.body)
        estrofes = poema.estrofes
        c = poema.estruturaFixa
        estrofes.pop()
        print("Este poema é constituido por " + str(poema.n_estrofes - 1) + " estrofes")
        if(poema.estruturaFixa != 0):
            print("Como estrutura fixa este poema " + poema.estruturaFixa)
        else:
            print("Não tem estrutura fixa")
        print("O seu esquema rimático é de: " + scheme[:-1])
        for estrofe in estrofes:
            iterator += 1
            print("A estrofe " + str(iterator) + " tem " + str(estrofe.n_versos) + " versos: " + estrofe.n_versos_label)
            for verso in estrofe.versos:
                print("O verso " + str(secondIterator) + " tem " + allSilabas[secondIterator-1] + " silabas")
                secondIterator += 1
        print(allSilabas)           
                

if __name__ == '__main__':
    main()