from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from urllib.parse import quote

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","z"]

def listVerbs():
    verbList = set()
    for letter in abc:
        with open('datasets/divisaosilabica_'+letter+'.csv', 'rb') as f:
            with open('datasets/verbos_'+letter+'.txt', 'wb') as f2:
                for line in f:
                    line = line.decode()
                    matched = re.search(r'(\w+), \(verbo\)(.*)',line, re.I)
                    if matched is None:
                        continue
                    getVerbConjugado(matched.group(1),f2)

    return list(sorted(verbList))

def getVerbConjugado(verb,f2):
    verbs = []
    response = urllib.request.urlopen(f'https://conjuga-me.net/verbo-' + quote(verb))
    soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'), features="html.parser")
    if soup.find('div',{'class':'conjugation-header'}):
        for tag in soup.findAll('div',{'class':'conjugation'}):
                f2.write(tag.getText().encode())
                f2.write(b", (verbo), -\n")
                

        

def main():
     verbList = listVerbs()


if __name__ == "__main__":   
    main()