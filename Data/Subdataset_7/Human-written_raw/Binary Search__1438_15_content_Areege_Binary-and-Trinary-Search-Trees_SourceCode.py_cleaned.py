import random
import time
def fonk1(collection, b3):
    a1 = 0
    b1 = len(collection) -1
    while b1 >= a1:
        b2 = (b1 + a1)
        if (b3 = = collection[b2]):
            return b2
        if (b3 < collection[b2]):
            b1 = b2 - 1
        else:
            a1 = b2 + 1
    return -1
def fonk2(collection, b3):
    a1 = 0
    b1 = len(collection) -1
    while b1 >= a1:
        b4 = a1 + (b1-a1)
        b5 = a1 + b8*(b1-a1)
        if (b3 = = collection[b4]):
            return b4
        elif (b3 < collection[b4]):
            b1 = b4 - 1
        elif (b3 = = collection[b5]):
            return b5
        elif (b3 < collection[b5]):
            a1 = b4 + 1
            b1 = b5 - 1
        else:
            a1 = b5 + 1
    return -1
def fonk3(b7):
   for fill in range(len(b7)-1,0,-1):
       a2 = 0
       for b10 in range(1,fill+1):
           if b7[b10]>b7[a2]:
               a2 = b10
       b6 = b7[fill]
       b7[fill] = b7[a2]
       b7[a2] = b6
def fonk4(b16):
    b7 = random.sample(range(1, 16001), b16)
    for b10 in range(0, len(b7)-1):
        if (b7[b10] % b8 != 0):
            b7[b10] = b7[b10] + 1
    return b7
def fonk5(b16):
    b7 = random.sample(range(1, 1000000), 10*b16)
    for b10 in range(0, len(b7)-1):
        if (b7[b10] % b8 = = 0):
            b7[b10] = b7[b10] + 1
    return b7
def fonk6(b14):
    b9 = []
    for integer in range(0, len(b14)):
        for b10 in range(0,10):
            b9.append(b14[integer])
            b10 = b10 + 1
    return b9
def fonk7(b14, b9):
    b11 = time.clock()
    for b10 in b9:
        b12 = fonk1(b14, b10)
    print("Binary Search time: " + str(time.clock()-b11))
    b11 = time.clock()
    for b10 in b9:
        b13 = fonk2(b14, b10)
    print("Trinary Search time: " + str(time.clock()-b11) + "\b16")
def fonk8(b16):
    print("Experiment
    b14 = fonk4(b16)
    fonk3(b14)
    b9 = fonk6(b14)
    fonk7(b14, b9)
    print("Experiment
    b9 = fonk5(b16)
    fonk7(b14, b9)
def fonk9():
    b15 = [1000, 2000, 4000, 8000, 16000]
    for b10 in b15:
        print("For b16 = " + str(b10) + "\b16")
        fonk8(b10)
fonk9()