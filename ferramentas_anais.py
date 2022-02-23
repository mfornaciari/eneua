'Ferramentas para limpar e manipular texto dos anais.'

import re
from string import punctuation


def separar_palavras(dict_texto: dict[int, str]) -> list[str]:
    '''
    Separa palavras do texto completo.\n
    Retorna lista de palavras (str).
    '''
    print('Separando palavras...')
    palavras = [
        palavra for pag in dict_texto for palavra in dict_texto[pag].split()]
    print('Palavras separadas.')
    return palavras


def limpar_palavras(palavras: list[str]) -> list[str]:
    '''
    Limpa palavras separadas, removendo pontuação, espaços em branco,
    palavras a ignorar e números (exceto anos).\n
    Retorna lista de palavras(str).
    '''
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


def contar_palavras(palavras_limpas: list[str]) -> list[tuple[str, int]]:
    '''
    Conta número de ocorrências de cada palavra no texto.\n
    Retorna lista de tuplas organizada decrescentemente por número de ocorrências.
    Tupla[0] = palavra (str) e tupla[1] = número de ocorrências (int).
    '''
    print('Contando palavras...')
    contagem = {palavra: palavras_limpas.count(
        palavra) for palavra in palavras_limpas}
    print('Todas as palavras contadas.')
    return sorted(contagem.items(), key=lambda par: par[1], reverse=True)


# Processo completo de contagem.
def contar(dict_texto: dict[int, str]) -> list[tuple[str, int]]:
    palavras = separar_palavras(dict_texto)
    palavras_limpas = limpar_palavras(palavras)
    return contar_palavras(palavras_limpas)


# Cria TXT com texto completo das págs. extraídas
def escrever_completo(dict_texto: dict[int, str], num_anais: int) -> None:
    print('Criando arquivo .txt com o texto completo...')

    with open(f'texto_completo_{num_anais}.txt', 'w', encoding='utf-8') as arquivo_txt:
        for pag in dict_texto:
            texto = dict_texto[pag]
            arquivo_txt.write(f'----------\nPÁGINA {pag}\n\n{texto}\n\n')

    print('Arquivo criado.')


# Cria TXT a partir de lista de tuplas (palavra, núm. de ocorrências)
def escrever_contagem(contagem: list[tuple[str, int]], num_anais: int) -> None:
    print('Criando arquivo .txt com a contagem de palavras...')

    with open(f'contagem_{num_anais}.txt', 'w', encoding='utf-8') as arquivo_txt:
        for item in contagem:
            arquivo_txt.write(f'{item[0]}: {item[1]}\n')

    print('Arquivo criado.')
