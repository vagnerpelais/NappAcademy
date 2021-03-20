def juros_compostos(valor_inicial, juros, tempo):
    if type(valor_inicial) == str or type(juros) == str or type(tempo) == str:
        raise TypeError('Insira apenas números!!')

    juros = juros/100
    valor_final = valor_inicial * (1+juros)**tempo
    return round(valor_final, 2)

