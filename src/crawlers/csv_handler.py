import csv


def csv_reader():
    with open("../../archives/Entrada.CSV", "r") as csv_file:
        csv_items = csv.reader(csv_file, delimiter=',')
    return csv_items


def csv_writer(items, products):
    for i in range(items):
        with open('Saída ' + str(i + 1), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["PRODUTO", "VALOR"])
            writer.writerow(products[i])
