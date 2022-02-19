import unittest
import entrada


class TestarEntrada(unittest.TestCase):
    def setUp(self):
        self.pags_totais = 10

    def test_validar_num_anais(self):
        self.assertTrue(entrada.validar_num_anais('1'))
        self.assertFalse(entrada.validar_num_anais('7'))
        self.assertFalse(entrada.validar_num_anais('a'))
        self.assertFalse(entrada.validar_num_anais('-1'))
        self.assertFalse(entrada.validar_num_anais('1.2'))

    def test_validar_pags(self):
        self.assertFalse(entrada.validar_pags('', self.pags_totais))
        self.assertFalse(entrada.validar_pags('a', self.pags_totais))
        self.assertFalse(entrada.validar_pags(',', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1-,2', self.pags_totais))
        self.assertFalse(entrada.validar_pags('2-1', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1-2-3', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1,2-', self.pags_totais))
        self.assertFalse(entrada.validar_pags('12', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1,2-12', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,1', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,1-2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1, ', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,', self.pags_totais))
        self.assertTrue(entrada.validar_pags(',1', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1, 2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,2 ', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1 ,2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1 , 2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1-2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,2-3', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,2-3,', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,2 -3', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,2- 3', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1, 2-3', self.pags_totais))


if __name__ == '__main__':
    unittest.main()
