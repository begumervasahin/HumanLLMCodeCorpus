import sys
import random
b1 = []
a1 = 0.66
b2 = int(sys.argv[1])
def fonk1(b6):
    b3 = []
    print("numberOfInstance : %d" % (len(b6)))
    b4 = int(len(b6) / b2)
    print("One Bootstrap size : %d " % (b4))
    for i in range(b2):
        b5 = []
        for j in range(b4):
            b5.append(random.choice(b6))
        b3.append(b5)
    for i in range(b2):
        print("**********")
        print("length : %d" % (len(b3[i])))
def fonk2(b1):
    b6 = []
    b7 = []
    for line in range(len(b1)):
        if random.random() < a1:
            b6.append(b1[line])
        else:
            b7.append(b1[line])
    print("Train : ")
    print(b6)
    print("Test :")
    print(b7)
    b8 = len(b7)
def fonk3(inputSet):
    fonk2(inputSet)
    fonk1(b6)
if b9 = = "__main__":
    fonk3(b1)