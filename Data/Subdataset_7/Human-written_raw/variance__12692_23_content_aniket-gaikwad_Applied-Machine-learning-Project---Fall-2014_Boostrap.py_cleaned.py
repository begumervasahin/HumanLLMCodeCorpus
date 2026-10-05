b1 = 'Aniket'
import sys
import random
b2 = []
a1 = 0.66
b3 = int(sys.argv[3])
def fonk1(b7):
    global b4
    b4 = []
    print("numberOfInstance : %d" %(len(b7)))
    b5 = int(len(b7)/b3)
    print("One Bootstrap size : %d " %(b5))
    for i in range(b3):
        b6 = []
        for j in range(b5):
            b6.append(random.choice(b7))
        b4.append(b6)
    for i in range(b3):
        print("**********")
        print("length : %d" %(len(b4[i])))
def fonk2(b2):
    global b7
    b7 = []
    global b8
    b8 = []
    for line in range(len(b2)):
        if random.random() < a1:
            b7.append(b2[line])
        else:
            b8.append(b2[line])
    print("TRain : ")
    print(b7)
    print("Test :")
    print(b8)
    global b9
    b9 = len(b8)
def fonk3(inputSet):
    global b7
    global b8
    global b4
    fonk2(inputSet)
    fonk1(b7)