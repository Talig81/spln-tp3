import rimas as rimas

class Verso:
    def __init__(self, body: str):
        self.body = body


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
        else:
            return 'irregular'

    @property
    def n_versos(self):
        return len(list(self.versos))

    @property
    def versos(self):
        for line in self.body.split('\n'):
            yield Verso(line)


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
        return c[1:-1]

    @property
    def estruturaFixa(self):
        c = []
        for estrofe in self.estrofes:
            c.append(estrofe.n_versos)

        c.pop()
        if self.n_estrofes == 4:
            if(c[0] == 4 and c[1]==4 and c[2] == 3 and c[3]==3):
                return "é um Soneto"
            elif (c[0] == 8 and c[1]==8 and c[2] == 8 and (c[3]==4 or c[3]==5)):
                return "é uma Balada"

        elif len(c) == 7 and (c[0] == 6 and c[1]== 6 and c[2] == 6 and c[3]== 6 and c[4] == 6 and c[5]==6 and c[6] == 3):
            return "é uma Sextina"

        elif len(c)==3:
            if(c[0] == 5 and c[1]== 3 and c[2] == 5):
                return "é um Rondó"
            elif(c[0] == 4 and c[1]==4 and c[2] == 5):
                return "é um Rondel"

        elif len(c)==1 and c[0] == 3:
            return "é um Haicai"

        return "não tem estrutura fixa"


    @property
    def estruturaFixa2(self):
        resultados = {
            "Soneto": (4, [4, 4, 3, 3]),
            "Balada": (8, [8, 8, 4, 5]),
            "Sextina": (7, [6, 6, 6, 6 ,6, 6, 3]),
            "Rondó": (4, [5, 3, 5]),
            "Rondel": (3, [4, 4, 5]),
            "Haicai": (1, [3]),
        }

        n_versos_por_estrofe = [estrofe.n_versos for estrofe in self.estrofes]
        
        for (nome_estrutura, (n_estrofes, n_versos_por_estrofe_esperado)) in resultados.items():
            if self.n_estrofes != n_estrofes:
                continue
            if n_versos_por_estrofe == n_versos_por_estrofe_esperado:
                return nome_estrutura

        return None

def contaEstrofes(poema):
    for values in poema.split("\n\n"):
        contaestrofes+=1
    return contaestrofes




def main():
    with open('poema1.txt') as f:
        poema = Poema(f.read())
        estrofes = poema.estrofes
        c = poema.estruturaFixa2
        print(c)
        print(rimas.aliteracao("Isto sofre sofrendo sofrido"))
        
        
       # nEstrofes = contaEstrofes(poema)
       # rimas.rima("foder","perder")


if __name__ == '__main__':
    main()