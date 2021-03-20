lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
lista_nova = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]


def extrair_novos_registros(OldList, NewList):
     list = []
     for item in NewList:
             if item not in OldList:
                     list.append([item])
     return list





if __name__ == "__main__":
    lista_novos_registros = extrair_novos_registros(lista_antiga, lista_nova)
    print(lista_novos_registros)
