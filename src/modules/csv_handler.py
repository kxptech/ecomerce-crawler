import csv


def csv_reader():
    with open("../../archives/Entrada.CSV", "r") as csv_file:
        csv_items = csv.reader(csv_file, delimiter=',')
        items = []
        for item in csv_items:
            items.append(item)
        return items


def csv_writer(products, indice):
    with open('Saída ' + str(indice) + '.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(len(products)):
            writer.writerow(products[i])
