from rhymez import Rhymez

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
    with open('file') as f:
        poema = Poema(f.read())
        print(poema.estrofes[0].n_versos_label)


main()