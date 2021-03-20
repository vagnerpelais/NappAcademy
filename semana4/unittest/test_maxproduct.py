import unittest
from maxproduct import max_product


class MaxProductTestCase(unittest.TestCase):
    def test_maxproduct_cenario_1(self):
        self.assertEqual(10, max_product(1, 2, 5, 0))
        self.assertNotEqual(20, max_product(1, 2, 5, 0))

    def test__maxproduct_cenario_2(self):
        self.assertEqual(50, max_product(1, 2, 5, 10))

    def test__maxproduct_cenario_3(self):
        self.assertEqual(200, max_product(2, 5, 10, 9, 8, 20))

    def test__maxproduct_error_cenario_1(self):
        with self.assertRaises(ValueError):
            max_product(2, 5, 'a', 9, 8, 20)

    def test__maxproduct_error_cenario_2(self):
        with self.assertRaises(IndexError):
            max_product(2)

    def test__maxproduct_error_cenario_3(self):
        self.assertEqual(200, max_product(2, 5, '10', 9, 8, 20))

if __name__ == '__main__':
    unittest.main()
