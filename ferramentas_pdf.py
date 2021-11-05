'Ferramentas para extrair texto de PDF.'

from typing import Iterator
from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBoxHorizontal


def pegar_pags(caminho_arquivo: str, numeros: list | None = None) -> Iterator:
    '''
    Extrai páginas de PDF.\n
    Retorna iterator de objetos LTPage.
    '''

    print('Extraindo páginas...')
    # laparams: Parâmetros para análise de layout do documento.
    # Necessário p/ extração correta de blocos de texto.
    laparams = LAParams(word_margin=0.5, line_margin=1, boxes_flow=None)
    pags_ltpage = extract_pages(
        caminho_arquivo, page_numbers=numeros, laparams=laparams)
    print('Páginas extraídas.')
    return pags_ltpage


def pegar_blocos_texto(pags_ltpage: Iterator) -> dict:
    '''
    Extrai blocos de texto.\n
    Retorna dict com pares = número da página (int):
    lista de blocos de texto da página.
    '''

    print("Extraindo blocos de texto...")
    dict_blocos = {}
    num_pag = 0

    for pag in pags_ltpage:
        num_pag += 1
        blocos_pag = []

        for bloco in pag:
            # Garantindo que este bloco contém texto e não img., p. ex.
            if isinstance(bloco, LTTextBoxHorizontal):
                blocos_pag.append(bloco)

        dict_blocos[num_pag] = blocos_pag
        print(f'Blocos da pág. {num_pag} extraídos.')

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
        print(f'Texto da pág. {num_pag} extraído.')

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
