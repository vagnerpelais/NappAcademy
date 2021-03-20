from massa_dados_situacao_teste import lista_pessoas


def lista_simples(list):
     lista = []
     for item in list:
             if type(item[-1]) is tuple:
                     lista.append((item[0], item[-1]))
     return lista


entrada = []
saida_esperada = []
saida = lista_simples(entrada)
assert(saida == saida_esperada)


entrada = 'string'
saida_esperada = []
saida = lista_simples(entrada)
assert(saida == saida_esperada)


if __name__ == "__main__":
     pedaco = slice(0,2)
     entrada = lista_pessoas[pedaco]
     saida_esperada = [('daniellemosley', ('33.93113', '-117.54866')), ('rhodesrichard', ('39.00622', '-77.4286'))]
     saida = lista_simples(entrada)
     assert(saida == saida_esperada)
