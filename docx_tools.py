from string import punctuation
from docx import Document


def extractor(file_name): # Extrai texto do arquivo, retornando lista de parágrafos
    doc = Document(f'anais/{file_name}.docx') # Documento aberto
    paras_text = [] # Lista contendo o texto de cada parágrafo identificado
    for para in doc.paragraphs:
        para_text = para.text.strip() # Texto do parágrafo, sem espaços antes ou depois
        
        if para_text: # Caso texto não esteja em branco
            paras_text.append(para_text) # Acrescenta texto à lista
    
    return paras_text


def text_splitter(text_list): # Divide o texto em palavras
    words = [] # Lista de palavras
    for paragraph in text_list:
        paragraph = paragraph.split() # Divide o parágrafo em palavras
        for word in paragraph:
            words.append(word) # Adiciona palavras à lista de palavras
    return words


def clean(word_list): # Limpa as palavras
    with open('ignore.txt', encoding='utf-8') as file_1:
        ignore = file_1.read().lower() # Lista de palavras a ignorar
    
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
        