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
        print('Número inválido.')
        num_anais = input(msg_anais)
    print('Número válido.')
    diretorio_atual = os.path.dirname(__file__)
    arquivo_anais = os.path.join(
        diretorio_atual, 'anais', f'anais_{num_anais}.pdf')

    while True:
        # Selecionando págs. a extrair
        nums_pag = entrada.pegar_nums_pag()
        try:
            # Extraindo texto
            texto_pags = fp.extrair(arquivo_anais, nums_pag)
            break
        except AssertionError:
            print('O arquivo escolhido não possui uma ou mais das páginas definidas.\n')
            continue

    # Contando número de ocorrências de cada palavra
    contagem = fa.contar(texto_pags)
    # entradarando e exibindo nuvem de palavras
    nuvem = fn.gerar_nuvem(contagem)
    fn.exibir_nuvem(nuvem)
