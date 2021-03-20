import unittest
from semana4.exercicio07 import calculo_porcentagem_entre_0_e_100


class CalculoPorcentageTestCase(unittest.TestCase):
    def test_calculoporcentagem_case_1(self):
        self.assertEqual(14, calculo_porcentagem_entre_0_e_100(20, 70))
        self.assertNotEqual(40, calculo_porcentagem_entre_0_e_100(35, 58))

    def test_calculoporcentagem_case_2(self):
        with self.assertRaises(ValueError):
            calculo_porcentagem_entre_0_e_100(60, 103)


if __name__ == '__main__':
    unittest.main()
