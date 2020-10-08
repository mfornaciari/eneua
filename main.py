import docx_tools as dtools
from countwords import countwords


file_name = input('Digite o nome do arquivo sem a extensão .docx: ')

'''
text = dtools.extractor(file_name) # Lista de texto dos parágrafos identificados
words = dtools.text_splitter(text) # Lista (suja) de palavras
words = dtools.clean(words) # Lista (limpa) de palavras
counted_words = countwords(words) # Dicionário de palavras organizado por número de ocorrências

for pair in counted_words[:50]: # Teste
    print(f'{pair[0]}: {pair[1]}')
'''