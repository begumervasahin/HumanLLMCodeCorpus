import numpy as np
import copy
import random
import keras
from keras.models import load_model
a1 = 10
class class1:
    def fonk1(self):
        self.b1 = load_model('model_a_3_8')
        self.b1.compile(b2 = 'mse', optimizer='adam')
    def fonk2(self, state, b3 = False):
        b4 = copy.deepcopy(state)
        for i in range(len(b4)):
            for j in range(len(b4[i])):
                b4[i][j] += 1
            while len(b4[i]) < a1:
                b4[i].append(0)
        if not b3:
            return np.array([b4[0] + b4[1]])
        else:
            return np.array([b4[0], b4[1]])
    def fonk3(self, state, task):
        b5 = self.fonk2(state)
        return self.b1.predict([b5, task])
    def fonk4(self, state, task):
        a2 = 5
        b5 = self.fonk2(state, True)
        b4 = None
        for i in range(a1
            b6 = b5[0][i * a2: (i + 1) * a2]
            b7 = b5[1][i * a2: (i + 1) * a2]
            b8 = self.b1.predict([[list(b6) + list(b7)], task])
            if b4 is not None:
                b4 = b4 + b8
            else:
                b4 = b8
        return b4 / (a1
    def fonk5(self, state, task):
        a2 = 5
        b5 = self.fonk2(state, True)
        b4 = None
        for i in range(a1 - a2 + 1):
            b6 = b5[0][i: i + a2]
            b7 = b5[1][i: i + a2]
            b8 = self.b1.predict([[list(b6) + list(b7)], task])
            if b4 is not None:
                b4 = b4 + b8
            else:
                b4 = b8
        return b4 / (a1 - a2 + 1)
def fonk6(b8):
    b9 = np.random.choice(len(b8[0]), 1, p=b8[0])[0]
    b10 = b9
    return b10
def fonk7():
    return [[], []]
def fonk8(state):
    a3 = 0
    a4 = 1
    a5 = 0.5
    a6 = 1
    if a3 in state[0]:
        a6 *= 0.5
    a7 = 0.6
    a8 = 0.6
    if a4 not in state[1]:
        a7 *= 0.5
    b11 = random.random()
    if len(state[0]) > 0:
        if state[0][0] == a3:
            if b11 < a5:
                state[0].pop(0)
        else:
            if b11 < a6:
                state[0].pop(0)
    if len(state[1]) > 0:
        if state[1][0] == a3:
            if b11 < a7:
                state[1].pop(0)
        else:
            if b11 < a8:
                state[1].pop(0)
def fonk9(state, b8, task):
    if len(state[b8]) >= a1:
        return 0
    else:
        state[b8].append(task)
        return 1
def fonk10(task):
    b4 = [0, 0]
    b4[task] = 1
    return np.array([b4])
def fonk11():
    b1 = class1()
    random.seed()
    a9 = 0
    b12 = open('evaluated.txt', 'w')
    a10 = 0
    a11 = 10000
    for round in range(a11):
        if round % b13 = = 0 and round != 0:
            print(a10 / round)
        b14 = fonk7()
        a12 = 1.0
        a9 = 0
        for b10 in range(40):
            for task_ind in range(2):
                b15 = random.randrange(2)
                b8 = b1.fonk3(b14, fonk10(b15))
                if len(b8) > 1:
                    b16 = fonk6(b8[b15])
                else:
                    b16 = fonk6(b8)
                if len(b14[b16]) >= a1:
                    b16 = 1 - b16
                b17 = copy.deepcopy(b14)
                b18 = fonk9(b17, b16, b15)
                b14 = b17
                a9 += b18
                if b18 = = 0:
                    break
            fonk8(b14)
            if b18 = = 0:
                break
        a10 += a9
        b12.write(str(a9))
        b12.write('\n')
    b12.close()
    print('avg b18: ', a10 / a11)
if b19 = = "__main__":
    fonk11()