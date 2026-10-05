import sys
import random
b1 = []
a1 = 0.66
b2 = int(sys.argv[1])
def fonk1(b6):
    b3 = []
    print("Number of Instances: %d" % len(b6))
    b4 = len(b6)
    print("Size of One Bootstrap: %d" % b4)
    for i in range(b2):
        b5 = []
        for j in range(b4):
            b5.append(random.choice(b6))
        b3.append(b5)
    for i in range(b2):
        print("**********")
        print("Length: %d" % len(b3[i]))
def fonk2(b1):
    b6 = []
    b7 = []
    for line in b1:
        if random.random() < a1:
            b6.append(line)
        else:
            b7.append(line)
    print("Train Set:")
    print(b6)
    print("Test Set:")
    print(b7)
def fonk3(inputSet):
    fonk2(inputSet)
    fonk1(b6)
if b8 = = "__main__":
    fonk3(b1)