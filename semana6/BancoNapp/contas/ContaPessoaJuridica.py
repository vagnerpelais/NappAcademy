from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.empresa = kwargs.get('empresa', '')
        self.limite = kwargs.get('limite', 1500)

    def deposito(self, valor):
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo += valor
            self.extrato.append(('D', valor))
            return
        else:
            raise TypeError('O depósito precisa ser numérico')

    def saque(self, valor):
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            self.saldo -= valor
            self.extrato.append(('S', valor))
            return valor
        else:
            raise TypeError('O valor do saque precisa ser numérico')

    def get_extrato(self):
        return self.extrato
