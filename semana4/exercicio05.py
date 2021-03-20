import csv
from datetime import date, datetime


def find_born_monday(lista):
    list = []
    for person in lista:
        if person[-2] == 'birthdate':
            continue

        data = datetime.strptime(person[-2], '%Y-%m-%d').date()

        if data.weekday() == 0:
            list.append(person[0])

    return list


def carregar_arquivo(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    nascidos_segunda_feira = find_born_monday(lista)
    for item in nascidos_segunda_feira:
        print(item)
