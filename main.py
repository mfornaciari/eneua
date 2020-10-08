from docx2python import docx2python
import docx_tools as dtools
from countwords import countwords


file_name = input('Digite o nome do arquivo sem a extensão .docx: ') # Nome do arquivo
doc = docx2python(f'anais/{file_name}.docx') # Documento aberto

body = dtools.extract(doc.body) # Corpo do texto
footnotes = dtools.extract(doc.footnotes) # Notas de rodapé

with open('test.txt', mode= 'w', encoding= 'utf-8') as f: # Teste
    for paragraph in body: # Escreve parágrafos do corpo no .txt
        f.write(paragraph + '\n\n')
    for paragraph in footnotes: # Escreve parágrafos das notas no .txt
        f.write(paragraph + '\n\n')

'''
text = dtools.extractor(file_name) # Lista de texto dos parágrafos identificados
words = dtools.text_splitter(text) # Lista (suja) de palavras
words = dtools.clean(words) # Lista (limpa) de palavras
counted_words = countwords(words) # Dicionário de palavras organizado por número de ocorrências

for pair in counted_words[:50]: # Teste
    print(f'{pair[0]}: {pair[1]}')
'''