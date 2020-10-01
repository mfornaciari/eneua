import string

texto = open('Anais-III-ENEUA.txt').read().lower()
for c in string.punctuation:
    texto = texto.replace(c, ' ')

palavras = texto.split()
ignore = ["eua", "EUA", "USA", "forma", "durante", "américa", "america", "estadunidense", "estados", "i", "momento", "período", "university", "”", "anais", "press", "momento", "american", "americana", "press", "então", "entao", "unidos", "parte", "assim", "american" "i", "norte", "anos", "Estados", "Unidos", "Americano", "Americana", "americano", "Americano", "the", "and", "-", "são", "–", "in", "of", "outros", "desde", "to", "além", "ver", "1", "is", "s", "org", "apenas", "that", "new", "1", "pos", "vez", "são" "meu","mai", "de", "diversos", "outro", "p", "_", "sob", "outra", "outras", "após", "caso" "outros", "a","o","que","e","do","da","em","um","para","é","com","não","uma","os","no","se","na","por","mais","partiu","partir","as","dos","como","mas","foi","ao","ele","das","tem","à","seu","sua","ou","ser","quando","muito","há","nos","já","está","eu","também","só","pelo","pela","até","isso","ela","entre","era","depois","sem","mesmo","aos","ter","seus","quem","nas","me","esse","eles","estão","você","tinha","foram","essa","num","nem","suas","meu","às","minha","têm","numa","pelos","elas","havia","seja","qual","será","nós","tenho","lhe","deles","essas","esses","pelas","este","fosse","dele","tu","te","vocês","vos","lhes","meus","minhas","teu","tua","teus","tuas","nosso","nossa","nossos","nossas","dela","delas","esta","estes","estas","aquele","aquela","aqueles","aquelas","isto","aquilo","estou","está","estamos","estão","estive","esteve","estivemos","estiveram","estava","estávamos","estavam","estivera","estivéramos","esteja","estejamos","estejam","estivesse","estivéssemos","estivessem","estiver","estivermos","estiverem","hei","há","havemos","hão","houve","houvemos","houveram","houvera","houvéramos","haja","hajamos","hajam","houvesse","houvéssemos","houvessem","houver","houvermos","houverem","houverei","houverá","houveremos","houverão","houveria","houveríamos","houveriam","sou","somos","era","éramos","eram","fui","foi","fomos","foram","fora","fôramos","seja","sejamos","sejam","fosse","fôssemos","fossem","for","formos","forem","serei","será","seremos","serão","seria","seríamos","seriam","tenho","tem","temos","tém","tinha","tínhamos","tinham","tive","teve","tivemos","tiveram","tivera","tivéramos","tenha","tenhamos","tenham","tivesse","tivéssemos","tivessem","tiver","tivermos","tiverem","terei","terá","teremos","terão","teria","teríamos","teriam", "cit", "op", "segundo","através", "Segundo", "Contudo", "sobre", "onde", "dessa", "sendo", "ainda","grande"]

wc = {}
for p in palavras:
    if p in ignore:
        wc[p] = 0
    if p in wc:
        wc[p] += 1
    else:
        wc[p] = 1

##def contador(dupla):
##    return dupla[1]

duplas = sorted(wc.items(),
                key=lambda dupla:dupla[1],
                reverse=True)
for dupla in duplas[:20]:
    print (dupla[0], dupla[1])
