import numpy.random as rand
import sys
b1 = "acgt"
b2 = "01"
def fonk1(chars, b9):
    return "".join([chars[rand.randint(0, len(chars))] for _ in range(b9)])
def fonk2(chars, b9, b3 = None):
    b4 = fonk1(chars, b9)
    if b3 is None:
        return b4, b4
    b5 = rand.permutation(len(b4))[:b3]
    b6 = "".join([chars[rand.randint(0, len(chars))] if i in b5 else b4[i] for i in range(len(b4))])
    return b4, b6
def fonk3(b9, b3 = None):
    return fonk2(b1, b9, b3)
def fonk4(b9, b3 = None):
    return fonk2(b2, b9, b3)
b7 = {
    "bits": get_random_bits,
    "acgt": get_random_acgt
}
def fonk5():
    if len(sys.argv) < 3:
        print("Usage: python " + __file__ + " acgt/bits N")
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
        print("N - b9 of the random strings to generate")
        return
    b8 = sys.argv[1]
    b9 = int(sys.argv[2])
    b3 = round(b9 * 0.3)
    if b8 in b7:
        b4, b6 = b7[b8](b9, b3)
        with open(b8 + ".txt", 'w') as f:
            f.write(b4 + "\n" + b6)
    else:
        print("Unknown type, please specify a valid type (acgt/bits)")
if b10 = = "__main__":
    fonk5()