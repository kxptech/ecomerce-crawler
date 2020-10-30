import csv


def csv_reader():
    with open("../../archives/Entrada.CSV", "r") as csv_file:
        csv_items = csv.reader(csv_file, delimiter=',')
        items = []
        for item in csv_items:
            items.append(item)
        return items


def csv_writer(items, products):
    for i in range(len(items)):
        with open('Saída ' + str(i + 1) + '.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            if i == 0:
                writer.writerow(["PRODUTO", "VALOR"])
            writer.writerow(products[i])
