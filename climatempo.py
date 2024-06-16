from datetime import datetime
from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/1443/saojose-sc").content

soup = BeautifulSoup(html, 'html.parser') 

temperaturaMinima = soup.find(id='min-temp-1')  
temperaturaMaxima = soup.find(id='max-temp-1')

print('Data: ' + datetime.now().date().strftime("%d/%m/%Y"))
print('Temperatura Mínima: '+ temperaturaMinima.string)
print('Temperatura Máxima: ' + temperaturaMaxima.get_text())

