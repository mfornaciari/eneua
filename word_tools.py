import os
import pandas as pd
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
from docx_tools import article_titles


# Conta palavras, retornando lista organizada por no. de ocorrências
def count(word_list):
    wordcount = {} # Dicionário de contagem de palavras

    for word in word_list:
        if word in wordcount: 
            wordcount[word] += 1 # Soma 1 ao valor da palavra no dicionário
            continue
        wordcount[word] = 1 # Cria chave para palavra ausente no dicionário, com valor de 1

    # Organiza lista de palavras por quantidade de ocorrências; retorna lista de tuplas
    wordcount = sorted(wordcount.items(), 
                    key= lambda pair: pair[1],
                    reverse= True)

    # Remove palavras ocorrendo < 5 vezes
    output = {word: value for word, value in wordcount if value >= 5}
    return output


# Cria nuvem de palavras a partir de arquivo .txt
def generate_cloud(txt): 
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    text = open(path.join(d, f'{txt}.txt',), encoding='utf-8').read() # Read the whole text
    wordcloud = WordCloud().generate(text) # Generate a word cloud image

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# Cria lista de no. de ocorrências a partir de lista contada de artigos
def generate_wordcount(file_number, article_list):
    titles = article_titles[file_number] # Tupla de títulos de artigos
    full_data = pd.DataFrame(columns=titles) # Tabela com títulos dos artigos como colunas
    idx = 0 # Índice do atual artigo

    for article in article_list: # Calculando somatório total
        article_title = titles[idx] # Título do artigo
        idx += 1

        if idx >= len(titles): # Encerra loop após passar por todos os artigos
            break

        for word in article: # Para cada palavra registrada no artigo
            value = article[word] # no. de ocorr. da palavra
            full_data.loc[word, article_title] = value # Adiciona palavra e no. de ocorr. à tabela

    full_data.fillna(0, inplace=True) # Substitui ausência de dados por zeros
    total = full_data.sum(axis=1) # Soma totais
    full_data['TOTAL'] = total # Adiciona coluna 'TOTAL' à tabela

    full_data.to_excel(r'wordcount.xlsx') # Escreve tabela em arquivo .xlsx    
