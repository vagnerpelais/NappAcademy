import pytest
from imc import IMC


class TestIMC:
    def test_imc_cenario_1(self):
        pessoa = IMC()
        assert pessoa.peso == 80
        assert pessoa.altura == 1.65
        assert pessoa.imc == pytest.approx(29.38, 0.1)
        assert pessoa.calculo() == pytest.approx(29.38, 0.1)

    def test_imc_cenario_2(self):
        pessoa = IMC(100)
        assert pessoa.peso == 100
        assert pessoa.altura == 1.65
        assert pessoa.imc == pytest.approx(36.73, 0.1)

    def test_imc_cenario_3(self):
        pessoa = IMC(100, 1.82)
        assert pessoa.peso == 100
        assert pessoa.altura == 1.82
        assert pessoa.imc == pytest.approx(30.18, 0.001)

    def test_wrong_cenario_1(self):
        """ Altura maior que o limite """
        with pytest.raises(ValueError) as error:
            pessoa = IMC(100, 20.82)
        assert str(error.value) == 'Altura acima do permitido'

    def test_wrong_cenario_2(self):
        """ Peso maior que o limite """
        with pytest.raises(ValueError) as error:
            pessoa = IMC(200, 1.82)
        assert str(error.value) == 'Peso acima do permitido'
