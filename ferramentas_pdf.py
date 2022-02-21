'Ferramentas para extrair texto de PDF.'

from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import resolve1
from pdfminer.high_level import extract_pages


def contar_pags(caminho_arquivo: str) -> int:
    with open(caminho_arquivo, 'rb') as arquivo:
        analisador = PDFParser(arquivo)
        documento = PDFDocument(analisador)
        return resolve1(documento.catalog['Pages'])['Count']


def pegar_pags(caminho: str, paginas: set | None = None) -> tuple:
    '''
    Extrai páginas de PDF.\n
    Retorna tupla de objetos LTPage.
    '''

    print('Extraindo páginas...')
    # Parâmetros para análise de layout do documento
    laparams = LAParams(char_margin=10, word_margin=0.5,
                        line_margin=1, boxes_flow=None)
    iter_pags = extract_pages(caminho, page_numbers=paginas, laparams=laparams)
    tupla_pags = ()
    for numero, pagina in enumerate(iter_pags, start=1):
        print(f"Página {numero} extraída.")
        tupla_pags += pagina,

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

    for num, pag in enumerate(tupla_pags):
        # Adiciona bloco à lista se ele contiver texto e não, p. ex., imagem
        blocos_pag = [bloco for bloco in pag if isinstance(
            bloco, LTTextBoxHorizontal)]
        dict_blocos[num] = blocos_pag
        print(f'Blocos da página {num} extraídos.')

    print('Blocos de texto extraídos.')
    return dict_blocos


def pegar_texto(dict_blocos: dict) -> dict:
    '''
    Extrai texto de blocos de texto.\n
    Retorna dict com pares = número da página (int): texto da página (str).    
    '''

    print('Extraindo texto...')
    dict_texto = {}

    for num_pag, blocos in dict_blocos.items():
        texto_pag = '\n'.join([bloco.get_text() for bloco in blocos])
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
    return pegar_texto(dict_blocos)
