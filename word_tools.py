import os
import matplotlib.pyplot as plt

from os import path
from wordcloud import WordCloud


def countwords(word_list): # Conta palavras, retornando lista organizada por no. de ocorrências
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