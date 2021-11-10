'Ferramentas para limpar e manipular texto dos anais.'

import re
from string import punctuation


# Limpa texto de cada pág. em um dict com pares = núm. da pág.: texto da pág.
# def limpar_texto(dict_texto):
#     print('Limpando texto...')

#     for pag, texto in dict_texto.items():
#         texto = re.sub(r'\n\s+', r'\n', texto)  # Remove linhas em branco
#         texto = re.sub(r' +', r' ', texto)  # Remove espaços extras
#         dict_texto[pag] = texto
#         print(f'Texto da pág. {pag} limpo.')

#     print('Texto completo limpo.')


# Separa palavras do texto completo.
# Retorna lista de palavras (str).
def separar_palavras(dict_texto: dict) -> list:
    print('Separando palavras...')
    palavras = []

    for pag in dict_texto:
        lista_palavras_pag = dict_texto[pag].split()
        palavras.extend(lista_palavras_pag)

    print('Palavras separadas.')
    return palavras


# Limpa palavras separadas.
# Retorna lista de palavras (str).
def limpar_palavras(palavras: list) -> list:
    print('Limpando palavras...')
    palavras_limpas = []
    pontuacao = punctuation + '“”‘…–ºª'

    for palavra in palavras:
        tem_digitos = any(caractere.isdigit() for caractere in palavra)

        if tem_digitos:
            # Checa se é um ano (4 dígitos seguidos)
            ano = re.search(r'[0-9]{4}', palavra)

            if not ano:
                # Remove todos os dígitos
                palavra = re.sub(r'[0-9]+', r'', palavra)

        palavra = palavra.strip(pontuacao)

        if len(palavra) > 1:
            palavras_limpas.append(palavra.upper())

    print('Palavras limpas.')
    return palavras_limpas


# Conta número de ocorrências de cada palavra.
# Retorna dict onde pares = palavra: núm. de ocorrências.
def contar_palavras(palavras_limpas: list) -> dict:
    print('Contando palavras...')
    contagem = {}

    for palavra in palavras_limpas:
        contagem[palavra] = contagem[palavra] + \
            1 if palavra in contagem else 1

    print('Todas as palavras contadas.')
    return contagem


# Organiza contagem de palavras por número de ocorrências.
# Retorna lista de tuplas, onde tupla[0] = palavra (str) e tupla[1] = núm. de ocorrências (int)
def organizar_contagem(contagem: dict) -> list:
    contagem_organizada = sorted(contagem.items(),
                                 key=lambda par: par[1], reverse=True)
    return contagem_organizada


# Processo completo de contagem.
def contar(dict_texto: dict) -> list:
    palavras = separar_palavras(dict_texto)
    palavras_limpas = limpar_palavras(palavras)
    contagem = contar_palavras(palavras_limpas)
    return organizar_contagem(contagem)


# Cria TXT com texto completo das págs. extraídas
def escrever_completo(dict_texto: dict, num_anais: int) -> None:
    print('Criando arquivo .txt com o texto completo...')

    with open(f'txt/texto_completo_{num_anais}.txt', 'w', encoding='utf-8') as arquivo_txt:
        for pag in dict_texto:
            texto = dict_texto[pag]
            arquivo_txt.write(f'----------\nPÁGINA {pag}\n\n{texto}\n\n')

    print('Arquivo criado.')


# Cria TXT a partir de lista de tuplas (palavra, núm. de ocorrências)
def escrever_contagem(contagem_organizada: list, num_anais: int) -> None:
    print('Criando arquivo .txt com a contagem de palavras...')

    with open(f'txt/contagem_{num_anais}.txt', 'w', encoding='utf-8') as arquivo_txt:
        for item in contagem_organizada:
            arquivo_txt.write(f'{item[0]}: {item[1]}\n')

    print('Arquivo criado.')
