from docx import Document

file_name = input('Digite o nome do arquivo sem a extensão .docx: ')
paras_text = [] # Lista contendo o texto de cada parágrafo identificado

document = Document(f'anais/{file_name}.docx') # Documento aberto

for para in document.paragraphs:
    para_text = para.text.strip() # Texto do parágrafo
    if para_text: # Caso texto não esteja em branco
        paras_text.append(para_text) # Acrescenta texto à lista

for para in paras_text[:200]: # Exibe texto na lista
    print(para)
    print()
