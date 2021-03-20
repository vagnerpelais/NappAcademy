import pytest
from imc import IMC


class TestIMC2:
    obesos = [
        (90, 1.66, 32.66),
        (100, 1.65, 36.73),
        (100, 1.82, 30.18),
    ]

    @pytest.mark.parametrize("peso, altura, imc", obesos)
    def test_imc_cenarios_obesos(self, peso, altura, imc):
        pessoa = IMC(peso, altura)
        assert pessoa.peso == peso
        assert pessoa.altura == altura
        assert pessoa.imc == pytest.approx(imc, 0.1)
        assert pessoa.calculo() == pytest.approx(imc, 0.1)

    normal = [
        (70, 1.76, 24.22),
        (72.5, 1.75, 23.94),
        (67.0, 1.64, 24.98),
        (78.0, 1.64, 29.00),
    ]

    @pytest.mark.parametrize("peso, altura, imc", normal)
    def test_imc_cenarios_normal(self, peso, altura, imc):
        pessoa = IMC(peso, altura)
        assert pessoa.peso == peso
        assert pessoa.altura == altura
        assert pessoa.imc == pytest.approx(imc, 0.1)
        assert pessoa.calculo() == pytest.approx(imc, 0.1)

    pessoas = [
        (50, 1.70, 'abaixo do peso'),
        (60, 1.70, 'peso normal'),
        (79, 1.70, 'sobrepeso'),
        (99, 1.70, 'Obesidade I'),
        (109, 1.70, 'Obesidade II'),
        (129, 1.70, 'Obesidade III'),
    ]

    @pytest.mark.parametrize("peso, altura, situacao", pessoas)
    def test_cenarios_situacao(self, peso, altura, situacao):
        pessoa = IMC(peso, altura)
        assert pessoa.situacao() == situacao
