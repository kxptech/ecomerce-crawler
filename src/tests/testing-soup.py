from bs4 import BeautifulSoup
import requests
from src.modules import csv_handler

res = requests.get('https://lista.mercadolivre.com.br/botas')
soup = BeautifulSoup(res.text, 'html.parser')

# items = soup.find_all('div', {'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated'})

items = soup.find_all('div', {'class': 'ui-search-result__image'})

for i in range(len(items)):
    for link in soup.find_all('a', {'class': 'ui-search-link'}):
        if (str(link.get('title')) != 'None') and ('ui-search-result__content' in link['class']):
            # print(link.attrs)
            print(link.get('title'))
            print(link.get('href'))

#     for a in soup.find_all('a', href=True, text=True):
#         link_text = a['href']
#     print('Link: ' + str(i) + ' ' + link_text)

# for aux in items:
#     aux2 = aux.find_all('a', href=True, text=True)
#     # link = aux2['href']
#     print(aux2)


# for i in range(len(items)):
#     for a in soup.find_all('a', href=True, text=True):
#         link_text = a['href']
#     print('Link: ' + str(i) + ' ' + link_text)

# for i in range(len(items)):
#     soup = BeautifulSoup(str(items[i]), 'html.parser')
#     link_text = ''
#     for a in soup.find_all('a', href=True, text=True):
#         link_text = a['href']
#
#     print('Link: ' + str(i) + ' ' + link_text)

# links = soup.find_all('a', href=True)
#
# print(links)

# ui-search-link
