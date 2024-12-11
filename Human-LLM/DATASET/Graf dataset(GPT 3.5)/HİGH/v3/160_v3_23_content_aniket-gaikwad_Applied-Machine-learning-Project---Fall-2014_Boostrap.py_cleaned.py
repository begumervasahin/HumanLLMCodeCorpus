import sys
import random
b1 = []
a1 = 0.66
b2 = int(sys.argv[1])
def fonk1(b7):
    b3 = []
    b4 = len(b7)
    print("Number of Instances: %d" % b4)
    b5 = b4
    print("Size of One Bootstrap: %d" % b5)
    for _ in range(b2):
        b6 = [random.choice(b7) for _ in range(b5)]
        b3.append(b6)
    for i, bootstrap_sample in enumerate(b3):
        print("**********")
        print("Length of Bootstrap %d: %d" % (i+1, len(bootstrap_sample)))
def fonk2(b1):
    b7 = [line for line in b1 if random.random() < a1]
    b8 = [line for line in b1 if random.random() >= a1]
    print("Train Set:")
    print(b7)
    print("Test Set:")
    print(b8)
def fonk3(b1):
    fonk2(b1)
    fonk1(b1)
if b9 = = "__main__":
    fonk3(b1)