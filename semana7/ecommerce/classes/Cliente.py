class Cliente:
    def __init__(self, nome):
        self._nome = nome


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome =  value


    def __str__(self):
        return self._nome


    def __repr__(self):
        return f'Cliente => {self._nome}'
