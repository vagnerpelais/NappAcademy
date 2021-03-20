def calculo_porcentagem_entre_0_e_100(valor, porcentagem):
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("Porcentagem precisa estar entre 0 e 100")
    porcentagem = porcentagem / 100
    return valor * porcentagem
