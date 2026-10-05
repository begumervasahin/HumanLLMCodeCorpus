import numpy as np
import copy
import random
a1 = 10
a2 = 20
from keras.models import Sequential, Model, load_model
import keras
class class1:
    def fonk1(self):
        global problems
        self.b1 = np.zeros( (2,) )
        self.b2 = np.zeros( (a1*2,) )
        self.b3 = np.zeros((2,))
def fonk2(b14):
    b4 = np.random.choice(len(b14[0]), 1, p=b14[0])[0]
    b5 = b4
    return b5
class class2:
    def fonk3(self):
        self.b6 = load_model('trained_RNN')
        self.b6.compile(b7 = 'mse', optimizer='adam')
    def fonk4(self, state):
        b8 = copy.deepcopy(state)
        for i in range(len(b8)):
            for j in range(len(b8[i])):
                b8[i][j] += 1
            while (len(b8[i]) < a1):
                b8[i].append(0)
        return [b8[0] , b8[1]]
    def fonk5(self, state):
        b9 = self.fonk14(state)
        b9[0].append(-1)
        b9[1].append(-1)
        b9 = keras.preprocessing.sequence.pad_sequences( b9,  a2, 'float32','post','post', value =-100)
        return b9[0], b9[1]
    def fonk6(self, state, task):
        b10 = self.fonk5(state)
        return self.b6.predict( [ b10[0].reshape(1, len(b10[0]), 1), b10[1].reshape(1, len(b10[1]), 1) ] )
class class3:
    def fonk7(self):
        self.b6 = load_model('model_a_3_8')
        self.b6.compile(b7 = 'mse', optimizer='adam')
    def fonk8(self, state, b11 = False):
        b8 = copy.deepcopy(state)
        for i in range(len(b8)):
            for j in range(len(b8[i])):
                b8[i][j] += 1
            while (len(b8[i]) < a1):
                b8[i].append(0)
        if(not b11):
            return np.array([b8[0] + b8[1]])
        else:
            return np.array([b8[0] , b8[1]])
    def fonk9(self, state, task):
        b10 = self.fonk8(state)
        return self.b6.predict( [ b10,  task ] )
    def fonk10(self, state, task):
        a3 = 5
        b10 = self.fonk8(state, True)
        b8 = None
        for i in range( a1
            b12 = b10[ 0 ][ i*a3: (i+1)*a3 ]
            b13 = b10[ 1 ][i * a3: (i + 1) * a3]
            b14 = self.b6.predict( [ [ list(b12)+ list(b13) ],  task ] )
            if(not b8 is None): b8 = b8 + b14
            else: b8 = b14
        return b8 / ( a1
    def fonk11(self, state, task):
        a3 = 5
        b10 = self.fonk8(state, True)
        b8 = None
        for i in range( a1 -a3 + 1 ):
            b12 = b10[ 0 ][ i : i + a3]
            b13 = b10[ 1 ][i : i + a3]
            b14 = self.b6.predict( [ [ list(b12)+ list(b13) ],  task ] )
            if(not b8 is None): b8 = b8 + b14
            else: b8 = b14
        return b8 / ( a1 -a3 + 1 )
def fonk12(b14):
    b4 = np.random.choice(len(b14[0]), 1, p=b14[0])[0]
    b5 = b4
    return b5
def fonk13():
    return [[],[]]
def fonk14(state):
    b8 = copy.deepcopy(state)
    for i in range( len(b8) ):
        for j in range( len(b8[i])):
            b8[i][j] += 1
        while( len(b8[i])<a1 ):
            b8[i].append(0)
    return np.array([b8[0] + b8[1]])
def fonk15(state):
    a4 = 0
    a5 = 1
    a6 = 0.5
    a7 = 1
    if(a4 in state[0]): a7*=0.5
    a8 = 0.6
    a9 = 0.6
    if(not a5 in state[1]): a8*=0.5
    b15 = random.random()
    if( len(state[0])>0 ):
        if(state[0][0] == a4):
            if(b15 < a6): state[0].pop(0)
        else:
            if(b15 < a7): state[0].pop(0)
    if (len(state[1]) > 0):
        if (state[1][0] == a4):
            if (b15 < a8): state[1].pop(0)
        else:
            if (b15 < a9): state[1].pop(0)
def fonk16(state, b14, task):
    if( len(state[b14])>=a1 ): return 0
    else: state[b14].append(task)
    return 1
def fonk17(task):
    b8 = [0,0]
    b8[task] = 1
    return np.array([b8])
def fonk18():
    b6 = class3()
    random.seed()
    a10 = 0
    b16 = open('evaluated.txt','w')
    b9 = 0
    a11 = 10000
    for round in range(a11):
        if(round%b17 = =0)and(round!=0):
            print(b9/round)
        b18 = fonk13()
        a12 = 1.0
        a10 = 0
        for b5 in range(40):
            for task_ind in range(2):
                b19 = random.randrange(2)
                b14 = b6.fonk9( b18, fonk17(b19))
                if(len(b14)>1):
                    b20 = fonk12(b14[b19])
                else:
                    b20 = fonk12(b14)
                if(len( b18[b20] ) >= a1):
                    b20 = 1 - b20
                b21 = copy.deepcopy(b18)
                b22 = fonk16(b21, b20, b19)
                b18 = b21
                a10 += b22
                if (b22 = = 0): break
            fonk15(b18)
            if (b22 = = 0): break
        b9 += a10
        b16.write(str(a10))
        b16.write('\n')
    b16.close()
    print('avg b22: ', b9/a11)
if b23 = = "__main__":
    fonk18()