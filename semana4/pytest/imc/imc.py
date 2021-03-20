class IMC:
    """
    Cálculo do IMC baseado em OO
    """
    def __init__(self, peso=80, altura=1.65):
        """
        Construtor de objetos IMC para cálculo do IMC de cada objeto.

        Args:
            peso (int, optional): Peso da pessoa. Padrão 80.
            altura (float, optional): Altura da pesso. Padrão 1.65.
        """
        if altura > 2.2:
            raise ValueError('Altura acima do permitido')
        if altura < 0.3:
            raise ValueError('Altura abaixo do permitido')
        if peso > 180:
            raise ValueError('Peso acima do permitido')
        self.peso = peso
        self.altura = altura
        self.imc = self.calculo()

    def calculo(self):
        """
        Método para cálculo do IMC
        """
        return self.peso / (self.altura * self.altura)

    def situacao(self):
        """
        A partir do IMC calculado, este método retorna a situação
        da pessoa conforme o IMC:
        Abaixo do peso\t\tabaixo 18,5
        Peso normal\t\tentre 18,5  e  24,9
        Sobrepeso\t\tentre 25,0  e  29,9
        Obesidade grau I\tentre 30,0  e  34,9
        Obesidade grau II\tentre 35,0  e  39,9
        Obesidade grau III\tmaior 40

        Returns:
            string: Situação da pessoa
        """
        if self.imc <= 18.5:
            return 'abaixo do peso'
        elif self.imc < 24.9:
            return "peso normal"
        elif self.imc < 29.9:
            return "sobrepeso"
        elif self.imc < 34.9:
            return "Obesidade I"
        elif self.imc < 39.9:
            return "Obesidade II"
        else:
            return "Obesidade III"
