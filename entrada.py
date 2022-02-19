'Ferramentas para lidar com a entrada de dados pelo usuário.'

import re


def validar_num_anais(numero: str) -> bool:
    '''
    Valida número dos anais fornecido pelo usuário.\n
    Se número estiver no intervalo 1-6 (anais disponíveis), retorna True;
    caso contrário, False.
    '''
    if numero in '123456':
        print('Número válido.')
        return True

    print('Número inválido.')
    return False


def validar_pags(pags: str, pags_totais: int) -> list | bool:
    padrao_pagina = r'^\d+$'
    padrao_intervalo = r'^\d+\s*-\s*\d+$'
    if not pags:
        print('Extraindo arquivo completo.')
        return True

    lista_pags = [pag.strip() for pag in pags.split(',') if pag.strip()]
    lista_final = []
    if not lista_pags:
        print('Você não inseriu nenhuma página ou intervalo.')
        return False

    for item in lista_pags:
        e_pagina_avulsa = re.search(padrao_pagina, item)
        e_intervalo = re.search(padrao_intervalo, item)
        if e_pagina_avulsa:
            lista_final.append(int(item))
            continue

        if e_intervalo:
            intervalo = [int(pag.strip()) for pag in item.split('-')]
            if intervalo[0] > intervalo[-1]:
                print(f'O intervalo {item} é inválido.')
                return False

            pags_intervalo = [pag for pag in range(
                intervalo[0], intervalo[1] + 1)]
            lista_final.extend(pags_intervalo)
            continue

        print(f'"{item}" não é uma página ou intervalo válido.')
        return False

    for item in lista_final:
        if int(item) > pags_totais:
            print(f'O arquivo não possui a página {item}.')
            return False

    print('Páginas válidas.')
    return sorted(set(lista_final))
