
import numpy.random as rand
import sys
b1 = "acgt"
b2 = "01"
def fonk1(length, b3 = None):
    b4 = "".join([b1[rand.randint(0, len(b1))] for _ in range(length)])
    if b3 is None:
        return b4, b4
    b5 = rand.permutation(len(b4))[:b3]
    b6 = "".join(
        [b1[rand.randint(0, len(b1))] if i in b5 else b4[i] for i in range(len(b4))]
    )
    return b4, b6
def fonk2(length, b3 = None):
    b4 = "".join([b2[rand.randint(0, len(b2))] for _ in range(length)])
    if b3 is None:
        return b4, b4
    b5 = rand.permutation(len(b4))[:b3]
    b6 = "".join(
        [b2[rand.randint(0, len(b2))] if i in b5 else b4[i] for i in range(len(b4))]
    )
    return b4, b6
b7 = {
    "bits": get_random_bits,
    "acgt": get_random_acgt
}
if b8 = = "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python {__file__} acgt/bits N")
        print("acgt - generate sequences of acgt")
        print("bits - generate sequences of binary digits")
        print("N - length of the random strings to generate")
    else:
        b9 = sys.argv[1]
        b10 = int(sys.argv[2])
        b3 = round(b10 * 0.3)
        if b9 in b7:
            b4, b6 = b7[b9](b10, b3)
            with open(f"{b9}.txt", 'w') as f:
                f.write(f"{b4}\n{b6}")
        else:
            print("Unknown type. Please specify a valid type (acgt/bits).")