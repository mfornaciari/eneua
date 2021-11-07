import os.path as path
import ferramentas_pdf as fp
import ferramentas_anais as fa
import gerenciamento_entrada as ge


def pegar_caminho_relativo(numero_anais):
    # Definindo caminho relativo p/ anais
    caminho_diretorio_atual = path.dirname(__file__)
    return path.join(caminho_diretorio_atual, 'anais', f'anais_{numero_anais}.pdf')


def gerar_texto(caminho_arquivo):
    try:
        # Selecionando págs.
        nums_pag = ge.pegar_nums_pag()
        # Extraindo texto
        # Limpando texto
        # fa.limpar_texto(texto_pags)
        return fp.extrair(caminho_arquivo, nums_pag)

    except AssertionError:
        print('O arquivo escolhido não possui uma ou mais das páginas definidas.\n')
        return gerar_texto(caminho_arquivo_anais)


def gerar_contagem(texto_pags):
    # Contando palavras e organizando contagem
    return fa.contar(texto_pags)


# Executando processo principal
entrada_numero_anais = ge.pegar_num_anais()
caminho_arquivo_anais = pegar_caminho_relativo(entrada_numero_anais)
texto_pags = gerar_texto(caminho_arquivo_anais)
contagem_organizada = gerar_contagem(texto_pags)

# TESTE
fa.escrever_completo(texto_pags, entrada_numero_anais)
fa.escrever_contagem(contagem_organizada, entrada_numero_anais)
