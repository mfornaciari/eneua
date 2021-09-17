def count_words(pages_text):
    word_dict = {}  # Dict [palavra: número de ocorrências]

    for page_number in pages_text:  # Para cada pág. no dict
        text = pages_text[page_number].split()  # Texto da pág.

        for word in text:
            if word in word_dict:  # Se palavra já estiver no dict, aumenta ocorrências em 1
                word_dict[word] += 1
                continue

            # Se não estiver no dict, adiciona com ocorrências = 1
            word_dict[word] = 1

    # Organiza dict por número de ocorrências; retorna lista de tuplas
    word_dict = sorted(word_dict.items(),
                       key=lambda pair: pair[1],
                       reverse=True)

    # Remove palavras ocorrendo < 5 vezes; retorna dict [palavra: número de ocorrências]
    output = {word: value for word, value in word_dict if value >= 5}
    return output  # Dict [palavra: número de ocorrências]
