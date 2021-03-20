def max_product(*args):
    """
    Função que retorna o produto máximo entre dois elementos enviados
    via *args

    Returns:
        *args: Conjunto de parâmetros
    """
    lista = list(args)
    lista = [float(numero) for numero in lista]
    lista.sort(reverse=True)
    return lista[0] * lista[1]
