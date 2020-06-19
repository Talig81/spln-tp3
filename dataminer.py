from bs4 import BeautifulSoup
import requests
import urllib.request
import re



abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","y","z"][1:]




file = open('datasets/divisaosilabica.csv','wb')
file.write(b"palavra,tipo,divisao_silabica\n")

def getNumberPages(letter):
    r = requests.get('http://www.portaldalinguaportuguesa.org/index.php?action=syllables&act=list&letter='+letter)
    soup = BeautifulSoup(r.content,"html.parser")
    paragraphs = soup.findAll("p")
    matched = re.search(r'1 - 100 de (\d+) resultados',str(paragraphs[1].get_text),re.M|re.I)
    quantity = int(matched.group(1))
    return quantity

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


if __name__ == "__main__":   
    main()