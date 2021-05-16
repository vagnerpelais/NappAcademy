import csv

def abre_csv(filePath):
    lista = []
    anos = set()
    retorno = []
    with open(filePath, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            anos.add(row[0])
            lista.append(row)

        retorno.append(anos)
        retorno.append(lista)
        return retorno


def cria_csv(param):
    anos = list(param[0])
    for ano in anos:
        for row in param[1]:
            if ano == row[0]:
                with open(f'eleicao_{ano}.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(row)
        print(f'Arquivo do ano de {ano} gerado com sucesso!')
    print("Terminou!")


if __name__ == "__main__":
    arquivo = "candidatura.csv"
    open_csv = abre_csv(arquivo)
    cria_csv(open_csv)
