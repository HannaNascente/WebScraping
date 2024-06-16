from bs4 import BeautifulSoup

import requests

html = requests.get("https://imoveisgodoy.com.br/5-melhores-bairros-para-morar-em-santa-catarina/").content

soup = BeautifulSoup(html, 'html.parser')

melhoresBairros = soup.findAll("h3", class_='wp-block-heading')

for bairro in melhoresBairros:
    print(bairro.get_text())
     