import unittest
import os
import entrada
import ferramentas_pdf as fp


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
        self.assertFalse(entrada.validar_pags(',,', self.pags_totais))
        self.assertFalse(entrada.validar_pags('--', self.pags_totais))
        self.assertFalse(entrada.validar_pags(',-', self.pags_totais))
        self.assertFalse(entrada.validar_pags('a', self.pags_totais))
        self.assertFalse(entrada.validar_pags(',', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1-,2', self.pags_totais))
        self.assertFalse(entrada.validar_pags('2-1', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1-2-3', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1,2-', self.pags_totais))
        self.assertFalse(entrada.validar_pags('11', self.pags_totais))
        self.assertFalse(entrada.validar_pags('1,2-11', self.pags_totais))
        self.assertTrue(entrada.validar_pags('', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,1', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1,1-2', self.pags_totais))
        self.assertTrue(entrada.validar_pags('1', self.pags_totais))
        self.assertTrue(entrada.validar_pags('10', self.pags_totais))
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


class TestarFerramentasPDF(unittest.TestCase):
    def setUp(self):
        self.diretorio_anais = os.path.join(os.path.dirname(__file__), 'anais')
        self.caminhos = {num: os.path.join(
            self.diretorio_anais, f'anais_{num}.pdf') for num in range(1, 7)}

    def test_contar_pags(self):
        self.assertEqual(fp.contar_pags(self.caminhos[1]), 543)
        self.assertEqual(fp.contar_pags(self.caminhos[2]), 276)
        self.assertEqual(fp.contar_pags(self.caminhos[3]), 245)
        self.assertEqual(fp.contar_pags(self.caminhos[4]), 333)
        self.assertEqual(fp.contar_pags(self.caminhos[5]), 223)
        self.assertEqual(fp.contar_pags(self.caminhos[6]), 125)

    def test_pegar_pags(self):
        self.total = fp.pegar_pags(self.caminhos[6], None)
        self.assertIsInstance(self.total, tuple)
        self.assertEqual(len(self.total), 125)
        self.parcial = fp.pegar_pags(self.caminhos[6], {1, 2, 5, 8, 10})
        self.assertEqual(len(self.parcial), 5)


if __name__ == '__main__':
    unittest.main()
