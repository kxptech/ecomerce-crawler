from bs4 import BeautifulSoup
import requests
from src.modules import csv_handler

csv_items = csv_handler.csv_reader()

indice = 1

for item in csv_items['Produtos']:
    #item = '-'.join(item)
    print(item)
    item = str(item).replace(' ', '-')
    print(item)
    item = 'https://lista.mercadolivre.com.br/' + item
    res = requests.get(item)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('div', {'class': 'ui-search-result__content-wrapper'})
    products = []
    products.append(['PRODUTOS', 'VALOR'])
    for i in range(len(items)):
        item_to_be_parsed = BeautifulSoup(str(items[i]), 'html.parser')
        title = item_to_be_parsed.find(
            'h2', 'ui-search-item__title').text
        price_fraction = item_to_be_parsed.find('span', 'price-tag-fraction').text

        try:
            price_cents = item_to_be_parsed.find(
                'span', 'price-tag-cents').text
        except:
            price_cents = 0

        full_price = 'R$ {},{}'.format(price_fraction, price_cents)

        products.append([title, full_price])

    csv_handler.csv_writer(products, indice)
    indice += 1
