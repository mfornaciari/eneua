from string import punctuation
from text_cleaner import text_cleaner

file_name = input('Digite o nome do arquivo sem a extensão .txt: ')
text = text_cleaner(file_name) # Texto limpo, dividido em lista de linhas
words = [] # lista de palavras no texto

with open('ignore.txt', encoding='utf-8') as f2:
    ignore = f2.read().lower() # Lista de termos a ignorar, em minúsculas

for line in text:
    for char in punctuation + '“”‘’': # Remove pontuação
        if char in line:
            line = line.replace(char, ' ')
    line = line.lower() # Transforma linha em minúsculas
    line = line.split() # Divide linha em palavras

    for word in line:
        # Ignora: 1) Letras avulsas; 2) números; 3) palavras na lista de ignoradas
        if len(word) == 1 or word.isnumeric() or word in ignore:
            continue
        words.append(word) # Adiciona palavra à lista de palavras

wordcount = {} # Dicionário de contagem de palavras

for word in words:
    if word not in wordcount: # Cria chave para palavra ausente no dicionário, com valor de 1
        wordcount[word] = 1
        continue
    wordcount[word] += 1 # Soma 1 ao valor da chave da palavra no dicionário

pairs = sorted(wordcount.items(), # Organiza lista de palavras por quantidade de ocorrências
                key=lambda pair:pair[1],
                reverse=True)

for pair in pairs[:20]: # Exibe palavras e número de ocorrências
    print(pair[0], pair[1])
