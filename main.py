import docx_tools as dt
import word_tools as wt


file_number = input('Digite o número dos anais: ') # Nome do arquivo
body = (article for article in dt.extract(file_number)) # Artigos como listas de palavras
counted_articles = {} # Dicionário contendo listas de palavras contadas
total = {} # Dicionário contendo total de ocorrências em todo o arquivo

choice = input('Digite "n" para gerar nuvem ou "l" para gerar lista de palavras: ')
if choice.lower() == 'n':
    dt.generate_txt(body)
    wt.generate_cloud('full_text')

elif choice.lower() == 'l':
    # Lista de artigos, contendo lista de palavras e no. de ocorrências para cada artigo
    counted_articles = [wt.countwords(article) for article in body]

    with open('wordcount.txt', mode= 'w', encoding='utf-8') as output: # Cria .txt
        idx = 1

        for article in counted_articles:
            if idx != 1: # Pula elementos pré-textuais
                output.write(f'\nARTIGO {idx - 1}:\n\n') # Escreve número do artigo no .txt     

                for pair in article:
                    if pair[1] >= 5: # Ignora palavras que aparecem menos de 5 vezes
                        output.write(f'{pair[0]}: {pair[1]}\n') # Escreve par "palavra: quantidade" no .txt

                    # Atualiza contagem total
                    if pair[0] not in total:
                        total[pair[0]] = pair[1]
                    else:
                        total[pair[0]] += pair[1]

            idx += 1 # Próximo artigo
        
        # Organiza total por quantidade de palavras
        total = sorted(total.items(), 
                        key= lambda pair: pair[1],
                        reverse= True)

        # Escreve contagem total no .txt
        output.write(f'\nTOTAL:\n\n')
        for pair in total:
            if pair[1] >= 5: # Ignora palavras que aparecem menos de 5 vezes
                output.write(f'{pair[0]}: {pair[1]}\n')
                continue
            break
