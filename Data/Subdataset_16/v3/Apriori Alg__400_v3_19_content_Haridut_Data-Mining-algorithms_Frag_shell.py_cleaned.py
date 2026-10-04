import sys
import itertools
def fonk1():
    b1 = sys.stdin.readlines()
    b2 = int(b1[0].strip())
    b3 = [line.strip().split() for line in b1[1:]]
    return b2, b3
def fonk2(b3):
    b4 = list(zip(*b3))
    b5 = [sorted(set(dim)) for dim in b4]
    return b5
def fonk3(b3, b2):
    b6 = [[] for _ in range(b2)]
    for i in range(len(b3[0])):
        b6[i % b2].append(i)
    b7 = [len(indices) for indices in b6]
    return b6, b7
def fonk4(b5, b2, b7):
    b8 = []
    a1 = 0
    for b9 in b7:
        b8.append(b5[a1:a1 + b9])
        a1 += b9
    return b8
def fonk5(subset, b3):
    b9 = sum(1 for item in b3 if set(subset).issubset(item))
    return b9
def fonk6(b8, b3):
    for fragment in b8:
        for length in range(1, len(fragment) + 1):
            for combination in itertools.combinations(fragment, length):
                b10 = [item for sublist in combination for item in sublist]
                for subset in itertools.combinations(b10, length):
                    b9 = fonk5(subset, b3)
                    if b9 > 0:
                        print(" ".join(subset) + ": " + str(b9))
        print()
def fonk7():
    b2, b3 = fonk1()
    b5 = fonk2(b3)
    b6, b7 = fonk3(b3, b2)
    b8 = fonk4(b5, b2, b7)
    fonk6(b8, b3)
if b11 = = "__main__":
    fonk7()