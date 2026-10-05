import sys
import random
b1 = 'Aniket'
b2 = []
a1 = 0.66
b3 = int(sys.argv[3])
def fonk1(b7):
    b4 = []
    b5 = len(b7)
    print("Number of Instances:", len(b7))
    print("One Bootstrap size:", b5)
    for b10 in range(b3):
        b6 = [random.choice(b7) for b10 in range(b5)]
        b4.append(b6)
    for i, sample in enumerate(b4):
        print("**********")
        print("Length of Sample", i + 1, ":", len(sample))
def fonk2(input_data):
    b7 = []
    b8 = []
    for line in input_data:
        if random.random() < a1:
            b7.append(line)
        else:
            b8.append(line)
    print("Train Set:")
    print(b7)
    print("Test Set:")
    print(b8)
    b9 = len(b8)
    return b7, b8, b9
def fonk3(input_data):
    b7, b10, b10 = fonk2(input_data)
    fonk1(b7)
if b11 = = "__main__":
    fonk3(b2)