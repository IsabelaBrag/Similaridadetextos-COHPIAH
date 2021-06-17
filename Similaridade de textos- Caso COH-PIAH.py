import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    #wal = float(input("Entre o tamanho médio de palavra:"))
    #ttr = float(input("Entre a relação Type-Token:"))
    #hlr = float(input("Entre a Razão Hapax Legomana:"))
    #sal = float(input("Entre o tamanho médio de sentença:"))
    #sac = float(input("Entre a complexidade média da sentença:"))
    #pal = float(input("Entre o tamanho medio de frase:"))
    wal = 4.325
    ttr = 0.7375
    hlr = 0.5875
    sal = 54.125
    sac = 2.0
    pal = 26.5625

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(ass_main, matriz_ass_input):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    lista_Sab = []
    soma_mod = 0
    if type(matriz_ass_input[0]) is list:
        for linha in range(len(matriz_ass_input)):
            for coluna in range(len(matriz_ass_input[linha])):
                soma_mod += abs(ass_main[coluna] - matriz_ass_input[linha][coluna])
            Sab = abs(soma_mod) / 6
            lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(matriz_ass_input)):      
            soma_mod += abs(ass_main[i] - matriz_ass_input[i])
        Sab = abs (soma_mod)/ 6
        return Sab

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    num_sentencas = 0
    soma_car_sentencas = 0

    frases = []
    for i in range(len(sentencas)):
        frase_aux = separa_frases(sentencas[i])
        frases.append(frase_aux)
        num_sentencas += 1
        soma_car_sentencas = soma_car_sentencas + len(sentencas[i])

    palavras = []
    num_frases = 0
    soma_car_frases = 0
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_aux = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_aux)
            num_frases += 1
            soma_car_frases += len(frases[linha][coluna])

    mtrx_para_lista = []
    #COLOCA O QUE ESTÁ NA EM MATRIZ PARA UMA LISTA
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            mtrx_para_lista.append(palavras[linha][coluna])
    palavras = mtrx_para_lista[:]

    total_letras = 0
    num_tot_palavras = len(palavras)
    #CALCULA A QUANTIDADE DE LETRAS
    for lin in range(len(palavras)):
        for col in range(len(palavras[lin])):
            total_letras = total_letras + len(str(palavras[lin][col]))
    
    tam_medio_pal = total_letras / num_tot_palavras
    type_token = n_palavras_diferentes(palavras) / num_tot_palavras
    razao_hapax_lego = n_palavras_unicas(palavras) / num_tot_palavras
    tam_medio_sent = soma_car_sentencas / num_sentencas
    comp_media_sent = num_frases / num_sentencas
    tam_medio_frase = soma_car_frases / num_frases
    
    return [tam_medio_pal, type_token, razao_hapax_lego, tam_medio_sent, comp_media_sent, tam_medio_frase]


def avalia_textos(textos, assinaturaMain):
    aux_ass_com = assinaturaMain[:]
    aux_ass_com.sort()
    for indice in range(len(assinaturaMain)):
        if aux_ass_com[0] == assinaturaMain[indice]:
            copiah = indice
    return copiah-1

'''Minhas funções'''
def main():
    assinaturaMain = le_assinatura()
    textos = le_textos()

    return print("O autor do texto " , avalia_textos(textos, assinaturaMain), " está infectado com COH-PIAH")
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass
main()
