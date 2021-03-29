# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:26:48 2021

@author: tobia

This is the first test building the groups neural network Jarvis
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)

traning_inputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

traning_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1))-1

print('random starting synaptic weights')
print(synaptic_weights)

for iteration in range(200000):
    input_layer = traning_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    
    error = traning_outputs - outputs
    adjustments = error * sigmoid_derivative(outputs)
    synaptic_weights += np.dot(input_layer.T, adjustments)

print('synaptic weights after traning')
print(synaptic_weights)

print('outputs after training')
print(outputs)