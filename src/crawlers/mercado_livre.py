from bs4 import BeautifulSoup
import requests
import csv_handler

csv_items = csv_handler.csv_reader()

for item in csv_items:
    item = '-'.join(item)
    item = str(item).replace(' ', '-')
    item = 'https://lista.mercadolivre.com.br/' + item
    res = requests.get(item)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all('div', {'class': 'ui-search-result__content-wrapper'})
    products = []
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

    csv_handler.csv_writer(csv_items, products)
