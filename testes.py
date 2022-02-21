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

    def test_contar_pags(self):
        self.assertEqual(fp.contar_pags(os.path.join(
            self.diretorio_anais, 'anais_1.pdf')), 543)
        self.assertEqual(fp.contar_pags(os.path.join(
            self.diretorio_anais, 'anais_2.pdf')), 276)
        self.assertEqual(fp.contar_pags(os.path.join(
            self.diretorio_anais, 'anais_3.pdf')), 245)
        self.assertEqual(fp.contar_pags(os.path.join(
            self.diretorio_anais, 'anais_4.pdf')), 333)
        self.assertEqual(fp.contar_pags(os.path.join(
            self.diretorio_anais, 'anais_5.pdf')), 223)
        self.assertEqual(fp.contar_pags(os.path.join(
            self.diretorio_anais, 'anais_6.pdf')), 125)

    def test_pegar_pags(self):
        self.caminho = os.path.join(
            self.diretorio_anais, 'anais_6.pdf')
        self.assertIsInstance(fp.pegar_pags(self.caminho, None), tuple)
        self.assertEqual(len(fp.pegar_pags(self.caminho, None)), 125)
        self.assertEqual(len(fp.pegar_pags(self.caminho, {1, 2, 5, 8, 10})), 5)


if __name__ == '__main__':
    unittest.main()
