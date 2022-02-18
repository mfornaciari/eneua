import os
import gerenciamento_entrada as ge
import ferramentas_pdf as fp
import ferramentas_anais as fa
import ferramentas_nuvem as fn


# Definindo caminho relativo p/ anais
numero_anais = ge.pegar_num_anais()
diretorio_atual = os.path.dirname(__file__)
arquivo_anais = os.path.join(
    diretorio_atual, 'anais', f'anais_{numero_anais}.pdf')

while True:
    # Selecionando págs.
    nums_pag = ge.pegar_nums_pag()

    try:
        # Extraindo texto
        texto_pags = fp.extrair(arquivo_anais, nums_pag)
        break
    except AssertionError:
        print('O arquivo escolhido não possui uma ou mais das páginas definidas.\n')
        continue

# Contando número de ocorrências de cada palavra
contagem = fa.contar(texto_pags)
# Gerando e exibindo nuvem de palavras
nuvem = fn.gerar_nuvem(contagem)
fn.exibir_nuvem(nuvem)
