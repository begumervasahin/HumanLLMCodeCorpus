import sys
import random
import KNN
b1 = []
a1 = 0.66
def fonk1(b5, no_of_bootstraps):
    b2 = []
    print("Number of Instances: %d" % len(b5))
    b3 = len(b5)
    print("One Bootstrap size: %d" % b3)
    for _ in range(no_of_bootstraps):
        b4 = [random.choice(b5) for _ in range(b3)]
        b2.append(b4)
    for i in range(no_of_bootstraps):
        print("**********")
        print("Length: %d" % len(b2[i]))
    return b2
def fonk2(b8):
    b5 = []
    b6 = []
    with open(b8, "r") as fin:
        for line in fin:
            b7 = line.strip().split(',')
            if random.random() < a1:
                b5.append(b7)
            else:
                b6.append(b7)
    return b5, b6
def fonk3():
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file> <number_of_bootstraps>")
        return
    b8 = sys.argv[1]
    b9 = int(sys.argv[2])
    b5, b6 = fonk2(b8)
    b2 = fonk1(b5, b9)
    KNN.fonk3(b2[1], b6, 3)
if b10 = = "__main__":
    fonk3()