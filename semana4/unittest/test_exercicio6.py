import unittest
from semana4.exercicio06 import calculo_porcentagem_entre_0_e_1


class CalculoporcentagemTestCase(unittest.TestCase):
    def test_calculoporcent_cenario_1(self):
        self.assertEqual(10, calculo_porcentagem_entre_0_e_1(10, 1))
        self.assertNotEqual(10, calculo_porcentagem_entre_0_e_1(4, 1))

    def test_calculoporcent_cenario_2(self):
        with self.assertRaises(ValueError):
            calculo_porcentagem_entre_0_e_1(10, 4)


if __name__ == '__main__':
    unittest.main()
