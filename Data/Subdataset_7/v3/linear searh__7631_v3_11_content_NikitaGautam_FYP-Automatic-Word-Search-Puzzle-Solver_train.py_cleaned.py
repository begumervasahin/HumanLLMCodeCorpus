import numpy as np
import scipy.special as sp
import random
import dill
class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = np.random.rand(self.b2, self.b1) - 0.5
        self.b6 = np.random.rand(self.b3, self.b2) - 0.5
        self.b7 = sp.expit
    def fonk2(self, inputs_list, targets_list):
        b8 = np.array(inputs_list, ndmin=2).T
        b9 = np.array(targets_list, ndmin=2).T
        b10 = np.dot(self.b5, b8)
        b11 = self.b7(b10)
        b12 = np.dot(self.b6, b11)
        b13 = self.b7(b12)
        b14 = b9 - b13
        b15 = np.dot(self.b6.T, b14)
        self.b6 += self.b4 * np.dot((b14 * b13 * (1.0 - b13)),
                                                                 b11.T)
        self.b5 += self.b4 * np.dot((b15 * b11 * (1.0 - b11)),
                                                                b8.T)
    def fonk3(self, inputs_list):
        b8 = np.array(inputs_list, ndmin=2).T
        b10 = np.dot(self.b5, b8)
        b11 = self.b7(b10)
        b12 = np.dot(self.b6, b11)
        b13 = self.b7(b12)
        return b13
def fonk4():
    b1 = 784
    b2 = 1500
    b3 = 26
    b4 = 0.005
    b16 = class1(b1, b2, b3, b4)
    with open("trainFinal.csv", 'r') as training_data:
        b17 = training_data.readlines()
        random.shuffle(b17)
        b18 = b17[:8000]
        b19 = b17[:]
    for _ in range(50):
        for record in b19:
            b20 = record.split(',')
            b21 = record.split(",")[0]
            b22 = int(b21.split("e0")[1]) - 10
            b20[0] = b22
            b8 = (np.asfarray(b20[1:]) / 255 * 0.99) + 0.01
            b9 = np.zeros(b3) + 0.01
            b9[b22 - 1] = 0.99
            b16.fonk2(b8, b9)
    print("Training completed.")
    with open('nn.dill', 'wb') as f:
        dill.dump(b16, f)
if b23 = = "__main__":
    fonk4()