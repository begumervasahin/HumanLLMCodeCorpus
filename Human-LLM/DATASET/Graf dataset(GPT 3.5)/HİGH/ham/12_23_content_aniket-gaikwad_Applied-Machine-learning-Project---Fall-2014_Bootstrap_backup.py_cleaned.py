b1 = 'Aniket'
import sys
import random
import  KNN
b2 = []
a1 = 0.66
b3 = int(sys.argv[2])
def fonk1(b8):
    global b4
    b4 = []
    print("numberOfInstance : %d" %(len(b8)))
    b5 = int(len(b8)/b3)
    print("One Bootstrap size : %d " %(b5))
    for i in range(b3):
        b6 = []
        for j in range(b5):
            b6.append(random.choice(b8))
        b4.append(b6)
    for i in range(b3):
        print("**********")
        print("length : %d" %(len(b4[i])))
def fonk2(b11):
    b7 = open(b11,"r")
    global b8
    b8 = []
    global b9
    b9 = []
    for line in b7:
        b10 = line.strip()
        if random.random() < a1:
            b8.append(b10.split(','))
        else:
            b9.append(b10.split(','))
def fonk3():
    b11 = sys.argv[1]
    global b8
    global b9
    global b4
    fonk2(b11)
    fonk1(b8)
    KNN.fonk3(b4[1],b9,3)
fonk3()