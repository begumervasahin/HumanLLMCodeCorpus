from __future__ import division
import numpy
import scipy.special
import random
import dill
class class1:
    def fonk1(self, b1, b2, b3, a1):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = a1
        self.b5 = (numpy.random.rand(self.b2, self.b1) - 0.5)
        self.b6 = (numpy.random.rand(self.b3, self.b2) - 0.5)
        self.b7 = lambda x: scipy.special.expit(x)
    def fonk2(self, inputs_list, targets_list):
        b8 = numpy.array(inputs_list, ndmin=2).T
        b9 = numpy.array(targets_list, ndmin=2).T
        b10 = numpy.dot(self.b5, b8)
        b11 = self.b7(b10)
        b12 = numpy.dot(self.b6, b11)
        b13 = self.b7(b12)
        b14 = b9 - b13
        b15 = numpy.dot(self.b6.T, b14)
        self.b6 += self.b4 * numpy.dot((b14 * b13 * (1.0 - b13)),
                                                         numpy.transpose(b11))
        self.b5 += self.b4 * numpy.dot((b15 * b11 * (1.0 - b11)),
                                                        numpy.transpose(b8))
    def fonk3(self, inputs_list):
        b8 = numpy.array(inputs_list, ndmin=2).T
        b10 = numpy.dot(self.b5, b8)
        b11 = self.b7(b10)
        b12 = numpy.dot(self.b6, b11)
        b13 = self.b7(b12)
        return b13
def fonk4():
    b1 = 784
    b2 = 1500
    b3 = 26
    a1 = 0.005
    b16 = class1(b1, b2, b3, a1)
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
            b8 = (numpy.asfarray(b20[1:]) / 255 * 0.99) + 0.01
            b9 = numpy.zeros(b3) + 0.01
            b9[b22 - 1] = 0.99
            b16.fonk2(b8, b9)
    print("Trained")
    with open('nn.dill', 'wb') as f:
        dill.dump(b16, f)
if b23 = = "__main__":
    fonk4()