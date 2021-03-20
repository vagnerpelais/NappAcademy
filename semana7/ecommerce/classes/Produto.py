class Produto:
    def __init__(self, *args, **kwargs):
        if kwargs.get('preco', 0) < 0:
            raise ValueError('Preço negativo')
        self._codigo_ean = kwargs.get('ean', '') # Atributos 'privados'
        self._preco = kwargs.get('preco', 0)

    @property #Getter
    def preco(self):
        return self._preco

    @preco.setter #Setter
    def preco(self, value):
        self._preco = value

    def __str__(self):
        """Ao printar o objeto, o código ean será exibido"""
        return self._codigo_ean

    def __repr__(self):
        """Representação do objeto"""
        return f'Produto: {self._codigo_ean}'

    