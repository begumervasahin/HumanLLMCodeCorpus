
import numpy.random as rand
import sys
b1 = "b1"
b2 = "01"
def fonk1(length, b3 = None):
    b4 = "".join([b1[rand.randint(0, len(b1))] for _ in range(length)])
    if b3 is None:
        return b4, b4
    else:
        b5 = rand.permutation(len(b4))[:b3]
        b6 = "".join([b1[rand.randint(0, len(b1))]
                     if i in b5
                     else b4[i]
                     for i in range(len(b4))])
        return b4, b6
def fonk2(length, b3 = None):
    b4 = "".join([b2[rand.randint(0, len(b2))] for _ in range(length)])
    if b3 is None:
        return b4, b4
    else:
        b5 = rand.permutation(len(b4))[:b3]
        b6 = "".join([b2[rand.randint(0, len(b2))]
                     if i in b5
                     else b4[i]
                     for i in range(len(b4))])
        return b4, b6
b7 = {
    "b2": get_random_bits,
    "b1": get_random_acgt
}
if b8 = = "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 " + __file__ + " b1/b2 N")
        print("b1 - generate sequences of b1")
        print("b2- generate sequences of binary digits")
        print("N - length of the random strings to generate")
    else:
        b9 = sys.argv[1]
        b10 = int(sys.argv[2])
        b3 = round(b10 * 0.3)
        if b9 in b7:
            b4, b6 = b7[b9](b10, b3)
            with open(b9 + ".txt", 'w') as f:
                f.write(b4 + "\n" + b6)
        else:
            print("unknown b9, please specify valid b9 (b1/b2)")