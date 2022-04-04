# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:45:53 2018

@author: Rafael
"""

import numpy as np

# A base de dados ja esta no ski-laerning
from sklearn import datasets

base = datasets.load_breast_cancer()

entradas = base.data

valores_saidas = base.target
# vai ser necessario converter para algo mais simples
saidas = np.empty([569, 1], dtype = int)
# ants, so iniicializou, agora, vamos por
for i in range(569):
    saidas[i] = valores_saidas[i]

# Os pesos na verdade sao iniciados aleartorios
len_entradas = 30
pesos0 = 2*np.random.random((len_entradas,3)) - 1
pesos1 = 2*np.random.random((3,1)) - 1


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))
    # Se a entrada for muito alt
    
# dereivada da sigmoide
def sigmoide_derivada(sig):
    return sig * (1 - sig)

momento = 1
taxa_aprendizagem = 0.5

epocas = 100

print('Pesos Iniciais da Camada de Saida:\n', pesos1)
print('Pesos Iniciais da Camada Oculta:\n', pesos0)

for i in range(epocas):
    camada_entrada = entradas
    # ao usar np.dot do numpy, ele faz a soma e multiplicaçao
    somaSinapse0 = np.dot(camada_entrada, pesos0)
    """
    numpy.dot ==> caluclo complexo de algebra linear => Multiplicaçao de Matriz
    ==> Esses calculos sao apra a primiera interacao
    somaSinapse
        Quantidade de linhas => Para cada entrada, entao, sao 4 entradas
        Quantidade de Colunas => Para cada Neuronio, sao 3 neuronios
        # Esta imploeto, preenha depoois
        1 linha [0,0] => [0*]
        2 linha [0,1] => 
        3 linha [1,0] =>
        4 linha [1,1] => [1*-0.424 + 1*0.358] [1*0.740 + 1*-0.577] [1*-0.961 + 1*-0.469]
    """
    # A aplicaçao da sigmoide sobre o array implica em aplicar essa funçao a cada elemento do array
    # ou seja, a saida é aray 3x4 ==> 3 neurinos e 4 entradas
    camada_oculta = sigmoid(somaSinapse0)
    
    
    somaSinapse1 = np.dot(camada_oculta, pesos1)
    camada_saida = sigmoid(somaSinapse1)
    
    
    erro_camada_saida = saidas - camada_saida
    # Quantidade de erro que existe na minha rede neural
    # se eu quiser acerto é 1 - isso daqui
    media_absoluta = np.mean(np.abs(erro_camada_saida))
    print('Erro['+str(i)+']:', media_absoluta)
    
    derivada_saida = sigmoide_derivada(camada_saida) # acamada de saida é a ativaçâo final de cada registro
    delta_saida = erro_camada_saida * derivada_saida
    
    #       Clculod Da derivada de saida da camda Oculta
    # vamos colocar a traposta pois asism vai conseguir executar o calculo 
    # de algeba lienar que queroms
    # nao cosegue fazer essa linha pois, pois seria com pesos 1 e presisa converter pesos1 para trapsorta
    # pesos.T ==>   Trapsota => vai converter de 3 linhas para 4 colunas
    # Isos é necessario para fazre o dot_product de matrizes
    delta_saida_x_peso = delta_saida.dot(pesos1.T)
    delta_camada_oculta = delta_saida_x_peso * sigmoide_derivada(camada_oculta)
    
    # Atualização dos pesos da camada de Saida (BACKPROPAGATION)
    # OBS: O que estou achadno estranho é que, a parte da (entrada * delta) ele faz para todos os dados
    camada_oculta_transposta = camada_oculta.T
    pesos_novos_1 = camada_oculta_transposta.dot(delta_saida)
    pesos1 = (pesos1 * momento) + (pesos_novos_1 * taxa_aprendizagem)
    
    # Atualizaçâo dos pesos da camda oculta (BACKPROPAGATION)
    camada_entrada_transposta = camada_entrada.T
    pesos_novos_0 = camada_entrada_transposta.dot(delta_camada_oculta)
    pesos0 = (pesos0 * momento) + (pesos_novos_0 * taxa_aprendizagem)
        
print('Happy End')
print('Pesos da Camada de Saida:\n', pesos1)
print('Pesos da Camada Oculta:\n', pesos0)

# Por usar sigmoide, nâo vai chegar à exatamente 
    