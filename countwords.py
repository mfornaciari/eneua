from string import punctuation
from text_cleaner import text_cleaner

with open('anais1.txt', encoding='utf-8') as f, open('ignore.txt', encoding='utf-8') as f2:
    text = f.readlines() # Texto, dividido em lista de linhas
    ignore = f2.read().lower() # Lista de termos a ignorar, em minúsculas

text = text_cleaner(text) # Texto limpo, dividido em lista de linhas
words = [] # lista de palavras no texto

for line in text: # Executa operações em cada linha do texto
    for char in punctuation: # Remove pontuação
        line = line.replace(char, ' ')
    line = line.lower() # Transforma linha em minúsculas
    line = line.split() # Divide linha em palavras

    for word in line:
        if word in ignore or len(word) == 1: # Ignora palavras na lista de ignoradas ou letras avulsas
            continue
        words.append(word) # Adiciona palavra à lista de palavras

wordcount = {} # Dicionário de contagem de palavras

for word in words:
    if word not in wordcount: # Cria chave para palavra ausente no dicionário, com valor de 1
        wordcount[word] = 1
        continue
    wordcount[word] += 1 # Soma 1 ao valor da chave da palavra no dicionário

pairs = sorted(wordcount.items(),
                key=lambda pair:pair[1],
                reverse=True)

for pair in pairs[:20]:
    print(pair[0], pair[1])