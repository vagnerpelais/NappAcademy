import pytest
import sys
from imc import IMC


def test_imc_cenario_1():
    pessoa = IMC()
    assert pessoa.peso == 80
    assert pessoa.altura == 1.65
    assert pessoa.imc == pytest.approx(29.38, 0.1)
    assert pessoa.calculo() == pytest.approx(29.38, 0.1)


def test_imc_cenario_2():
    pessoa = IMC(100)
    assert pessoa.peso == 100
    assert pessoa.altura == 1.65
    assert pessoa.imc == pytest.approx(36.73, 0.1)


def test_imc_cenario_3():
    pessoa = IMC(100, 1.82)
    assert pessoa.peso == 100
    assert pessoa.altura == 1.82
    assert pessoa.imc == pytest.approx(30.18, 0.001)


@pytest.mark.skip(reason="Não implementado ainda")
def test_wrong_cenario_1():
    """ Altura maior que o limite """
    with pytest.raises(ValueError) as error:
        pessoa = IMC(100, 20.82)
    assert str(error.value) == 'Altura acima do permitido'


@pytest.mark.skip(reason="Não implementado ainda")
def test_wrong_cenario_3():
    """ Altura menor que o limite """
    with pytest.raises(ValueError) as error:
        pessoa = IMC(100, 0.29)
    assert str(error.value) == 'Altura abaixo do permitido'


@pytest.mark.skip(reason="Não implementado ainda")
def test_wrong_cenario_2():
    """ Peso maior que o limite """
    with pytest.raises(ValueError) as error:
        pessoa = IMC(200, 1.82)
    assert str(error.value) == 'Peso acima do permitido'


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Update your python env")
def test_version_on_dev():
    """ Testar a versão atual do Python """
    assert sys.version_info.major == 3
    assert sys.version_info.minor >= 8


@pytest.mark.xfail(sys.platform == 'linux', reason="Don't run on Linux ")
def test_don_t_run_on_linux():
    assert 1 == 1
