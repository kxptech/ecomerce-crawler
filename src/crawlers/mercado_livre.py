from bs4 import BeautifulSoup
import requests
from src.modules import csv_handler
from multiprocessing import Pool
import time


def executeProcess(link):
    res = requests.get(link)
    item_to_be_parsed = BeautifulSoup(res.text, 'html.parser')
    title = item_to_be_parsed.find('h1', 'ui-pdp-title').text

    square_to_be_parsed = item_to_be_parsed.find('div', 'ui-pdp-price__second-line')

    price_fraction = square_to_be_parsed.find('span', 'price-tag-fraction').text

    try:
        price_cents = square_to_be_parsed.find('span', 'price-tag-cents').text
    except:
        price_cents = '00'

    try:
        numb_solds = item_to_be_parsed.find('span', 'ui-pdp-subtitle').text
        if (numb_solds != 'Novo'):
            numb_solds = numb_solds.join(numb for numb in numb_solds.split() if numb.isdigit())
        else:
            numb_solds = '0'
    except:
        numb_solds = '0'

    numb_solds = int(numb_solds)
    full_price = price_fraction + '.' + price_cents
    full_price = float(full_price)

    return [title, full_price, numb_solds]


if __name__ == '__main__':
    csv_items = csv_handler.csv_reader()

    indice = 1

    t0 = time.time()

    for item in csv_items['Produtos']:

        threads = []
        links = []

        item = str(item).replace(' ', '-')
        item = 'https://lista.mercadolivre.com.br/' + item
        res = requests.get(item)
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.find_all('div', {'class': 'ui-search-result__image'})

        for i in range(len(items)):
            for link in soup.find_all('a', {'class': 'ui-search-link'}):
                if (str(link.get('title')) != 'None') and (('ui-search-result__content' in link['class']) or
                                                           ('ui-search-item__group__element' in link['class'])):
                    links.append(link.get('href'))

        links = set(links)

        p = Pool(processes=10)
        products = p.map(executeProcess, links)
        p.close()

        csv_handler.csv_writer(products, indice)
        indice += 1

    t1 = time.time()
    totalTime = t1 - t0
    print(totalTime)