import re
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextBoxHorizontal


def extract(file_path):
    with open(file_path, 'rb') as pdf_file:
        extracted_text = extract_text(pdf_file)
        print('Texto extraído')
        return extracted_text


def clean(text):
    clean_text = re.sub(r'\n+\s+', r'\n', text)
    clean_text = re.sub(r'\s+\n+', r'\n', clean_text)
    clean_text = re.sub(r' +', r' ', clean_text)
    return clean_text


def write_test(text, number):
    with open(f'test_{number}.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
        print('Arquivo criado')


'''
for i in range(1, 7):
    pdf_text = extract(
        f'C:/Users/mforn/Desktop/Projeto Eneua/eneua/anais/anais_{i}.pdf')
    pdf_text = clean(pdf_text)
    write_test(pdf_text, i)
'''

pdf_text = extract_pages(
    'C:/Users/mforn/Desktop/Projeto Eneua/eneua/anais/anais_6.pdf')

with open(f'test_7.txt', 'w', encoding='utf-8') as txt_file:
    pgnum = 1

    for page in pdf_text:
        txt_file.write(f'\nPÁGINA {pgnum}\n')
        pgnum += 1

        for box in page:

            if isinstance(box, LTTextBoxHorizontal):
                text = box.get_text()

                if not re.fullmatch(r'\s+', text):
                    txt_file.write(
                        f'\nINÍCIO DE BLOCO\n{text}FIM DE BLOCO\n')
