import numpy as np
import copy
import random
from keras.models import load_model
a1 = 10
class class1:
    def fonk1(self):
        self.b1 = load_model('model_a_3_8')
        self.b1.compile(b2 = 'mse', optimizer='adam')
    def fonk2(self, state, b3 = False):
        b4 = copy.deepcopy(state)
        for i in range(len(b4)):
            b4[i] = [val + 1 for val in b4[i]]
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
            b8 = self.b1.predict([[*b6, *b7], task])
            if b4 is not None:
                b4 += b8
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
            b8 = self.b1.predict([[*b6, *b7], task])
            if b4 is not None:
                b4 += b8
            else:
                b4 = b8
        return b4 / (a1 - a2 + 1)
def fonk6(b8):
    b9 = np.random.choice(len(b8[0]), 1, p=b8[0])[0]
    return b9
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
    b10 = random.random()
    if len(state[0]) > 0:
        if state[0][0] == a3:
            if b10 < a5:
                state[0].pop(0)
        else:
            if b10 < a6:
                state[0].pop(0)
    if len(state[1]) > 0:
        if state[1][0] == a3:
            if b10 < a7:
                state[1].pop(0)
        else:
            if b10 < a8:
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
    with open('evaluated.txt', 'w') as f:
        a10 = 0
        a11 = 10000
        for round in range(a11):
            if round % b11 = = 0 and round != 0:
                print(a10 / round)
            b12 = fonk7()
            a9 = 0
            for ind in range(40):
                for task_ind in range(2):
                    b13 = random.randrange(2)
                    b8 = b1.fonk3(b12, fonk10(b13))
                    if len(b8) > 1:
                        b14 = fonk6(b8[b13])
                    else:
                        b14 = fonk6(b8)
                    if len(b12[b14]) >= a1:
                        b14 = 1 - b14
                    b15 = copy.deepcopy(b12)
                    b16 = fonk9(b15, b14, b13)
                    b12 = b15
                    a9 += b16
                    if b16 = = 0:
                        break
                fonk8(b12)
                if b16 = = 0:
                    break
            a10 += a9
            f.write(str(a9))
            f.write('\n')
    print('avg b16: ', a10 / a11)
if b17 = = "__main__":
    fonk11()