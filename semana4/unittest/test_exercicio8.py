import unittest
from semana4.exercicio08 import juros_compostos


class JurosCompostosTestCase(unittest.TestCase):
    def test_juroscompsotos_case_1(self):
        self.assertEqual(11290256.02, juros_compostos(16000, 30, 25))
        self.assertNotEqual(543434.22, juros_compostos(233, 2, 13))

    def test_juroscompostos_case_2(self):
        with self.assertRaises(TypeError):
            juros_compostos(100, 2, 'a')


if __name__ == '__main__':
    unittest.main()
