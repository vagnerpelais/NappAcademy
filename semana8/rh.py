from rh.classes.Departamento import Departamento

from datetime import date, timedelta
dt1 = date.today() - timedelta(days=4)
hoje = date.today()

departamento = Departamento('Departamento XYZ', 'Vagner', hoje.day, hoje.month, 2021)
departamento.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
departamento.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
departamento.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
departamento.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1985)

aniversariantes = departamento.verificar_aniversariantes()

for aniversariante in aniversariantes:
    print(f'Parabéns {aniversariante[0]} do departamento {aniversariante[3]} pelo seu dia! O responsável pelo departamento é {aniversariante[2]}')
