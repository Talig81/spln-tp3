import rimas as rimas

class Verso:
    def __init__(self, body: str):
        self.body = body


class Estrofe:
    def __init__(self, body: str):
        self.body = body

    @property
    def n_versos_label(self):
        n_versos = self.n_versos
        if n_versos == 1:
            return 'monóstico'
        elif n_versos == 2:
            return 'dístico'
        elif False:
            ...
        else:
            return 'irregular'

    @property
    def n_versos(self):
        return len(self.versos)
    
    @property
    def versos(self):
        for line in self.body.split('\n'):
            yield Verso(line.strip())


class Poema:
    def __init__(self, body: str):
        self.body = body

    @property
    def estrofes(self):
        for line in self.body.split('\n\n'):
            yield Estrofe(line.strip())


def main():
    with open('poema1.txt') as f:
        line = f.readline()
        cenas = f.read()
        contaestrofes=0
        for values in cenas.split("\n\n"):
            print(values)
            print("-------------")
            contaestrofes+=1
        

        rimas.rima("foder","perder")


main()