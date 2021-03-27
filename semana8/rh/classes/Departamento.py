from rh.classes.Colaborador import Colaborador


class Departamento:
    def __init__(self, nome_setor, nome_responsavel, day, month, year):
        self._nome_setor = nome_setor
        self._responsavel = None
        self._colaboradores = []
        self._nome_responsavel = nome_responsavel
        self._day = day
        self._month = month
        self._year = year
        self.informar_responsavel(self._nome_responsavel, self._day, self._month, self._year)

    @property
    def responsavel(self):
        return self._responsavel._nome_responsavel

    @property
    def nome_setor(self):
        return self._nome_setor

    @nome_setor.setter
    def nome_setor(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is None:
            return None
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, dia, mes, ano):
        self._responsavel = Colaborador(nome, dia, mes, ano)

    def add_colaborador(self, nome, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((colaborador.nome, colaborador.aniversario, self.responsavel, self.nome_setor))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
