from string import punctuation
from docx2python import docx2python


with open('ignore.txt', encoding='utf-8') as file_1:
    ignore = file_1.read() # Lista de palavras a ignorar

# Dicionário com os títulos dos artigos em cada edição, formato "número: tupla"
article_titles = { 
    '3': ( # Anais 3
        'the office of the coordinator of inter-american affairs: o comitê de são paulo',
        '“the council-fire is extinguished”: a origem dos primeiros aliados na independência estadunidense (1766-1784)',
        'da contracultura ao conservadorismo: o cinema de crime em hollywood das décadas 1960-70',
        'um pequeno olhar sobre a democracia dos estados unidos da américa',
        '“eis que sou contra ti, ó gogue”: a ameaça comunista nas interpretações escatológicas de hal lindsey e tim lahaye (1970-1980)',
        'um olhar sobre as representações em cinderela (1950) e a bela e a fera (1991)',
        'thanksgiving em imagens: representações da colônia no século xix',
        'a guerra do iraque em perspectiva: um balanço da política externa neoconservadora e o ônus da guerra',
        'os cartoons vão à guerra: uma análise de discurso do desenho hitler’s children – education for death na campanha da segunda guerra mundial (1941-1945)',
        'as transformações da imprensa estadunidense dos anos 1950, o the new york times e seus correspondentes na américa do sul',
        'brasil e estados unidos no pós segunda guerra mundial: dos 4-h clubs aos clubes 4-s no brasil',
        'uma nação em questão: análise dos discursos de jfk na televisão e no rádio',
        'muitas nações unidas: spielberg, liberais nacionalistas e a segunda guerra mundial em call of duty (2003)',
        'um führer na américa: fritz kuhn e o nazismo nos estados unidos (1936-1941)',
        'as terras do grande espírito: memórias da colônia e políticas de assentamento indígena na américa inglesa (1860-1890)',
        '“juventude em fúria”: representações, tensões e política na era reagan (1981-1988)',
        'das páginas para as telas e de lá de volta outra vez: a construção das narrativas compartilhadas de batman nas hqs e no cinema',
    ),
    '4': ( # Anais 4
        'antes de feminista, latina: a construção da identidade latina no feminismo dos estados unidos contemporâneo',
        'produzindo mitos: a imagem do soldado afro-americano na revista the crisis na primeira guerra mundial',
        'walt disney no brasil – fatos e propaganda na imprensa brasileira em 1941',
        'cinema e resistência no capitalismo contemporâneo: um estudo da obra de michael moore',
        'lincoln kirstein: o enviado de nelson rockefeller à américa do sul e sua importância para a formação da coleção de arte brasileira do museu de arte moderna de nova york no início dos anos 1940',
        'a revolução de fevereiro nas páginas do the new york times: a nova rússia e a entrada dos eua na primeira guerra mundial',
        'o filme lincoln de steven spielberg (2012) e os historiadores',
        'experiência urbana na virada do século xx: nova york em três romances norte-americanos',
        'família, conservadorismo e cinema: uma análise do filme atração fatal (1987)',
        'o homem que sabia português e tantas outras línguas: apontamentos da trajetória de tad szulc (1926-2001), correspondente do the new york times na américa latina',
        'a representação do 11 de setembro na obra “the amazing spider man #36”',
        'a coleção de pôsteres históricos da national agricultural library dos estados unidos',
        'oliveira lima nos estados unidos: impressões políticas e sociais (1896-1898)',
        'a representação da guerra do vietnã e a crítica política no filme nascido para matar, de stanley kubrick',
        'sobrevivendo ao teste do tempo: samuel huntington, sid meier’s civilization e o choque de civilizações',
        'propagandas comerciais e a relação entre atores brasileiros e norte-americanos em tempos de segunda guerra mundial: notas iniciais',
        'a literatura policial na história: o quarteto de los angeles, de james ellroy',
        'a indústria cultural na perspectiva do filme verdades e mentiras de orson welles',
        'disney e pocahontas: a reconstrução de um mito',
        'nacionalismo e cosmopolitismo: clivagens da direita nos estados unidos dos anos 1970',
        'a fratura do sonho americano em o grande gatsby de f. scott fitzgerald',
        'homeland e a representação da guerra ao terror na televisão',
        'march 19th, 1944: basquete universitário e a jim crow no sul dos estados unidos',
        'a prohibition unit e a lei seca',
        'a narrativa da nação na série/documentário “america: the story of us”',
    ),
    '6': ( # Anais 6
        'a criação da ideia de juventude e o surgimento do rock nos eua',
        'há sangue na terra onde o sol se põe: narrativas sobre two-spirits',
        'o fbi de john edgar hoover: história e historiografia',
        'a ruptura das esquerdas norte-americanas nos longos anos 1960: o conflito entre a lid e o sds',
        'william l. laurence e a construção da era atômica',
        'a new england cicero? a formação intelectual de john adams e sua relação com o pensamento clássico grego e romano',
        'duck and cover (1952): aprendendo a sobreviver na guerra fria e na era atômica',
        'literatura e pobreza nos anos 30: uma leitura de pergunte ao pó, de john fante',
    ),
}


def clean(word): # Limpa palavras
    # Ignora "palavras" compostas unicamente por números ou pontuação
    if all(char.isnumeric() or char in punctuation + '“”‘’' for char in word):
        return False

    # Remove pontuação e números
    for char in word:
        if char.isnumeric():
            word = word.replace(char, '')
        elif char in punctuation + '“”‘’':
            word = word.replace(char, '')
        
    # Ignora letras avulsas
    if len(word) < 2:
        return False
        
    # Transforma palavra em minúsculas
    word = word.lower()
        
    # Ignora palavras na lista de palavras ignoradas
    if word in ignore:
        return False
    
    return word


def extract(number): # Extrai texto de uma seção do documento
    
    doc = docx2python(f'Anais/anais_{number}.docx') # Documento aberto
    # Dicionário contendo pares onde chave = título do artigo e valor = número de ocorrências no texto
    titles = {title: 0 for title in article_titles[number]}
    article = [] # Artigo completo como lista de palavras

    '''
    Segundo a documentação do docx2python, os elementos são extraídos como
    uma série de listas aninhadas: document -> table -> row -> cell. O texto
    é encontrado no quarto nível de profundidade, daí a série de loops abaixo.
    '''
    for i in doc.body:
        for j in i:
            for k in j:
                for text in k:
                    if text: # Caso texto não esteja em branco

                        for title in titles: 
                            if title in text.lower(): # Checa se texto = algum título
                                titles[title] += 1 # Aumenta contagem de ocorrências do título
                                
                                if titles[title] == 2: # Caso seja a segunda ocorrência
                                    titles.pop(title) # Remove título da lista
                                    yield(article) # Retorna artigo completo
                                    article = [] # Esvazia lista para começar novo artigo 
                                break # Encerra loop de títulos
                        
                        text = text.split() # Divide texto em palavras
                        for word in text:
                            clean_word = clean(word) # Limpa cada palavra do texto
                            if clean_word: # Caso palavra não tenha sido ignorada
                                article.append(clean_word) # Adiciona palavra ao artigo

    yield(article) # Retorna último artigo


def generate_txt(iterator):
    with open('full_text.txt', mode= 'w', encoding='utf-8') as output: # Cria .txt
        idx = 1

        for article in iterator:
            if idx > 1:
                for word in article:
                    output.write(f'{word} ')
                output.write('\n\n')
            
            idx += 1