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
def fonk2(b15):
    b4 = np.random.choice(len(b15[0]), 1, p=b15[0])[0]
    return b4
class class2:
    def fonk3(self):
        self.b5 = load_model('trained_RNN')
        self.b5.compile(b6 = 'mse', optimizer='adam')
    def fonk4(self, state):
        b7 = copy.deepcopy(state)
        for b8 in b7:
            b8 = [x + 1 for x in b8]
            b8.extend([0] * (a1 - len(b8)))
        return [b7[0], b7[1]]
    def fonk5(self, state):
        b9 = self.fonk13(state)
        b9[0].append(-1)
        b9[1].append(-1)
        b10 = keras.preprocessing.sequence.pad_sequences(b9, a2, dtype='float32', padding='post', value=-100)
        return b10[0], b10[1]
    def fonk6(self, state, task):
        b11 = self.fonk5(state)
        return self.b5.predict([b11[0].reshape(1, len(b11[0]), 1), b11[1].reshape(1, len(b11[1]), 1)])
class class3:
    def fonk7(self):
        self.b5 = load_model('model_a_3_8')
        self.b5.compile(b6 = 'mse', optimizer='adam')
    def fonk8(self, state, b12 = False):
        b7 = copy.deepcopy(state)
        for b8 in b7:
            b8 = [x + 1 for x in b8]
            b8.extend([0] * (a1 - len(b8)))
        if not b12:
            return np.array([b7[0] + b7[1]])
        else:
            return np.array([b7[0], b7[1]])
    def fonk9(self, state, task):
        b11 = self.fonk8(state)
        return self.b5.predict([b11, task])
    def fonk10(self, state, task):
        a3 = 5
        b11 = self.fonk8(state, True)
        b7 = None
        for i in range(a1
            b13 = b11[0][i * a3: (i + 1) * a3]
            b14 = b11[1][i * a3: (i + 1) * a3]
            b15 = self.b5.predict([[list(b13) + list(b14)], task])
            b7 = b7 + b15 if b7 is not None else b15
        return b7 / (a1
    def fonk11(self, state, task):
        a3 = 5
        b11 = self.fonk8(state, True)
        b7 = None
        for i in range(a1 - a3 + 1):
            b13 = b11[0][i: i + a3]
            b14 = b11[1][i: i + a3]
            b15 = self.b5.predict([[list(b13) + list(b14)], task])
            b7 = b7 + b15 if b7 is not None else b15
        return b7 / (a1 - a3 + 1)
def fonk12():
    return [[], []]
def fonk13(state):
    b7 = copy.deepcopy(state)
    for b8 in b7:
        b8 = [x + 1 for x in b8]
        b8.extend([0] * (a1 - len(b8)))
    return np.array([b7[0] + b7[1]])
def fonk14(state):
    A, b16 = 0, 1
    p0a, b17 = 0.5, 1
    if A in state[0]:
        b17 *= 0.5
    p1a, b18 = 0.6, 0.6
    if b16 not in state[1]:
        p1a *= 0.5
    b19 = random.random()
    if state[0] and state[0][0] == A and b19 < p0a:
        state[0].pop(0)
    elif state[0] and b19 < b17:
        state[0].pop(0)
    if state[1] and state[1][0] == A and b19 < p1a:
        state[1].pop(0)
    elif state[1] and b19 < b18:
        state[1].pop(0)
def fonk15(state, b15, task):
    if len(state[b15]) < a1:
        state[b15].append(task)
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
        b9 = 0
        for round in range(a5):
            if round % b20 = = 0 and round != 0:
                print(b9 / round)
            b21 = fonk12()
            a6 = 1.0
            a4 = 0
            for ind in range(40):
                for task_ind in range(2):
                    b22 = random.randrange(2)
                    b15 = b5.fonk9(b21, fonk16(b22))
                    b23 = fonk2(b15[b22] if len(b15) > 1 else b15)
                    if len(b21[b23]) >= a1:
                        b23 = 1 - b23
                    b24 = copy.deepcopy(b21)
                    b25 = fonk15(b24, b23, b22)
                    b21 = b24
                    a4 += b25
                    if b25 = = 0:
                        break
                fonk14(b21)
                if b25 = = 0:
                    break
            b9 += a4
            f.write(f"{a4}\n")
    print('avg b25: ', b9 / a5)
if b26 = = "__main__":
    fonk17()