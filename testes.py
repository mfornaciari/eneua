import os.path as path
import ferramentas_pdf as fp
import ferramentas_anais as fa
import gerenciamento_entrada as ge


if __name__ == '__main__':
    caminho_diretorio_atual = path.dirname(__file__)

    for i in range(1, 7):
        numero_anais = i
        caminho_arquivo = path.join(
            caminho_diretorio_atual, 'anais', f'anais_{numero_anais}.pdf')

        texto_pags = fp.extrair(caminho_arquivo, None)
        contagem_organizada = fa.contar(texto_pags)
        fa.escrever_completo(texto_pags, numero_anais)
        fa.escrever_contagem(contagem_organizada, numero_anais)
