import os
import entrada
import ferramentas_pdf as fp
import ferramentas_anais as fa
import ferramentas_nuvem as fn


if __name__ == '__main__':
    # Definindo caminho relativo p/ anais
    msg_anais = 'Digite o número dos anais (1-6): '
    num_anais = input(msg_anais)
    while not entrada.validar_num_anais(num_anais):
        num_anais = input(msg_anais)
    diretorio_atual = os.path.dirname(__file__)
    arquivo_anais = os.path.join(
        diretorio_atual, 'anais', f'anais_{num_anais}.pdf')

    # Contando número de páginas no arquivo escolhido
    pags_totais = fp.contar_pags(arquivo_anais)

    # Definindo páginas dos anais com as quais trabalhar
    # region
    msg_pags = '''Digite as páginas a extrair, separadas por VÍRGULAS.
Use HÍFENS para definir INTERVALOS. Ex.: 1,3,5-9
Observe a paginação DO ARQUIVO, não do sumário.
Aperte ENTER sem digitar nada para extrair todas as páginas.\n'''
    # endregion
    pags = input(msg_pags)
    while True:
        conjunto_pags = entrada.validar_pags(pags, pags_totais)
        if conjunto_pags:
            break

    # Extraindo páginas do arquivo
    texto_pags = fp.extrair(arquivo_anais, conjunto_pags)

    # Contando número de ocorrências de cada palavra
    contagem = fa.contar(texto_pags)

    # Gerando e exibindo nuvem de palavras
    nuvem = fn.gerar_nuvem(contagem)
    fn.exibir_nuvem(nuvem)
