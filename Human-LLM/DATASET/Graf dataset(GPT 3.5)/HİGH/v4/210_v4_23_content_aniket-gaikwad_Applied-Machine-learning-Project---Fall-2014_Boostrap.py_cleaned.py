import sys
import random
b1 = 'Aniket'
b2 = []
a1 = 0.66
b3 = int(sys.argv[3])
def fonk1(b7):
    global b4
    b4 = []
    print("Number of Instances: %d" % (len(b7)))
    b5 = int(len(b7) / b3)
    print("One Bootstrap size: %d " % (b5))
    for i in range(b3):
        b6 = []
        for j in range(b5):
            b6.append(random.choice(b7))
        b4.append(b6)
    for i in range(b3):
        print("**********")
        print("Length: %d" % (len(b4[i])))
def fonk2(b2):
    global b7, b8
    b7 = []
    b8 = []
    for line in range(len(b2)):
        if random.random() < a1:
            b7.append(b2[line])
        else:
            b8.append(b2[line])
    print("Train Set:")
    print(b7)
    print("Test Set:")
    print(b8)
    global b9
    b9 = len(b8)
def fonk3(inputSet):
    global b7, b8, b4
    fonk2(inputSet)
    fonk1(b7)
if b10 = = "__main__":
    fonk3(b2)