
import random
import copy

'''
Definição das funções do Algoritmo Genético
'''

def fitness(cromossomo):
    fitness = 0
    n = len(cromossomo)
    for i in range(n):
        for j in range(n):
            # A função abs retorna o valor absoluto do argumento
            if(abs(i-j) == abs(cromossomo[i]- cromossomo[j]) and i != j):
                fitness = fitness+1
    return fitness//2


def mutacao(cromossomo):
    tam_cromossomo = len(cromossomo)
    mult1 = random.randint(0, tam_cromossomo-1)
    mult2 = random.randint(0, tam_cromossomo-1)
    dna = cromossomo[mult1]
    cromossomo[mult1] = cromossomo[mult2]
    cromossomo[mult2] = dna
    return cromossomo

'''
Recebe os cromossomos do pai1 e do pai2
'''
def cruzamento(pai1, pai2):
    tam_pai1 = len(pai1)
    pos = random.randint(0, tam_pai1  - 1)
    # É necessário copiar para não alterar as referências das listas de cromossomos
    filho1 = copy.deepcopy(pai1)
    filho2 = copy.deepcopy(pai2)
    for i in range(tam_pai1 ):
        check1 = 0
        check2 = 0
        for j in range(pos):
            if(pai2[i] == pai1[j]):
                check1 = 1
            if(pai1[i] == pai2[j]):
                check2 = 1
        if(check1 == 0):
            filho1[pos] = pai2[i]
        if(check2 == 0):
            filho2[pos] = pai1[i]

    return [filho1, filho2]

def selecionaPais(populacao, k):
    return [torneio(populacao, k) for _ in range(2)]

def torneio(populacao, k):
    if(k > len(populacao)):
        raise Exception("k maior que o tamanho da populacao")

    lst_torneio = [copy.deepcopy(populacao[random.randint(
        0, len(populacao) - 1)]) for _ in range(k)]

    lst_torneio.sort(key=lambda e: fitness(e), reverse=False)

    return copy.deepcopy(lst_torneio[0])

def nova_geracao(pop, novos):
    aptidao = []
    pop.extend(novos)