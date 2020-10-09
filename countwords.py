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
