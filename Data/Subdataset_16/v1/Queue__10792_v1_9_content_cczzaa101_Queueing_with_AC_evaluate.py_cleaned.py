import numpy as np
import copy
import random
from keras.models import Sequential, Model, load_model
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
            for j in range(len(b7[i])):
                b7[i][j] += 1
            while len(b7[i]) < a1:
                b7[i].append(0)
        return [b7[0], b7[1]]
    def fonk5(self, state):
        b8 = self.fonk13(state)
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
            for j in range(len(b7[i])):
                b7[i][j] += 1
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
            b11 = b9[0][i * a3: (i + 1) * a3]
            b12 = b9[1][i * a3: (i + 1) * a3]
            b13 = self.b5.predict([[list(b11) + list(b12)], task])
            if b7 is not None:
                b7 = b7 + b13
            else:
                b7 = b13
        return b7 / (a1
    def fonk11(self, state, task):
        a3 = 5
        b9 = self.fonk8(state, True)
        b7 = None
        for i in range(a1 - a3 + 1):
            b11 = b9[0][i: i + a3]
            b12 = b9[1][i: i + a3]
            b13 = self.b5.predict([[list(b11) + list(b12)], task])
            if b7 is not None:
                b7 = b7 + b13
            else:
                b7 = b13
        return b7 / (a1 - a3 + 1)
def fonk12():
    return [[], []]
def fonk13(state):
    b7 = copy.deepcopy(state)
    for i in range(len(b7)):
        for j in range(len(b7[i])):
            b7[i][j] += 1
        while len(b7[i]) < a1:
            b7[i].append(0)
    return np.array([b7[0] + b7[1]])
def fonk14(state):
    a4 = 0
    a5 = 1
    a6 = 0.5
    a7 = 1
    if a4 in state[0]:
        a7 *= 0.5
    a8 = 0.6
    a9 = 0.6
    if a5 not in state[1]:
        a8 *= 0.5
    b14 = random.random()
    if len(state[0]) > 0:
        if state[0][0] == a4:
            if b14 < a6:
                state[0].pop(0)
        else:
            if b14 < a7:
                state[0].pop(0)
    if len(state[1]) > 0:
        if state[1][0] == a4:
            if b14 < a8:
                state[1].pop(0)
        else:
            if b14 < a9:
                state[1].pop(0)
def fonk15(state, b13, task):
    if len(state[b13]) >= a1:
        return 0
    else:
        state[b13].append(task)
    return 1
def fonk16(task):
    b7 = [0, 0]
    b7[task] = 1
    return np.array([b7])
def fonk17():
    b5 = class3()
    random.seed()
    a10 = 0
    b15 = open('evaluated.txt', 'w')
    b8 = 0
    a11 = 10000
    for round in range(a11):
        if round % b16 = = 0 and round != 0:
            print(b8 / round)
        b17 = fonk12()
        a12 = 1.0
        a10 = 0
        for ind in range(40):
            for task_ind in range(2):
                b18 = random.randrange(2)
                b13 = b5.fonk9(b17, fonk16(b18))
                if len(b13) > 1:
                    b19 = fonk2(b13[b18])
                else:
                    b19 = fonk2(b13)
                if len(b17[b19]) >= a1:
                    b19 = 1 - b19
                b20 = copy.deepcopy(b17)
                b21 = fonk15(b20, b19, b18)
                b17 = b20
                a10 += b21
                if b21 = = 0:
                    break
            fonk14(b17)
            if b21 = = 0:
                break
        b8 += a10
        b15.write(str(a10))
        b15.write('\n')
    b15.close()
    print('avg b21: ', b8 / a11)
if b22 = = "__main__":
    fonk17()