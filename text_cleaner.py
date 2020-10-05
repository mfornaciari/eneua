def text_cleaner(file_name):
    output = [] # Lista que conterá o texto limpo, dividido em linhas
    skip = False # Flag para pular marca d'água
    skip_count = 0 # Contador de linhas a pular

    with open('Anais/' + file_name + '.txt', encoding='utf-8') as f:
        text = f.readlines() # Texto, dividido em lista de linhas

    for line in text:
        if line.startswith('\n'): # Pula linha em branco
            continue
        
        if file_name == 'anais6':
            if line.startswith('Anais d'): # Pula única linha da marca d'água
                continue

        elif file_name in ('anais1', 'anais4'):
            if line.startswith('Anais'): # Pula primeira linha da marca d'água
                skip = True
                continue
            if skip: # Pula segunda linha da marca d'água
                skip = False
                continue
        
        elif file_name in ('anais2', 'anais3'):
            if line.startswith('ANAIS DO'): # Pula primeira linha da marca d'água
                skip = True
                skip_count += 1
                continue
            while skip and skip_count <= 2: # Pula linhas da marca d'água até pular 3 linhas
                skip_count += 1
                continue
            else: # Reseta flag e contador após pular todas as linhas da marca d'água
                skip = False
                skip_count = 0
        
        output.append(line) # Adiciona linha a uma lista
        
    return output
