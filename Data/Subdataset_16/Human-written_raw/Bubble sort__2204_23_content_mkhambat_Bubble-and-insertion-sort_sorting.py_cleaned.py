import random
import pickle
import time
import matplotlib.pyplot as plt
b1 = random.sample(range(-100000,100000),100000)
global b2
b2 = []
global b3
b3 = []
global a1
a1 = 0.0
global a2
a2 = 0.0
def fonk1(b1):
    a1 = []
    a2 = []
    b4 = []
    b1 = random.sample(range(1,300000),200000)
    with open("data.txt", 'wb') as fp:
        pickle.dump(b1,fp)
    with open("data.txt", 'rb') as fp:
        b1 = pickle.load(fp)
    a3 = 2000
    for b16 in range (0,25):
        b2 = []
        b3 = []
        a4 = 0.0
        a5 = 0.0
        for j in range(0,10):
            b5 = random.sample(b1,a3)
            b6 = random.sample(b1,a3)
            b7 = time.time()
            fonk2(b5)
            b8 = time.time()
            b9 = b8-b7
            b2.append(b9)
            a4 = a4+b2[j]
            b10 = time.time()
            fonk3(b6)
            b11 = time.time()
            b12 = b11-b10
            b3.append(b12)
            a5 = a5+b3[j]
        a1.append(a4/10)
        a2.append(a5/10)
        print(a1)
        print(a2)
        a3 = a3+2000
    for b16 in range(1,26):
        b4.append(2000*b16)
    plt.plot(b4,a1,'r--' ,b4,a2,'b--')
    plt.show()
def fonk2(b1):
    global time_list
    global avg_time
    b13 = len(b1)
    for b16 in range (0,b13):
        for j in range (0,b13-1):
            if(b1[j]>b1[j+1]):
                b14 = b1[j]
                b1[j]=b1[j+1]
                b1[j+1]=b14
def fonk3(b1):
    b13 = len(b1)
    for j in range (1,b13):
        b15 = b1[j]
        b16 = j-1
        while(b16>=0 and b1[b16]>b15):
            b1[b16+1]=b1[b16]
            b16 = b16-1
        b1[b16+1] = b15
fonk1(b1)