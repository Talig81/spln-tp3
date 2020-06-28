import re

import requests
from bs4 import BeautifulSoup


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
    return (esquemaMetrica,silabas)

funcaoSilabas("palavra\nmacabra")