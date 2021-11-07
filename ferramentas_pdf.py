'Ferramentas para extrair texto de PDF.'

from typing import Iterator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1
from pdfminer.high_level import extract_pages


def pegar_pags(caminho_arquivo: str, numeros: list | None = None) -> tuple:
    '''
    Extrai páginas de PDF.\n
    Retorna tupla de objetos LTPage.
    '''
    with open(caminho_arquivo, 'rb') as arquivo:
        analisador = PDFParser(arquivo)
        documento = PDFDocument(analisador)
        total_paginas = resolve1(documento.catalog['Pages'])['Count'] - 1

        assert not numeros or numeros and not any(
            [numero > total_paginas for numero in numeros])

    print('Extraindo páginas...')
    # laparams: Parâmetros para análise de layout do documento.
    # Necessário p/ extração correta de blocos de texto.
    laparams = LAParams(word_margin=0.5, line_margin=1, boxes_flow=None)
    iterator_pags = extract_pages(
        caminho_arquivo, page_numbers=numeros, laparams=laparams)

    tupla_pags = ()
    for numero, pagina in enumerate(iterator_pags, start=1):
        print(f"Página {numero} extraída.")
        tupla_pags += (pagina,)

    print('Páginas extraídas.')
    return tupla_pags


def pegar_blocos_texto(tupla_pags: tuple) -> dict:
    '''
    Extrai blocos de texto.\n
    Retorna dict com pares = número da página (int):
    lista de blocos de texto da página.
    '''

    print("Extraindo blocos de texto...")
    dict_blocos = {}
    num_pag = 0

    for pag in tupla_pags:
        num_pag += 1
        blocos_pag = []

        for bloco in pag:
            # Garantindo que este bloco contém texto e não img., p. ex.
            if isinstance(bloco, LTTextBoxHorizontal):
                blocos_pag.append(bloco)

        dict_blocos[num_pag] = blocos_pag
        print(f'Blocos da página {num_pag} extraídos.')

    print('Blocos de texto extraídos.')
    return dict_blocos


def pegar_texto(dict_blocos: dict) -> dict:
    '''
    Extrai texto de blocos de texto.\n
    Retorna dict com pares = número da página (int): texto da página (str).    
    '''

    print('Extraindo texto...')
    dict_texto = {}

    for num_pag in dict_blocos:
        texto_pag = ''

        for bloco in dict_blocos[num_pag]:
            texto_bloco = bloco.get_text()
            texto_pag += f'\n{texto_bloco}\n'

        dict_texto[num_pag] = texto_pag
        print(f'Texto da página {num_pag} extraído.')

    print('Texto completo extraído.')
    return dict_texto


def extrair(caminho_arquivo: str, numeros: list) -> dict:
    '''
    Processo completo de extração de texto do PDF.\n
    Realiza pegar_pags, pegar_blocos_texto e pegar_texto.\n
    Retorna dict com pares = número da página: texto da página.
    '''

    pags_ltpage = pegar_pags(caminho_arquivo, numeros)
    dict_blocos = pegar_blocos_texto(pags_ltpage)
    texto_pags = pegar_texto(dict_blocos)
    return texto_pags
