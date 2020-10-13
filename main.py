import docx_tools as dt # Ferramentas para extrair e limpar texto
import word_tools as wt # Ferramentas para gerar output a partir de texto limpo


file_number = input('Digite o número dos anais: ') # Nome do arquivo
body = (article for article in dt.extract(file_number)) # Artigos como listas de palavras

choice = input('Digite "n" para gerar nuvem ou "l" para gerar lista de palavras: ')
if choice.lower() == 'n':
    dt.generate_txt(body)
    wt.generate_cloud('full_text')

elif choice.lower() == 'l':
    # Lista de artigos, contendo lista de palavras e no. de ocorrências para cada artigo
    counted_articles = (wt.countwords(article) for article in body)
    wt.generate_wordcount(counted_articles)
