import re
from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBoxHorizontal


# Extrai págs. de .pdf. Arg.: caminho p/ arquivo
def get_pages(file_path):
    # Parâmetros para análise de layout. Necessário p/ extração correta de blocos de texto
    laparams = LAParams(
        word_margin=0.5, line_margin=1, boxes_flow=None)
    pdf_pages = extract_pages(file_path, laparams=laparams)
    return pdf_pages  # Retorna lista de páginas no formato LTPage


# Extrai blocos de texto. Arg.: Lista de págs.
def get_boxes(pages):
    pgdict = {}  # Dict com pares = núm. da pág.: blocos de texto da pág.
    pgnum = 0  # Núm. da pág. atual

    for page in pages:  # Para cada pág. na lista
        pgnum += 1  # Aumentando o núm. da pág. atual
        pgboxes = []  # Lista de blocos de texto na pág.

        for box in page:  # Para cada bloco na pág.

            # Garantindo que este bloco contém texto e não img., p. ex.
            if isinstance(box, LTTextBoxHorizontal):
                # Adicionando bloco à lista de blocos na pág.
                pgboxes.append(box)
        # Adicionando par núm. da pág.: lista de blocos ao dict
        pgdict[pgnum] = pgboxes

    return pgdict  # Retorna dict núm. da pág.: blocos de texto na pág.


# Extrai texto de dict. Arg: Dict (núm. da pág.: blocos da pág.)
def get_text(pgdict):
    textdict = {}  # Dict com pares núm. de pág.: texto

    for page in pgdict:  # Para cada pág.
        pgtext = ''  # Texto completo da pág.

        for box in pgdict[page]:  # Para cada bloco de texto na pág.
            box_text = box.get_text()  # Extraindo texto do bloco
            # Adicionando ao texto completo da pág.
            pgtext += f'\n{box_text}\n'

        textdict[page] = pgtext  # Adicionando texto da pág. ao dict

    return textdict  # Retorna dict núm. de pág.: texto da pág.


# Execução seguida dos 3 processos. Arg: núm. do arquivo
def full_extract(file_number):
    pdf_pages = get_pages(
        f'C:/Users/mforn/Desktop/Projeto Eneua/eneua/anais/anais_{file_number}.pdf')
    boxes_dict = get_boxes(pdf_pages)
    pages_text = get_text(boxes_dict)

    return pages_text


# Teste: Escreve o texto das págs. em um arquivo .txt
# Args: dict (núm. da pág.: texto da pág) e núm. do arquivo
def write_text(pages_text, file_number):
    with open(f'test_{file_number}.txt', 'w', encoding='utf-8') as txt_file:

        for page_number in pages_text:  # Para cada pág. no dict
            text = pages_text[page_number]  # Texto da pág.
            # Escreve o texto de cada pág. no .txt, identificando número da pág.
            txt_file.write(f'\nPÁGINA {page_number}\n\n{text}')


# Execução do teste
for i in range(1, 7):  # Para cada um dos anais (1 a 6)
    pages_text = full_extract(i)
    write_text(pages_text, i)
