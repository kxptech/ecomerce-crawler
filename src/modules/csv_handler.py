import pandas as pd
import csv


def csv_reader():
    df = pd.read_csv("../../archives/Entrada.CSV")
    return df


def csv_writer(products, indice):
    with open('Saída ' + str(indice) + '.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(len(products)):
            writer.writerow(products[i])
