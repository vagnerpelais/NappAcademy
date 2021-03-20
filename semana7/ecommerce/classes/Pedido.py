from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Produto import Produto

class Pedido:
    formas_aceitas = ['dinheiro', 'cartão', 'pix']
    def __init__(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente
            self._itens = []
            return
        raise TypeError('Não é possível instanciar um pedido sem um cliente')


    @property
    def cliente(self):
        return self._cliente


    @property
    def itens(self):
        return self._itens

    
    @itens.setter
    def itens(self, value):
        self._itens = value


    def __str__(self):
        return f'Pedido de {str(self.cliente)}'

    
    def __repr__(self):
        return f'Pedido de {str(self.cliente)}'


    def add_item(self, produto):
        if isinstance(produto, Produto):
            self.itens.append(produto)
            return
        raise TypeError('Não foi passado um objeto produto')

    
    def quantidade_produto_no_pedido(self, ean):
        quantidade = 0
        for produto in self.itens:
            if produto.ean == ean:
                quantidade += 1
        return quantidade

    
    def nota_fiscal(self):
        nota_produtos = []
        set_produtos = []
        for item in self.itens:
            set_produtos.append(str(item))
        set_produtos = set(set_produtos)
        for produto in set_produtos:
            quantidade = self.quantidade_produto_no_pedido(str(produto))
            nota_produtos.append((produto, quantidade))
        return nota_produtos

    
    def valor_total_pagar(self):
        total_pagar = 0
        for produto in self.itens:
            total_pagar = total_pagar + produto.preco
        return total_pagar

    def checkout(self, forma_de_pagamento=None):
        if forma_de_pagamento is None:
            raise Exception('Informe um meio de pagamento')
        if forma_de_pagamento.lower() in self.__class__.formas_aceitas:
            dados_checkout = (self.nota_fiscal(), self.valor_total_pagar())
            return dados_checkout
        raise Exception('Forma de pagamento não aceita')

    