import sys
import random
import KNN
b1 = []
a1 = 0.66
b2 = int(sys.argv[2])
b3 = []
def fonk1(b6):
    global b3
    print("Number of Instances: %d" % len(b6))
    b4 = int(len(b6) / b2)
    print("One Bootstrap size: %d" % b4)
    for i in range(b2):
        b5 = []
        for j in range(b4):
            b5.append(random.choice(b6))
        b3.append(b5)
    for i in range(b2):
        print("**********")
        print("Length: %d" % len(b3[i]))
def fonk2(b10):
    global b6, b7
    b6 = []
    b7 = []
    b8 = open(b10, "r")
    for line in b8:
        b9 = line.strip()
        if random.random() < a1:
            b6.append(b9.split(','))
        else:
            b7.append(b9.split(','))
    b8.close()
def fonk3():
    b10 = sys.argv[1]
    fonk2(b10)
    fonk1(b6)
    KNN.fonk3(b3[1], b7, 3)
if b11 = = "__main__":
    fonk3()