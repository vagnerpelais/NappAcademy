def calculo_porcentagem_entre_0_e_1(valor, porcentagem):
    if porcentagem < 0 or porcentagem > 1:
        raise ValueError("Porcentagem precisa estar entre 0 e 1")
    return valor * porcentagem
