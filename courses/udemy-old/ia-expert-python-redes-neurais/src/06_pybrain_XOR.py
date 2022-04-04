# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:41:21 2018

XOR Usando PYBRAIN

@author: Rafael
"""
# esse shorcuts serve para fazermos um atalho
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.structure.modules import SigmoidLayer

# 2 neuroions na camada de entrada, 3 na do meio e 1 na de saidas
rede = buildNetwork(2, 3, 1)
# Teremos 2 atributos para prever e uma classe
base = SupervisedDataSet(2, 1)
# Base de dados
base.addSample((0, 0), (0, ))
base.addSample((0, 1), (1, ))
base.addSample((1, 0), (1, ))
base.addSample((1, 1), (0, ))
#print(base['input'])
#print(base['target'])

# Para visualizar
'''rede = buildNetwork(2, 3, 1, outclass = SoftmaxLayer,
                    hiddenclass = SigmoidLayer, bias = False)
print(rede['in'])
print(rede['hidden0'])
print(rede['out'])
print(rede['bias'])'''
# Fazer o trienmaento, e com essa classe
# passa a rede, dataset, learning_rate, momentum)
treinamento = BackpropTrainer(rede, dataset = base, learningrate = 0.01,
                              momentum = 0.06)
# Definido epocas e executando treinamento
epocas = 10000
for i in range(1, epocas):
    erro = treinamento.train()
    if i % 1000 == 0:
        # Vou mostrar o erro de mil em mill
        print("Erro: %s" % erro)

# testando a rede, vai classificar os dado que eu passar
# testando: lembre-se, por usar a sigmoide, nao chega a ser 0 ou 1 exatamente
# Se quiser usar sigmoide, coloca um round, mas sim, EXECUTA CORRETAMENTE
        
print(rede.activate([0, 0]))
print(rede.activate([1, 0]))
print(rede.activate([0, 1]))
print(rede.activate([1, 1]))