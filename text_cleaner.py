def text_cleaner(text):
    output = [] # Lista que conterá o texto limpo, dividido em linhas
    adding = False # Flag para começar a adicionar linhas
    skip = False # Flag para pular marca d'água

    for line in text:
        if line.startswith('SUMÁRIO'): # Começa a adicionar linhas a partir do sumário
            adding = True
            continue

        if adding:
            if line.startswith('\n'): # Pula linha em branco
                continue
            elif line.startswith('Anais'): # Pula primeira linha da marca d'água
                skip = True
                continue
            elif skip: # Pula segunda linha da marca d'água
                skip = False
                continue
            
            output.append(line) # Adiciona linha a uma lista
        
    return output