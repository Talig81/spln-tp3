from bs4 import BeautifulSoup
import requests
import urllib



#file = open('../data/divisaosilabica.csv','w')
#file.write("palavra,tipo,divisao_silabica\n")


    
    
def main():
    
    r = requests.get('http://www.portaldalinguaportuguesa.org/index.php?action=syllables&act=list&letter=a')
    soup = BeautifulSoup(r.content,"html.parser")
    rows = soup.find(id="rollovertable").findAll("tr")
    stffs = soup.find().findAll("p")
    for s in stffs:
        print("um")

main()