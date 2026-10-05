import sys
import random
import KNN
b1 = []
a1 = 0.66
b2 = int(sys.argv[2])
def fonk1(b7):
    global b3
    b3 = []
    print("Number of instances: %d" % len(b7))
    b4 = int(len(b7) / b2)
    print("Size of each bootstrap sample: %d" % b4)
    for _ in range(b2):
        b5 = []
        for _ in range(b4):
            b5.append(random.choice(b7))
        b3.append(b5)
    for i in range(b2):
        print("**********")
        print("Length of bootstrap sample %d: %d" % (i+1, len(b3[i])))
def fonk2(b10):
    b6 = open(b10, "r")
    global b7
    b7 = []
    global b8
    b8 = []
    for line in b6:
        b9 = line.strip()
        if random.random() < a1:
            b7.append(b9.split(','))
        else:
            b8.append(b9.split(','))
def fonk3():
    if len(sys.argv) < 3:
        print("Usage: python script.py <b10> <number_of_bootstraps>")
        sys.exit(1)
    b10 = sys.argv[1]
    global b7
    global b8
    global b3
    fonk2(b10)
    fonk1(b7)
    KNN.fonk3(b3[1], b8, 3)
if b11 = = "__main__":
    fonk3()