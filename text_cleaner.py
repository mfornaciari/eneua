def text_cleaner(file_name):
    output = [] # Lista que conterá o texto limpo, dividido em linhas
    skip_count = 0 # Contador de linhas a pular

    with open('Anais/' + file_name + '.txt', encoding='utf-8') as f:
        text = f.readlines() # Texto, dividido em lista de linhas

    for line in text:
        if line.startswith('\n'): # Pula linha em branco
            continue
        
        if file_name == 'anais_6':
            if line.startswith('Anais d'): # Pula única linha da marca d'água
                continue

        elif file_name in ('anais_1', 'anais_4'):
            if line.startswith('Anais'): # Pula primeira linha da marca d'água
                skip_count += 1
                continue
            if skip_count > 0: # Reseta o contador e pula segunda linha da marca d'água
                skip_count = 0
                continue
        
        elif file_name in ('anais_2', 'anais_3'):
            if line.startswith('ANAIS DO'): # Pula primeira linha da marca d'água
                skip_count += 1
                continue
            if skip_count == 1: # Pula segunda linha da marca d'água
                skip_count += 1
                continue
            else: # Reseta o contador e pula terceira linha da marca d'água
                skip_count = 0
                continue
        
        output.append(line) # Adiciona linha a uma lista
        
    return output
