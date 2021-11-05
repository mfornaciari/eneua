'Ferramentas para lidar com a entrada de dados pelo usuário.'


def pegar_num_anais() -> int:
    ''' 
    Solicita que usuário defina o número dos anais com os quais trabalhar.\n
    Se usuário não fornecer número inteiro, levanta ValueError.
    Se fornecer número fora do intervalo 1-6 (anais disponíveis), levanta AssertionError.
    Em ambos os casos, chama a si mesma novamente para refazer a solicitação.\n  
    Retorna número dos anais (int).
    '''

    try:
        numero = int(input('Digite o número dos anais (1-6): '))
        assert 0 < numero < 7
        return numero

    except:
        print("Número inválido.")
        return pegar_num_anais()


def processar_nums_pag(entrada_nums: str) -> list:
    '''
    Processa os dados inseridos em resposta à solicitação de pegar_nums_pag().\n
    Separa string nas vírgulas, considerando cada valor da lista gerada uma página individual ou
    um intervalo (#-#).\n
    Páginas individuais são convertidas para int e adicionadas à lista final.
    Intervalos são separados no hífen, considerando o primeiro valor da lista gerada a página
    inicial do intervalo e o último, a página final. Tais valores são convertidos para int e
    usados para gerar uma lista de páginas no intervalo.\n
    Levanta exceção ValueError se qualquer tentativa de conversão para int falhar, informando
    ao usuário que os dados são inválidos e chamando pegar_nums_pag novamente.\n
    Retorna lista de números de páginas (int).
    '''

    lista_nums = []
    try:

        for item in entrada_nums.split(','):

            # Caso item seja intervalo (#-#), adiciona as págs. nele à lista
            if '-' in item:
                item_dividido = item.split('-')
                pag_inicial = int(item_dividido[0]) - 1
                pag_final = int(item_dividido[-1])
                intervalo = range(pag_inicial, pag_final)
                lista_nums.extend([num for num in intervalo])
                continue

            lista_nums.append(int(item) - 1)

        return lista_nums

    except:
        print('Entrada de dados inválida.\n')
        return pegar_nums_pag()


def pegar_nums_pag() -> list | None:
    '''
    Solicita que o usuário defina números das páginas com as quais trabalhar.\n
    Retorna None caso usuário não defina números das páginas, o que levará à extração de
    todas as páginas do arquivo; caso contrário, passa a entrada de dados como argumento
    à função processar_nums_pag e retorna a lista de números de páginas (int) resultante.
    '''

    # region
    entrada_nums = input('''Digite as páginas a extrair, separadas por VÍRGULAS.
Use HÍFENS para definir INTERVALOS. Ex.: 1,3,5-9
Observe a paginação DO ARQUIVO, não do sumário.
Aperte ENTER sem digitar nada para extrair todas as páginas.\n''')
    # endregion

    # Caso usuário não escolha págs., encerra (extrairá todas as págs.)
    if not entrada_nums:
        return

    return processar_nums_pag(entrada_nums)


if __name__ == '__main__':
    print(pegar_nums_pag())
