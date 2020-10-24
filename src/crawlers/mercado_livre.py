from bs4 import BeautifulSoup
import requests
import csv

with open("entrada.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')
    for coluna in leitor:
        print(coluna)

res = requests.get('https://lista.mercadolivre.com.br/botas')
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('div', {'class': 'ui-search-result__content-wrapper'})

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

    print(title, full_price)
