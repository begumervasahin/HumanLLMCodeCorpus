import math
def fonk1(b10, b13):
    b1 = ""
    a1 = 0
    b2 = len(b10)
    b3 = list(b10)
    b4 = sorted(list(b13))
    b5 = len(b13)
    b6 = math.ceil(b2 / b5)
    b7 = b6 * b5 - b2
    b3.extend('_' * b7)
    b8 = [b3[i: i + b5] for i in range(0, len(b3), b5)]
    for _ in range(b5):
        b9 = b13.index(b4[a1])
        b1 += ''.join([b6[b9] for b6 in b8])
        a1 += 1
    return b1
def fonk2(b1, b13):
    b10 = ""
    a1 = 0
    a2 = 0
    b2 = len(b1)
    b3 = list(b1)
    b5 = len(b13)
    b6 = math.ceil(b2 / b5)
    b4 = sorted(list(b13))
    b11 = [[] for _ in range(b6)]
    for _ in range(b5):
        b9 = b13.index(b4[a1])
        for j in range(b6):
            b11[j].append(b3[a2])
            a2 += 1
        a1 += 1
    try:
        b10 = ''.join(sum(b11, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    b12 = b10.count('_')
    if b12 > 0:
        return b10[:-b12]
    return b10
def fonk3():
    b13 = "HACK"
    b10 = "HelloWorld Nice"
    b1 = fonk1(b10, b13)
    print("Encrypted Message: {}".format(b1))
    b14 = fonk2(b1, b13)
    print("Decrypted Message: {}".format(b14))
if b15 = = "__main__":
    fonk3()