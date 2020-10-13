import docx_tools as dt # Ferramentas para extrair e limpar texto
import word_tools as wt # Ferramentas para manipular texto limpo


print('''
Anais disponíveis:
3º Eneua (Unirio, 2015)
4º Eneua (USP, 2017)
6º Eneua (UFF, 2019)
''')
file_number = input('Digite o número dos anais desejados: ') # Nome do arquivo
body = (article for article in dt.extract(file_number)) # Artigos como listas de palavras

choice = input('Digite "n" para gerar nuvem ou "l" para gerar lista de palavras: ')
if choice.lower() == 'n':
    # Gera "full_text.txt" para uso pela função geradora da nuvem
    dt.generate_txt(body)
    wt.generate_cloud('full_text')

elif choice.lower() == 'l':
    # Lista de artigos, contendo lista de palavras e no. de ocorrências para cada artigo
    counted_articles = (wt.count(article) for article in body)
    wt.generate_wordcount(counted_articles)
