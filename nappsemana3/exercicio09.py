import csv


def carregar_arquivo(path):
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


class CardNumber:

    def find_subtring_credit_card(self, lista, params):
        list = []
        for item in lista:
            if params in item["credit_card"]:
                list.append(item["name"])
        return list


    def find_start_subtring_credit_card(self, lista, params):
        list = []
        for item in lista:
            if item["credit_card"].startswith(params):
                list.append(item["name"])
        return list


if __name__ == "__main__":
    lista = carregar_arquivo('usernames.csv')
    listObj = CardNumber()
    print(listObj.find_subtring_credit_card(lista, '222'))
    print(listObj.find_start_subtring_credit_card(lista, '303'))


