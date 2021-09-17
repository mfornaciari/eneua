import pdf_tools as pt  # Ferramentas para extrair e limpar texto
import annals_tools as at  # Ferramentas para manipular texto limpo dos anais


annals_num = int(input('Digite o número dos anais: '))  # Edição dos anais
pg_nums = pt.get_page_numbers()  # Nos. das págs. a extrair
pgs_text = pt.full_extract(annals_num, pg_nums)  # Dict [no. da pág.: texto]
pt.clean(pgs_text)  # Limpa texto de cada pág.
words = at.count_words(pgs_text)  # Dict [palavra: no. de ocorrências]

# TESTE: escreve [palavras: número de ocorrências] em arquivo TXT
with open(f'test_{annals_num}.txt', 'w', encoding='utf-8') as txt_file:
    for word in words:
        txt_file.write(f'{word} : {words[word]}\n')
