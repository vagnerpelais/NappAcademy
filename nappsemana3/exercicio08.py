import csv


def find_subtring_credit_card(lista, parametro='322'):
    list = []
    for item in lista:
        if parametro in item["credit_card"]:
            list.append(item["name"])
    return list


def find_start_subtring_credit_card(lista, parametro='303'):
    list = []
    for item in lista:
        if item["credit_card"].startswith(parametro):
            list.append(item["name"])
    return list


def carregar_arquivo(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list
