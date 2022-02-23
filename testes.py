from ast import Str
from re import S
import unittest
import os
import entrada
import ferramentas_pdf as fp
from pdfminer.layout import LTPage, LTTextBoxHorizontal


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
        dir_anais = os.path.join(os.path.dirname(__file__), 'anais')
        self.caminhos = [os.path.join(
            dir_anais, f'anais_{num}.pdf') for num in range(1, 7)]
        pags_totais = (543, 276, 245, 333, 223, 125)
        self.infos_anais = {caminho: pags for caminho,
                            pags in zip(self.caminhos, pags_totais)}

    def test_contar_pags(self):
        for caminho, pags in self.infos_anais.items():
            self.assertEqual(fp.contar_pags(caminho), pags)

    def test_pegar_pags(self):
        total = fp.pegar_pags(self.caminhos[5], None)
        parcial = fp.pegar_pags(self.caminhos[5], {1, 2, 5, 8, 10})

        self.assertIsInstance(total, tuple)
        for pag in total:
            self.assertIsInstance(pag, LTPage)
        self.assertEqual(len(total), 125)
        self.assertEqual(len(parcial), 5)

    def test_pegar_blocos(self):
        tupla_pags = fp.pegar_pags(self.caminhos[5], {1})
        blocos = fp.pegar_blocos(tupla_pags)

        self.assertIsInstance(blocos, dict)
        for chave, valor in blocos.items():
            self.assertIsInstance(chave, int)
            self.assertEqual(chave, 1)
            self.assertIsInstance(valor, tuple)
            for bloco in valor:
                self.assertIsInstance(bloco, LTTextBoxHorizontal)

    def test_pegar_texto(self):
        tupla_pags = fp.pegar_pags(self.caminhos[5], {1})
        blocos = fp.pegar_blocos(tupla_pags)
        texto = fp.pegar_texto(blocos)

        self.assertIsInstance(texto, dict)
        for chave, valor in texto.items():
            self.assertIsInstance(chave, int)
            self.assertEqual(chave, 1)
            self.assertIsInstance(valor, str)

    def test_extrair(self):
        pass


if __name__ == '__main__':
    unittest.main()
