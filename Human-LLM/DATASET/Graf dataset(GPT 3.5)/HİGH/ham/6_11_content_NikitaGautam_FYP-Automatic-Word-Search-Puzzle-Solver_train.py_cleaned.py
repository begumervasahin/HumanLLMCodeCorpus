from __future__ import division
import numpy
import scipy.special
import random
import dill
class class1:
    def fonk1(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.b1 = inputnodes
        self.b2 = hiddennodes
        self.b3 = outputnodes
        self.b4 = learningrate
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
    b17 = open("/Users/Nikita/PycharmProjects/FYPPuzzle/static/trainFinal.csv", 'r')
    b18 = b17.readlines()
    random.shuffle(b18)
    b19 = b18[0:8000]
    b20 = b18[0:]
    b17.close()
    a2 = 0
    for a2 in (0, 50):
        for record in b20:
            b21 = record.split(',')
            b22 = record.split(",")[0]
            b23 = int(b22.split("e0")[1]) - 10
            b21[0] = b23
            b8 = (numpy.asfarray(b21[1:]) / 255 * 0.99) + 0.01
            b9 = numpy.zeros(b3) + 0.01
            b9[b23 - 1] = 0.99
            b16.fonk2(b8, b9)
    print("trained")
    with open('/Users/Nikita/PycharmProjects/FYPPuzzle/static/nn.dill', 'wb') as f:
        dill.dump(b16, f)