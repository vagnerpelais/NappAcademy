from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nome = kwargs.get('nome', '')
        self.profissao = kwargs.get('profissao', '')
        self.limite = kwargs.get('limite', 0)

    def deposito(self, valor):
        if isinstance(valor, (int, float)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo += valor
            self.extrato.append(('D', valor))
        else:
            raise TypeError('O depósito precisa ser numérico')

    def saque(self, valor):
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo.')
                return
            self.saldo -= valor
            self.extrato.append(('S', valor))
            return valor
        else:
            raise TypeError('O valor do saque precisa ser numérico')

    def get_extrato(self):
        return self.extrato

    def rendimento_aniversario(self, juros):
        if isinstance(juros, (float, int)):
            if juros < 0 or juros > 1.0:
                raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')

            self.saldo = self.saldo + (self.saldo * juros)
