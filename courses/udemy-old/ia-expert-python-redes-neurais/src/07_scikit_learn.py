# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:22:37 2018

@author: Rafael
"""

from sklearn.neural_network import MLPClassifier
from sklearn import datasets

iris = datasets.load_iris()

entradas = iris.data
saidas = iris.target

# verbose = True ==> Significa que vai mostar um print
# @tol => Tolerancia, caso sua rede nao estiver aprendenzo, vc diminui esse @tol
# Documentação: http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
redeNeural = MLPClassifier(verbose = True,
                           max_iter = 1000,
                           tol = 0.0001,
                           activation = 'logistic',
                           learning_rate = 0.01)
redeNeural.fit(entradas, saidas)
# predizer para um valor
redeNeural.predict([[5, 7.2, 5.1, 2.2]])