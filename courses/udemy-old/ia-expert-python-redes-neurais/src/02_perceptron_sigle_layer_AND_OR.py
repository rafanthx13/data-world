# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:50:31 2018

@author: Rafael
"""

# Perceptron Single Layer Com Reajuste de Peso (AND LOGIC)

# np.asarray 
# abs => to is not negative
# in python, a variable defined before of function can be used inside, but
#   what is modified will be only in your scope
# The code is not otimizated, it do twice updateds weights, everytime

import numpy as np

# AND LOGIC - Enable this Line to Run to AND LOGIC
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
expecteds_outputs =  np.array([0, 0, 0, 1])

# OR LOGIC - Enable this Line to Run to OR LOGIC
# inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
# expecteds_outputs =  np.array([0, 1, 1, 1])

# XOR LOGIC - Enable this Line to Run to XOR LOGIC -> Will exit ERRO
#inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
#expecteds_outputs =  np.array([0, 1, 1, 0])

weights = np.array([0.0, 0.0])
learning_rate = 0.1

def step_function(soma):
    if(soma >= 1):
        return 1
    return 0

def calcule_output(record):
    s = record.dot(weights)
    return step_function(s)

def trainning():
    erro_total = 1
    while(erro_total != 0):
        erro_total = 0
        for i in range(len(expecteds_outputs)):
            output_calculated = calcule_output(np.asarray(inputs[i]))
            erro = abs(expecteds_outputs[i] - output_calculated)
            erro_total += erro
            # UPDATE Weights
            for j in range(len(weights)):
                weights[j] = weights[j] + (learning_rate * inputs[i][j] * erro)
                print("Updated Weight: " + str(weights[j]))
            print('Total Erros: ' + str(erro_total))
            
trainning()
print("Neural Net Trained: Testing it")
print("1 input (0,0) ==>", calcule_output(inputs[0]))
print("2 input (0,1) ==>", calcule_output(inputs[1]))
print("3 input (1,0) ==>", calcule_output(inputs[2]))
print("4 input (1,1) ==>", calcule_output(inputs[3]))
print('Weights Useds: ' + str(weights[0]) + ', ' + str(weights[1]))