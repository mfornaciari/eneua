import os
import matplotlib.pyplot as plt

from os import path
from wordcloud import WordCloud


# Conta palavras, retornando lista organizada por no. de ocorrências
def countwords(word_list): 
    wordcount = {} # Dicionário de contagem de palavras

    for word in word_list:
        if word not in wordcount: # Cria chave para palavra ausente no dicionário, com valor de 1
            wordcount[word] = 1
            continue
        wordcount[word] += 1 # Soma 1 ao valor da chave da palavra no dicionário

    # Organiza lista de palavras por quantidade de ocorrências; retorna lista de tuplas
    wordcount = sorted(wordcount.items(), 
                    key= lambda pair: pair[1],
                    reverse= True)

    return wordcount


# Cria nuvem de palavras a partir de arquivo .txt
def generate_cloud(txt): 
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, f'{txt}.txt',), encoding='utf-8').read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    '''
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    '''
    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# Cria lista de no. de ocorrências a partir de lista contada de artigos
def generate_wordcount(article_list): 
     with open('wordcount.txt', mode= 'w', encoding='utf-8') as output: # Cria .txt
        total = {} # Contagem total
        idx = 1 # Índice do atual artigo
        articles = {} # Dicionário de artigos

        for article in article_list: # Calculando somatório total
            if idx != 1: # Pula elementos pré-textuais
                articles[idx] = []

                for pair in article: # Para cada par "palavra: quant." no artigo
                    word, value = pair[0], pair[1]
                    
                    # Adiciona pares a entrada no dicionário se quant. >= 5
                    if value >= 5:
                        articles[idx].append(pair)

                    # Atualiza contagem total
                    if word in total:
                        total[word] += value
                        continue
                    total[word] = value              
            
            idx += 1 # Próximo artigo
        
        idx = 1 # Reseta índice após terminar o cálculo do total

        # Organiza total por quantidade de palavras
        total = sorted(total.items(), 
                        key= lambda pair: pair[1],
                        reverse= True)
        
        # Escreve contagem total no .txt
        output.write(f'TOTAL:\n\n')
        for pair in total:
            word, value = pair[0], pair[1]
            if value >= 5: # Adiciona palavras que aparecem > 5x
                output.write(f'{word}: {value}\n')
                continue
            break # Encerra loop ao chegar numa palavra que aparece < 5x
        
        # Escreve contagem por artigo no .txt
        for article_number in articles:
            output.write(f'\nARTIGO {article_number}:\n\n') # Escreve número do artigo no .txt

            for pair in articles[article_number]:
                word, value = pair[0], pair[1]
                output.write(f'{word}: {value}\n')
 