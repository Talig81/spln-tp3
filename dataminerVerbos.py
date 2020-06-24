from bs4 import BeautifulSoup
import requests
import urllib.request
import re

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","z"]

def listVerbs():
    verbList = set()
    for letter in abc:
        with open('datasets/divisaosilabica_'+letter+'.csv', 'rb') as f:
            for line in f:
                line = line.decode()
                matched = re.search(r'(\w+), \(verbo\)(.*)',line, re.I)
                if matched is None:
                    continue
                verbList.add(matched.group(1))
    return list(verbList)

def addVerbos(verbList):
    for verb in verbList:
        print(verb)
        response = urllib.request.urlopen(f'https://conjuga-me.net/verbo-'+verb)
        

def main():
     verbList = listVerbs()
     addVerbos(verbList)

if __name__ == "__main__":   
    main()