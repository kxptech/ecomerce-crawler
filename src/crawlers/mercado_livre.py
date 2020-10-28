from bs4 import BeautifulSoup
import requests
import csv

aux = 0
csv_exit = []

with open("../../archives/Entrada.CSV", "r") as arquivo_csv:
    csv_items = csv.reader(arquivo_csv, delimiter=',')
    for item in csv_items:
        item = '-'.join(item)
        item = str(item).replace(' ', '-')
        item = 'https://lista.mercadolivre.com.br/' + item
        res = requests.get(item)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.find_all('div', {'class': 'ui-search-result__content-wrapper'})

        csv_exit.append('Saída' + str(aux) + '.csv')
        with open(csv_exit[aux], 'w', newline='') as file:

            writer = csv.writer(file)

            writer.writerow(["Produto", "Valor"])

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
                writer.writerow([title, full_price])

            aux = aux + 1