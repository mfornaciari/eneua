'Ferramentas para limpar e manipular texto dos anais.'

import re
from string import punctuation


# Separa palavras do texto completo.
# Retorna lista de palavras (str).
def separar_palavras(dict_texto: dict) -> list:
    print('Separando palavras...')
    palavras = [
        palavra for pag in dict_texto for palavra in dict_texto[pag].split()]
    print('Palavras separadas.')
    return palavras


# Limpa palavras separadas.
# Retorna lista de palavras (str).
def limpar_palavras(palavras: list) -> list:
    print('Limpando palavras...')
    pontuacao = punctuation + '“”‘…–ºª'
    with open('ignore.txt', 'r', encoding='utf-8') as arquivo_ignorar:
        lista_ignorar = [palavra.strip('\n')
                         for palavra in arquivo_ignorar.readlines()]
    palavras_limpas = []

    for palavra in palavras:
        # Checa se palavra é um ano (4 dígitos seguidos)
        if not re.search(r'[0-9]{4}', palavra):
            # Remove todos os dígitos da palavra se ela não for um ano
            palavra = re.sub(r'[0-9]+', r'', palavra)
        palavra = palavra.strip(pontuacao)
        if palavra.lower() not in lista_ignorar and len(palavra) > 1:
            palavras_limpas.append(palavra.upper())

    print('Palavras limpas.')
    return palavras_limpas


# Conta número de ocorrências de cada palavra.
# Retorna lista de tuplas organizada por número decrescente de ocorrências.
# Tupla[0] = palavra (str) e tupla[1] = número de ocorrências (int).
def contar_palavras(palavras_limpas: list) -> list:
    print('Contando palavras...')
    contagem = {}

    for palavra in palavras_limpas:
        contagem[palavra] = contagem[palavra] + \
            1 if palavra in contagem else 1

    print('Todas as palavras contadas.')
    return sorted(contagem.items(), key=lambda par: par[1], reverse=True)


# Processo completo de contagem.
def contar(dict_texto: dict) -> list:
    palavras = separar_palavras(dict_texto)
    palavras_limpas = limpar_palavras(palavras)
    return contar_palavras(palavras_limpas)


# Cria TXT com texto completo das págs. extraídas
def escrever_completo(dict_texto: dict, num_anais: int) -> None:
    print('Criando arquivo .txt com o texto completo...')

    with open(f'texto_completo_{num_anais}.txt', 'w', encoding='utf-8') as arquivo_txt:
        for pag in dict_texto:
            texto = dict_texto[pag]
            arquivo_txt.write(f'----------\nPÁGINA {pag}\n\n{texto}\n\n')

    print('Arquivo criado.')


# Cria TXT a partir de lista de tuplas (palavra, núm. de ocorrências)
def escrever_contagem(contagem_organizada: list, num_anais: int) -> None:
    print('Criando arquivo .txt com a contagem de palavras...')

    with open(f'contagem_{num_anais}.txt', 'w', encoding='utf-8') as arquivo_txt:
        for item in contagem_organizada:
            arquivo_txt.write(f'{item[0]}: {item[1]}\n')

    print('Arquivo criado.')
