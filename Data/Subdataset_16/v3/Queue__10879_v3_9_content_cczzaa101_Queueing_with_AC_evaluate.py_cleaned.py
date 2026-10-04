import os
import numpy as np
import copy
import random
from keras.models import load_model
import keras
a1 = 10
a2 = 20
class class1:
    def fonk1(self):
        self.b1 = np.zeros((2,))
        self.b2 = np.zeros((a1 * 2,))
        self.b3 = np.zeros((2,))
def fonk2(b14):
    b4 = np.random.choice(len(b14[0]), 1, p=b14[0])[0]
    return b4
class class2:
    def fonk3(self):
        self.b5 = load_model('trained_RNN')
        self.b5.compile(b6 = 'mse', optimizer='adam')
    def fonk4(self, state):
        b7 = copy.deepcopy(state)
        for i, sublist in enumerate(b7):
            b7[i] = [x + 1 for x in sublist]
            b7[i].extend([0] * (a1 - len(b7[i])))
        return [b7[0], b7[1]]
    def fonk5(self, state):
        b8 = self.fonk13(state)
        b8[0].append(-1)
        b8[1].append(-1)
        b9 = keras.preprocessing.sequence.pad_sequences(b8, a2, dtype='float32', padding='post', value=-100)
        return b9[0], b9[1]
    def fonk6(self, state, task):
        b10 = self.fonk5(state)
        return self.b5.predict([b10[0].reshape(1, len(b10[0]), 1), b10[1].reshape(1, len(b10[1]), 1)])
class class3:
    def fonk7(self):
        self.b5 = load_model('model_a_3_8')
        self.b5.compile(b6 = 'mse', optimizer='adam')
    def fonk8(self, state, b11 = False):
        b7 = copy.deepcopy(state)
        for i, sublist in enumerate(b7):
            b7[i] = [x + 1 for x in sublist]
            b7[i].extend([0] * (a1 - len(b7[i])))
        if not b11:
            return np.array([b7[0] + b7[1]])
        else:
            return np.array([b7[0], b7[1]])
    def fonk9(self, state, task):
        b10 = self.fonk8(state)
        return self.b5.predict([b10, task])
    def fonk10(self, state, task):
        a3 = 5
        b10 = self.fonk8(state, True)
        b7 = None
        for i in range(a1
            b12 = b10[0][i * a3: (i + 1) * a3]
            b13 = b10[1][i * a3: (i + 1) * a3]
            b14 = self.b5.predict([[list(b12) + list(b13)], task])
            b7 = b7 + b14 if b7 is not None else b14
        return b7 / (a1
    def fonk11(self, state, task):
        a3 = 5
        b10 = self.fonk8(state, True)
        b7 = None
        for i in range(a1 - a3 + 1):
            b12 = b10[0][i: i + a3]
            b13 = b10[1][i: i + a3]
            b14 = self.b5.predict([[list(b12) + list(b13)], task])
            b7 = b7 + b14 if b7 is not None else b14
        return b7 / (a1 - a3 + 1)
def fonk12():
    return [[], []]
def fonk13(state):
    b7 = copy.deepcopy(state)
    for i, sublist in enumerate(b7):
        b7[i] = [x + 1 for x in sublist]
        b7[i].extend([0] * (a1 - len(b7[i])))
    return np.array([b7[0] + b7[1]])
def fonk14(state):
    A, b15 = 0, 1
    p0a, b16 = 0.5, 1
    if A in state[0]:
        b16 *= 0.5
    p1a, b17 = 0.6, 0.6
    if b15 not in state[1]:
        p1a *= 0.5
    b18 = random.random()
    if state[0] and state[0][0] == A and b18 < p0a:
        state[0].pop(0)
    elif state[0] and b18 < b16:
        state[0].pop(0)
    if state[1] and state[1][0] == A and b18 < p1a:
        state[1].pop(0)
    elif state[1] and b18 < b17:
        state[1].pop(0)
def fonk15(state, b14, task):
    if len(state[b14]) < a1:
        state[b14].append(task)
        return 1
    return 0
def fonk16(task):
    b7 = [0, 0]
    b7[task] = 1
    return np.array([b7])
def fonk17():
    b5 = class3()
    random.seed()
    a4 = 0
    a5 = 10000
    with open('evaluated.txt', 'w') as f:
        b8 = 0
        for round in range(a5):
            if round % b19 = = 0 and round != 0:
                print(b8 / round)
            b20 = fonk12()
            a4 = 0
            for _ in range(40):
                for _ in range(2):
                    b21 = random.randrange(2)
                    b14 = b5.fonk9(b20, fonk16(b21))
                    b22 = fonk2(b14[b21] if len(b14) > 1 else b14)
                    if len(b20[b22]) >= a1:
                        b22 = 1 - b22
                    b23 = copy.deepcopy(b20)
                    b24 = fonk15(b23, b22, b21)
                    b20 = b23
                    a4 += b24
                    if b24 = = 0:
                        break
                fonk14(b20)
                if b24 = = 0:
                    break
            b8 += a4
            f.write(f"{a4}\n")
    print('avg b24: ', b8 / a5)
if b25 = = "__main__":
    fonk17()