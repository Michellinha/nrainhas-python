'''
-------------------------------------------------
Universidade Federal de Minas Gerais 
Ambiente de Computação 2021.1

Código desenvolvido por: Michelle Gomes Pereira
Projeto: Problema das N-Rainhas com Algoritmo Genético

O problema das N-rainhas consiste em encontrar todas as combinações possíveis de N rainhas 
num tabuleiro de dimensão N por N tal que nenhuma das rainhas ataque qualquer outra. Duas 
rainhas atacam-se uma à outra quando estão na mesma linha, na mesma coluna ou na mesma diagonal 
do tabuleiro. 
-------------------------------------------------
'''
# Importando módulos necessários para a implementação do Algoritmo Genético.
 
from itertools import permutations
import random
import operacoes_ag

'''

Primeira etapa: Definição dos parâmetros de execução do Algoritmo Genético

'''

pressao_seletiva = 5
tam_tabuleiro = 8   # NRainhas
tam_populacao = 500
geracoes = tam_populacao

'''

Segunda etapa: Geração da População inicial

'''

# Na geração da população inicial é utilizado uma função para permutação de inteiros 
# (permutations), que corresponde a representação das possiveis configurações de soluções 
# candidatas. Tais configurações são denominadas de fenótipo, enquanto cada posição assumida 
# pela rainha é denominada de genótipo. A função de permutação é necessária para evitar colisões
# e eliminar as seguintes restrições: linhas, colunas de diagonais.
# Melhorando meu espaço de busca
permutacao = permutations([x for x in range(1, tam_tabuleiro + 1)])

individuo = []
populacao = []
count = 0
for _ in range(tam_populacao):
    for elem in permutacao:
        count += 1
        gens = []
        for gen in elem:
            gens.append(gen)
        individuo.append(gens)
    populacao.append(individuo[random.randint(0, count)])

print("população inicial: ", populacao)


'''
Algoritmo Genético
'''

try:
    for i in range(geracoes):
        # Condição de parada
        if(operacoes_ag.fitness(populacao[i]) == 0):
            solucao = populacao[i]
            print("A solução das posições no tabuleiro:\n")
            print(solucao)
            break
        
        #Etapa de seleção dos pais 
        pais = operacoes_ag.selecionaPais(populacao, pressao_seletiva)

        filhos = operacoes_ag.cruzamento(pais[0],pais[1])

        filhos[0] = operacoes_ag.mutacao(filhos[0])
        filhos[1] = operacoes_ag.mutacao(filhos[1])

        operacoes_ag.nova_geracao(populacao, filhos)
except Exception as e:
    print(e)




