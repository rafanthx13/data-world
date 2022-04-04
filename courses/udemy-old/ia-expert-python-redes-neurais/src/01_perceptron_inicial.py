# -*- coding: utf-8 -*-
"""
Rafael Assis 16.05.2018

#       IDE - SPyder

# Para Executar:  <F5>
# Executar Trechos de: <F9>
# <TAB> auto-complete como Jupyter
# Possui consoles Iteractive de Python, como Jupyter, é ajanela abaixo a 
#   direita
# Existe 4 Janelas:
    # 1 Explorados de Variaveis, Exploradodr de Arquivos Ajuda e IPython
    # Os mehores sao Exploradorde de variaveis e o iteravivo
"""


############################################################################
# Executando primeiro exemplo
entradas = [1,7,5]
pesos = [0.8, 0.1, 0]

# definido SOMA
def soma(entradas, pesos):
    s = 0
    for i in range(3):
        # print(entradas[i])
        # print(pesos[i])
        s += entradas[i] * pesos[i]
    return s

s = soma(entradas, pesos)
print(s)

def stepfunction(soma):
    if(soma >= 1):
        return 1
    return 0

r = stepfunction(s)
    
