import os
import copy
import random
import numpy as np
from keras.models import load_model
import keras
a1 = 10
a2 = 20
class class1:
    def fonk1(self):
        self.b1 = np.zeros((2,))
        self.b2 = np.zeros((a1 * 2,))
        self.b3 = np.zeros((2,))
def fonk2(b13):
    b4 = np.random.choice(len(b13[0]), 1, p=b13[0])[0]
    return b4
class class2:
    def fonk3(self):
        self.b5 = load_model('trained_RNN')
        self.b5.compile(b6 = 'mse', optimizer='adam')
    def fonk4(self, state):
        b7 = copy.deepcopy(state)
        for i in range(len(b7)):
            b7[i] = [x + 1 for x in b7[i]]
            while len(b7[i]) < a1:
                b7[i].append(0)
        return [b7[0], b7[1]]
    def fonk5(self, state):
        b8 = self.fonk4(state)
        b8[0].append(-1)
        b8[1].append(-1)
        b8 = keras.preprocessing.sequence.pad_sequences(b8, a2, 'float32', 'post', 'post', value=-100)
        return b8[0], b8[1]
    def fonk6(self, state, task):
        b9 = self.fonk5(state)
        return self.b5.predict([b9[0].reshape(1, len(b9[0]), 1), b9[1].reshape(1, len(b9[1]), 1)])
class class3:
    def fonk7(self):
        self.b5 = load_model('model_a_3_8')
        self.b5.compile(b6 = 'mse', optimizer='adam')
    def fonk8(self, state, b10 = False):
        b7 = copy.deepcopy(state)
        for i in range(len(b7)):
            b7[i] = [x + 1 for x in b7[i]]
            while len(b7[i]) < a1:
                b7[i].append(0)
        if not b10:
            return np.array([b7[0] + b7[1]])
        else:
            return np.array([b7[0], b7[1]])
    def fonk9(self, state, task):
        b9 = self.fonk8(state)
        return self.b5.predict([b9, task])
    def fonk10(self, state, task):
        a3 = 5
        b9 = self.fonk8(state, True)
        b7 = None
        for i in range(a1
            b11 = b9[0][i * a3:(i + 1) * a3]
            b12 = b9[1][i * a3:(i + 1) * a3]
            b13 = self.b5.predict([[list(b11) + list(b12)], task])
            b7 = b7 + b13 if b7 is not None else b13
        return b7 / (a1
    def fonk11(self, state, task):
        a3 = 5
        b9 = self.fonk8(state, True)
        b7 = None
        for i in range(a1 - a3 + 1):
            b11 = b9[0][i:i + a3]
            b12 = b9[1][i:i + a3]
            b13 = self.b5.predict([[list(b11) + list(b12)], task])
            b7 = b7 + b13 if b7 is not None else b13
        return b7 / (a1 - a3 + 1)
def fonk12():
    return [[], []]
def fonk13(state):
    A, b14 = 0, 1
    p0a, b15 = 0.5, 1.0
    p1a, b16 = 0.6, 0.6
    if A in state[0]:
        b15 *= 0.5
    if b14 not in state[1]:
        p1a *= 0.5
    b17 = random.random()
    if len(state[0]) > 0:
        if state[0][0] == A:
            if b17 < p0a:
                state[0].pop(0)
        else:
            if b17 < b15:
                state[0].pop(0)
    if len(state[1]) > 0:
        if state[1][0] == A:
            if b17 < p1a:
                state[1].pop(0)
        else:
            if b17 < b16:
                state[1].pop(0)
def fonk14(state, b13, task):
    if len(state[b13]) >= a1:
        return 0
    state[b13].append(task)
    return 1
def fonk15(task):
    b7 = [0, 0]
    b7[task] = 1
    return np.array([b7])
def fonk16():
    b5 = class3()
    random.seed()
    a4 = 0
    b8 = 0
    a5 = 10000
    with open('evaluated.txt', 'w') as f:
        for round in range(a5):
            if round % b18 = = 0 and round != 0:
                print(b8 / round)
            b19 = fonk12()
            a4 = 0
            for ind in range(40):
                for task_ind in range(2):
                    b20 = random.randrange(2)
                    b13 = b5.fonk9(b19, fonk15(b20))
                    if len(b13) > 1:
                        b21 = fonk2(b13[b20])
                    else:
                        b21 = fonk2(b13)
                    if len(b19[b21]) >= a1:
                        b21 = 1 - b21
                    b22 = copy.deepcopy(b19)
                    b23 = fonk14(b22, b21, b20)
                    b19 = b22
                    a4 += b23
                    if b23 = = 0:
                        break
                fonk13(b19)
                if b23 = = 0:
                    break
            b8 += a4
            f.write(f'{a4}\n')
    print('Average b23: ', b8 / a5)
if b24 = = "__main__":
    fonk16()