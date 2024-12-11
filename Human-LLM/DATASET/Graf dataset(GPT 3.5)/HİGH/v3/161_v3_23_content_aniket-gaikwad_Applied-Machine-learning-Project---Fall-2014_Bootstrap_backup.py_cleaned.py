import sys
import random
import KNN
b1 = []
a1 = 0.66
b2 = int(sys.argv[2])
def fonk1(train_set):
    global b3
    b3 = []
    print("Number of instances: %d" % len(train_set))
    b4 = int(len(train_set) / b2)
    print("Size of each bootstrap sample: %d" % b4)
    for _ in range(b2):
        b5 = []
        for _ in range(b4):
            b5.append(random.choice(train_set))
        b3.append(b5)
    for i, sample in enumerate(b3):
        print("**********")
        print("Length of bootstrap sample %d: %d" % (i+1, len(sample)))
def fonk2(b10):
    b6 = open(b10, "r")
    global train_set, b7
    train_set, b7 = [], []
    for line in b6:
        b8 = line.strip().split(',')
        b9 = train_set if random.random() < a1 else b7
        b9.append(b8)
def fonk3():
    if len(sys.argv) < 3:
        print("Usage: python script.py <b10> <number_of_bootstraps>")
        sys.exit(1)
    b10 = sys.argv[1]
    global train_set, b7, b3
    fonk2(b10)
    fonk1(train_set)
    KNN.fonk3(b3[1], b7, 3)
if b11 = = "__main__":
    fonk3()