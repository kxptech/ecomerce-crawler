import threading
from src.modules import mercado_livre
from src.modules import csv_handler

def soup_mercado_livre(csv_items):
    df = mercado_livre.crawler_mercado_livre(csv_items)

csv_items = csv_handler.csv_reader()

