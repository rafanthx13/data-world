# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:23:38 2018

@author: Rafael
"""

# Isso so serve para monstar a estrutura

# Importa um FeedForward
from pybrain.structure import FeedForwardNetwork
# LinearLaye => Camada de Entrada
# SigmoidLaye = Camada  em que o dado passa pela Sigmoide (Oculta e Intermedia)
# Bias => Vies
from pybrain.structure import LinearLayer, SigmoidLayer, BiasUnit
from pybrain.structure import FullConnection

# Estrutura da Rede
rede = FeedForwardNetwork()

# Camdas Sepradas
camadaEntrada = LinearLayer(2) # 2 entradas
camadaOculta = SigmoidLayer(3) # 3 neuronios na camda oculta
camadaSaida = SigmoidLayer(1)

# UNidades de Bias
bias1 = BiasUnit()
bias2 = BiasUnit()

# Inserindo essas camdas na estutura da rede
rede.addModule(camadaEntrada)
rede.addModule(camadaOculta)
rede.addModule(camadaSaida)
rede.addModule(bias1)
rede.addModule(bias2)

# Ligaçâo entre as camdas (vai ligar os neurosios do @1 para todos do @2)
entradaOculta = FullConnection(camadaEntrada, camadaOculta)
ocultaSaida = FullConnection(camadaOculta, camadaSaida)
# bias tambem é ligado, nao tem como juntar a camdaEntraa
biasOculta = FullConnection(bias1, camadaOculta)
biasSaida = FullConnection(bias2, camadaSaida)

# Efitivamente vai construir e vai fazer
# ele já poe os pesos
rede.sortModules()

print(rede)
# esse .prams mostra os pesos das camdas
print(entradaOculta.params)
print(ocultaSaida.params)
print(biasOculta.params)
print(biasSaida.params)


