import unittest
import os
import entrada
import ferramentas_pdf as fp


class TestarEntrada(unittest.TestCase):
    def test_validar_num_anais(self):
        self.valores_falsos = ('7', 'a', '-1', '1.2')

        self.assertTrue(entrada.validar_num_anais('1'))
        for valor in self.valores_falsos:
            self.assertFalse(entrada.validar_num_anais(valor))

    def test_validar_pags(self):
        self.valores_verdadeiros = (
            '',
            '1,1',
            '1,1-2',
            '1',
            '10',
            '1, ',
            ',1',
            '1,2',
            '1 ,2',
            '1,2 ',
            '1-2',
            '1,2-3',
            '1,2-3,',
            '1,2 -3',
            '1,2- 3',
            '1, 2-3',
        )
        self.valores_falsos = (
            ',',
            '-',
            ',,',
            '--',
            ',-',
            '-,',
            'a',
            '1-',
            '1-,2',
            '2-1',
            '1-2-3',
            '1,2-',
            '11',
            '1,2-11',
        )

        for valor in self.valores_verdadeiros:
            self.assertTrue(entrada.validar_pags(valor, 10))
        for valor in self.valores_falsos:
            self.assertFalse(entrada.validar_pags(valor, 10))


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
