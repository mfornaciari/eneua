import os.path as path
import ferramentas_pdf as fp
import ferramentas_anais as fa
import gerenciamento_entrada as ge


# Definindo caminho relativo p/ anais
numero_anais = ge.pegar_num_anais()
caminho_diretorio_atual = path.dirname(__file__)
caminho_arquivo_anais = path.join(
    caminho_diretorio_atual, 'anais', f'anais_{numero_anais}.pdf')

while True:
    try:
        # Selecionando págs.
        nums_pag = ge.pegar_nums_pag()
        # Extraindo texto
        texto_pags = fp.extrair(caminho_arquivo_anais, nums_pag)
        break

    except AssertionError:
        print('O arquivo escolhido não possui uma ou mais das páginas definidas.\n')
        continue

contagem_organizada = fa.contar(texto_pags)

# TESTE
fa.escrever_completo(texto_pags, numero_anais)
fa.escrever_contagem(contagem_organizada, numero_anais)
