from string import punctuation
from docx2python import docx2python


def text_splitter(text_list): # Divide o texto em palavras
    words = [] # Lista de palavras
    for paragraph in text_list:
        paragraph = paragraph.split() # Divide o parágrafo em palavras
        for word in paragraph:
            words.append(word) # Adiciona palavras à lista de palavras
    return words


def clean(word_list): # Limpa as palavras
    with open('ignore.txt', encoding='utf-8') as file_1:
        ignore = file_1.read() # Lista de palavras a ignorar
    
    clean_words = [] # Lista de palavras limpas
    for word in word_list:
        
        # Ignora "palavras" compostas unicamente por números ou pontuação
        if all(char.isnumeric() or char in punctuation + '“”‘’' for char in word):
            continue

        # Remove pontuação e números
        for char in word:
            if char in punctuation + '“”‘’' or char.isnumeric():
                word = word.replace(char, '')
        
        # Ignora letras avulsas
        if len(word) < 2:
            continue
        
        # Transforma palavra em minúsculas
        word = word.lower()
        
        # Ignora palavras na lista de palavras ignoradas
        if word in ignore:
            continue
        
        # Adiciona palavra limpa à lista de palavras
        clean_words.append(word)
    return clean_words            


def extract_body(file_name): # Extrai corpo do texto
    doc = docx2python(f'anais/{file_name}.docx')
    body = doc.body
    return [item for i in body for j in i for k in j for item in k if item]


def extract_footnotes(file_name): # Extrai notas de rodapé
    doc = docx2python(f'anais/{file_name}.docx')
    footnotes = doc.footnotes
    return [item for i in footnotes for j in i for k in j for item in k if item]


body = extract_body('anais_3')
footnotes = extract_footnotes('anais_3')

with open('test.txt', mode= 'w', encoding= 'utf-8') as f:
    for paragraph in body:
        f.write(paragraph + '\n\n')
    for paragraph in footnotes:
        f.write(paragraph + '\n\n')
