import unittest
import entrada


class TestarEntrada(unittest.TestCase):

    def test_validar_num_anais(self):
        self.assertTrue(entrada.validar_num_anais('1'))
        self.assertFalse(entrada.validar_num_anais('7'))
        self.assertFalse(entrada.validar_num_anais('a'))
        self.assertFalse(entrada.validar_num_anais('-1'))
        self.assertFalse(entrada.validar_num_anais('1.2'))


if __name__ == '__main__':
    unittest.main()
