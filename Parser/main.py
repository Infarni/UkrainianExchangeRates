import json
import requests
from bs4 import BeautifulSoup


response = requests.get('https://minfin.com.ua/ua/currency/cards/')

soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('tr', class_='row--collapse')[7:]

exchanges = []

for item in items:
    name = item.find('td', class_='mfcur-table-bankname').text
    purchase = item.find('td', class_='mfm-text-right').text
    sale = item.find('td', class_='mfm-text-left').text
    
    if purchase == '0.000 ' and sale == '0.000 ':
        continue
    
    time = item.find('td', class_='mfcur-table-refreshtime').text
    
    exchanges.append(
        {
            'name': name.replace('\n', '').strip(),
            'purchase': purchase,
            'sale': sale,
            'time': time
        }
    )

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(exchanges, indent=4))
   