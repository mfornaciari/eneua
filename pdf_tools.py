import re
from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBoxHorizontal


# Gera lista de págs. a extrair de PDF
def get_page_numbers():
    page_numbers = input('''Digite as páginas a extrair, separadas por vírgulas, sem espaços.
Use hífens para definir intervalos. EX.: 1,3,5-9
Observe a paginação DO ARQUIVO, não do sumário.\n''')

    # Caso usuário não digite nada, encerra (extrairá todas as págs.)
    if not page_numbers:
        return

    # Cria lista a partir de números digitados
    page_numbers = page_numbers.split(',')
    output = []  # Lista de págs. a extrair

    for item in page_numbers:

        # Caso item seja intervalo [#-#], adiciona as págs. do intervalo à lista
        if '-' in item:
            split_item = item.split('-')
            start = int(split_item[0]) - 1
            end = int(split_item[-1]) + 1
            total = [num for num in range(start, end)]
            output.extend(total)
            continue

        # Caso item não seja intervalo, adiciona à lista
        output.append(int(item) - 1)

    return output


# Extrai págs. de PDF. Arg.: caminho p/ arquivo; págs. a extrair
def get_pages(file_path, numbers=None):
    print('Extraindo páginas...')

    # Parâmetros para análise de layout. Necessário p/ extração correta de blocos de texto
    laparams = LAParams(
        word_margin=0.5, line_margin=1, boxes_flow=None)
    # Extração de págs.
    pdf_pages = extract_pages(
        file_path, page_numbers=numbers, laparams=laparams)

    print('Páginas extraídas')
    return pdf_pages  # Retorna lista de páginas no formato LTPage


# Extrai blocos de texto. Arg.: Lista de págs.
def get_boxes(pages):
    print("Extraindo caixas de texto...")
    pgdict = {}  # Dict com pares = [número da pág.: blocos de texto da pág.]
    pgnum = 0  # Número da pág. atual

    for page in pages:  # Para cada pág. na lista
        pgnum += 1  # Aumentando o número da pág. atual
        pgboxes = []  # Lista de blocos de texto na pág.

        for box in page:  # Para cada bloco na pág.

            # Garantindo que este bloco contém texto e não img., p. ex.
            if isinstance(box, LTTextBoxHorizontal):
                # Adicionando bloco à lista de blocos na pág.
                pgboxes.append(box)

        # Adicionando par [número da pág.: lista de blocos] a pgdict
        pgdict[pgnum] = pgboxes
        print(f'Caixas da {pgnum}ª pág. extraídas')

    print('Caixas de texto extraídas')
    return pgdict  # Retorna dict [número da pág.: blocos de texto na pág.]


# Extrai texto de dict. Arg: Dict [número da pág.: blocos da pág.]
def get_text(pgdict):
    print('Extraindo texto...')
    textdict = {}  # Dict com pares [número de pág.: texto]

    for page in pgdict:  # Para cada pág.
        pgtext = ''  # Texto completo da pág.

        for box in pgdict[page]:  # Para cada bloco de texto na pág.
            box_text = box.get_text()  # Extraindo texto do bloco
            # Adicionando ao texto completo da pág.
            pgtext += f'\n{box_text}\n'

        textdict[page] = pgtext  # Adicionando texto da pág. ao dict
        print(f'Texto da {page}ª pág. extraído')

    print('Texto extraído')
    return textdict  # Retorna dict [número de pág.: texto da pág.]


# Limpa texto de cada pág. em um dict [número da pág.: texto da pág.]
def clean(textdict):
    for page, text in textdict.items():
        clean_text = re.sub('\n\s+', '\n', text)
        clean_text = re.sub(' +', ' ', clean_text)

        textdict[page] = clean_text


# Execução seguida dos 3 processos. Arg: núm. do arquivo; números das págs. a extrair
def full_extract(file_number, numbers):
    pdf_pages = get_pages(
        f'C:/Users/mforn/Desktop/Projeto Eneua/eneua/anais/anais_{file_number}.pdf', numbers)
    boxes_dict = get_boxes(pdf_pages)
    pages_text = get_text(boxes_dict)

    return pages_text  # Dict [número da pág: texto da pág.]
