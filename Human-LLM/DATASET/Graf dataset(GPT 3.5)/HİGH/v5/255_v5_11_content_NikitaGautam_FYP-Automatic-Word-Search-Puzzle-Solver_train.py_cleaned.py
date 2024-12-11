import numpy as np
from scipy.special import expit as sigmoid
import random
import dill
class class1:
    def fonk1(self, b1, b2, b3, a1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = a1
        self.b5 = np.random.rand(self.b2, self.b1) - 0.5
        self.b6 = np.random.rand(self.b3, self.b2) - 0.5
    def fonk2(self, inputs_list, targets_list):
        b7 = np.array(inputs_list, ndmin=2).T
        b8 = np.array(targets_list, ndmin=2).T
        b9 = np.dot(self.b5, b7)
        b10 = sigmoid(b9)
        b11 = np.dot(self.b6, b10)
        b12 = sigmoid(b11)
        b13 = b8 - b12
        b14 = np.dot(self.b6.T, b13)
        self.b6 += self.b4 * np.dot(b13 * b12 * (1.0 - b12),
                                                       np.transpose(b10))
        self.b5 += self.b4 * np.dot(b14 * b10 * (1.0 - b10),
                                                      np.transpose(b7))
    def fonk3(self, inputs_list):
        b7 = np.array(inputs_list, ndmin=2).T
        b9 = np.dot(self.b5, b7)
        b10 = sigmoid(b9)
        b11 = np.dot(self.b6, b10)
        b12 = sigmoid(b11)
        return b12
def fonk4():
    b1 = 784
    b2 = 1500
    b3 = 26
    a1 = 0.005
    b15 = class1(b1, b2, b3, a1)
    with open("/Users/Nikita/PycharmProjects/FYPPuzzle/static/trainFinal.csv", 'r') as training_data:
        b16 = training_data.readlines()
        random.shuffle(b16)
        b17 = b16[0:8000]
        b18 = b16[0:]
    for epoch in range(50):
        for record in b18:
            b19 = record.split(',')
            b20 = record.split(",")[0]
            b21 = int(b20.split("e0")[1]) - 10
            b19[0] = b21
            b7 = (np.asfarray(b19[1:]) / 255 * 0.99) + 0.01
            b8 = np.zeros(b3) + 0.01
            b8[b21 - 1] = 0.99
            b15.fonk2(b7, b8)
    print("Neural network trained")
    with open('/Users/Nikita/PycharmProjects/FYPPuzzle/static/nn.dill', 'wb') as f:
        dill.dump(b15, f)
fonk4()