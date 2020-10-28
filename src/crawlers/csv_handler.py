def csv_reader():
    with open("../../archives/Entrada.CSV", "r") as readed_csv_file:
        csv_items = csv.reader(readed_csv_file, delimiter=',')

