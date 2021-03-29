# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:08:41 2021

@author: tobia
"""

import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
        
    def train(self, traning_inputs, traning_outputs, traning_iterations):
        for iteration in range(traning_iterations):
            output = self.think(traning_inputs)
            error = traning_outputs - output
            adjustments = np.dot(traning_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
            
    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

if __name__ == "__main__":
    neural_network = NeuralNetwork()
    
    print("Random synaptic weights:")
    print(neural_network.synaptic_weights)
    
    traning_inputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

    traning_outputs = np.array([[0,1,1,0]]).T
    
    neural_network.train(traning_inputs, traning_outputs, 100000)
    
    print("Synaptic weights after traning:")
    print(neural_network.synaptic_weights)
    
    A = str(input('Input 1:'))
    B = str(input('Input 2:'))
    C = str(input('Input 3:'))
    
    print("New situation: input data = ", A, B, C)
    print("Output data")
    print(neural_network.think(np.array([A, B, C])))
    
    
    