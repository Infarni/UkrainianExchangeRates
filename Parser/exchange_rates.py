import json
import requests
from bs4 import BeautifulSoup


def get_exchange(currency: str='usd') -> dict:
    '''
        currency = ['usd', 'eur', 'gbp', 'chf']
    '''
    response = requests.get(f'https://minfin.com.ua/ua/currency/cards/{currency}/')
    if response.status_code == 404:
        raise Exception('Currency not found.')

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
    
    return exchanges


def main():
    with open('usd.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(get_exchange('usd'), indent=4))

    with open('eur.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(get_exchange('eur'), indent=4))

    with open('gbp.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(get_exchange('gbp'), indent=4))

    with open('chf.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(get_exchange('chf'), indent=4))


if __name__ == '__main__':
    main()
   