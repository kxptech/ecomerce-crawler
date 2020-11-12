import pandas as pd


def csv_reader():
    df = pd.read_csv("../../archives/Entrada.CSV")
    return df


def csv_writer(products, indice):
    df = pd.DataFrame(products, columns=['PRODUTOS', 'VALOR', 'QTDE VENDIDA'])
    df.to_csv(r'../../archives/Saída' + str(indice) + '.csv', index=False)
