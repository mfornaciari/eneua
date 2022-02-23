'Ferramentas para gerar, exibir e salvar nuvem de palavras.'

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def gerar_nuvem(contagem: list[tuple[str, int]]) -> WordCloud:
    contagem = dict(contagem)
    return WordCloud().generate_from_frequencies(contagem)


def exibir_nuvem(nuvem: WordCloud) -> None:
    plt.imshow(nuvem, interpolation="bilinear")
    plt.axis("off")
    plt.show()
