import docx_tools as dtools
from countwords import countwords


file_number = input('Digite o número dos anais: ') # Nome do arquivo
body = (article for article in dtools.extract(file_number)) # Artigos como listas de palavras
counted_articles = {} # Dicionário contendo listas de palavras contadas
total = {} # Dicionário contendo total de ocorrências em todo o arquivo

# Lista de artigos, contendo lista de palavras e no. de ocorrências para cada artigo
counted_articles = [countwords(article) for article in body]

with open('wordcount.txt', mode= 'w', encoding='utf-8') as output: # Cria .txt
    idx = 1

    for article in counted_articles:
        if idx != 1: # Pula elementos pré-textuais
            output.write(f'\nARTIGO {idx - 1}:\n') # Escreve número do artigo no .txt     
    
            for pair in article:
                output.write(f'{pair[0]}: {pair[1]}\n') # Escreve par "palavra: quantidade" no .txt

                # Atualiza contagem total
                if pair[0] not in total:
                    total[pair[0]] = pair[1]
                else:
                    total[pair[0]] += pair[1]

        idx += 1
    
    # Organiza total por quantidade de palavras
    total = sorted(total.items(), 
                    key= lambda pair: pair[1],
                    reverse= True)

    # Escreve contagem total no .txt
    output.write(f'\nTOTAL:\n')
    for pair in total:
        output.write(f'{pair[0]}: {pair[1]}\n')
