# SPLN-TP3 - Analisador de Poemas

Este projeto consiste na realização de um analisador de poemas em português. Este porgrama tem como requisitos estudar a estrutura e as várias caracteristicas de um poema (como rimas, a métrica, o numero de estrofes, etc...).


Name: Manuel Maria Moreno
StudentID: a67713
Date: 26/06/2020

## Web-Scrapping para Datasets

Antes de começar a analisarmos o poema, será interessante obter um dataset com todas as palavras portuguesas para obtermos a sua classe gramatical e também a sua divisão silábica.
Para isso fazemos um scrapping ao website www.portaldalinguaportuguesa.com que contém todas as palavras divididas por letras.
Primeiro começamos por buscar todos as páginas relacionadas com letras
```python
def getNumberPages(letter):
    r = requests.get('http://www.portaldalinguaportuguesa.org/index.php?action=syllables&act=list&letter='+letter)
    soup = BeautifulSoup(r.content,"html.parser")
    paragraphs = soup.findAll("p")
    matched = re.search(r'1 - 100 de (\d+) resultados',str(paragraphs[1].get_text),re.M|re.I)
    quantity = int(matched.group(1))
    return quantity
```

Após buscar todas as páginas procedemos a sua leitura e escrita num ficheiro. Este ficheiro será dividido por vários ficheiros cada um correspondendo a uma letra do abcedário português.
```python
def main():
    for letra in abc:
        pages = getNumberPages(letra)
        conta = 0
        for page_number in range(0, pages, 100):
            print(f"{letra} - {page_number}")
            response = urllib.request.urlopen(f'http://www.portaldalinguaportuguesa.org/index.php?action=syllables&act=list&letter={letra}&start={conta}')
            data = response.read().decode('utf-8', 'ignore')
            soup = BeautifulSoup(data,features="html.parser")
            rows = soup.find(id="rollovertable").findAll("tr")
            for row in rows:
                cells = row.findAll("td")
                if cells:
                    # __import__('pdb').set_trace()
                    palavra = cells[0].find('b').find('a').getText().encode()
                    file.write(palavra)
                    file.write(b',')
                    tipo = cells[0].getText().split("(")[1].split(")")[0].encode()
                    file.write(tipo)
                    file.write(b',')
                    divisaosilabica = cells[1].getText().encode()
                    file.write(divisaosilabica.replace(b"&middot;",b"."))
                    file.write(b"\n")
            break
```



## Estrutura fixa de um poema

Um poema tem como estrutura fixa uma certa combinação de estrofes e de versos. Por exemplo, um Soneto é constituído por duas quadras e dois tercetos.
Para contar as estrofes e os versos utiliza - se as seguintes funções
```python
    def n_estrofes(self):
        return len(list(self.estrofes))
```

```python
    def n_versos(self):
        return len(list(self.versos))
```
Após sabermos o número de versos e estrofes é possível verificar se têm uma certa estrutura fixa utilisando a seguinte função

```python
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
```

## WebScrapping para a divisão métrica.

Para descobrir a divisão métrica de cada verso, recorreu - se a um website que faz a divisão métrica e silábica e utilisando um scrapper, verificamos todo a métrica para cada verso que constitui um poema.

```python
def funcaoSilabas(texto):
    headers = {
        'authority': 'www.separarensilabas.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.separarensilabas.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.separarensilabas.com/index-pt.php',
        'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,ru;q=0.5',
        'cookie': 'cookieconsent_status=dismiss',
    }

    data = {
        'fs': texto,
        'cs': 'on',
        'an2': 'on',
        'button': 'Separar s\xEDlabas'
    }

    response = requests.post('https://www.separarensilabas.com/index-pt.php', headers=headers, data=data)
    soup = BeautifulSoup(response.content,features="html.parser")

    relevant_soup = soup.find("tr")
    esquemaMetrica = soup.find(text="Análise de estrofas (esquema métrico):").parent.nextSibling.nextSibling.li.getText()
    silabas = re.findall(r"\((\d+) sílabas\)", str(relevant_soup))
    return (esquemaMetrica,silabas))

```

## Rimas

Para verificar-se se as palavras rimam ou não e devido à dificuldade de atribuir fonética no programa, recorreu-se mais uma vez ao scrapping para verificar cada rima. Após a verificação de rima atribui-se um esquema rimático assim como a sua classificação quanto a esse esquema

```python
def esquemaRimativo(esquema):
    estrofes = esquema.split(" ")
    for estrofe in estrofes:
        if(estrofe[0] == estrofe[1]):
            print("Rima emparelhada em: " + estrofe[0])
        elif(estrofe[0] == estrofe[2]):
            print("Rima Cruazada em: " + estrofe[0])
        elif(estrofe[0] == estrofe[3]):
            print("Rima interpolada em: " + estrofe[0])
        else:
            print("rima solta")
```

Para as rimas perfeitas e imperfeitas primeiro temos que verificar se a sua terminação fonética e escrita coincidem e caso sejam muito diferentes podemos classificar como uma rima imperfeita.

```python
def rimaPerfeita(pal1, pal2):
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
        print("Rima imperfeita")
    if(conta == 2):
        print("Rima perfeita")
    elif(conta >= 3):
        print("Rima perfeita")
```

Quanto à riqueza das rimas (se é pobre ou rica), é preciso comparar a classe gramatical das palavras que constituem a rima. Para isso utilisa-se os datasets criados previamente e com uma expressão regular rapidamente conseguimos verificar se coincidem ou se são de classes diferentes
```python
def rimaRica(pal1, pal2):
    pal1Decoded = unidecode.unidecode(pal1)
    pal2Decoded = unidecode.unidecode(pal2)
    word1Lowered = pal1Decoded.lower()
    word2Lowered = pal2Decoded.lower()
    print(pal1Decoded + "-" + pal2Decoded)
    if(pal1Decoded[0] == pal2Decoded[0]):
        with open("datasets/divisaosilabica_"+pal2Decoded[0]+".csv") as f:
            readfile = f.read()
            matches = re.search(rf"(\b{word1Lowered}\b), (\(.+\)), (.+)", readfile, re.MULTILINE)
            matches2 = re.search(rf"(\b{word2Lowered}\b), (\(.+\)), (.+)", readfile, re.MULTILINE)
            return matchesRica(matches,matches2,word1Lowered,word2Lowered)
    else:
        with open("datasets/divisaosilabica_"+pal1Decoded[0]+".csv") as f1:
            with open("datasets/divisaosilabica_"+pal2Decoded[0]+".csv") as f2:
                readfile1 = f1.read()
                readfile2 = f2.read()
                matches = re.search(rf"(\b{word1Lowered}\b), (\(.+\)), (.+)", readfile1, re.MULTILINE)
                matches2 = re.search(rf"(\b{word2Lowered}\b), (\(.+\)), (.+)", readfile2, re.MULTILINE)
                if(matchesRica(matches,matches2,pal1Decoded,pal2Decoded) == 0):
                    return "Rima Rica"
                else:
                    return "Rima Pobre"
```

## Commands
Para correr o programa basta utilizar o seguinte comando

```$python3 initial.py```
