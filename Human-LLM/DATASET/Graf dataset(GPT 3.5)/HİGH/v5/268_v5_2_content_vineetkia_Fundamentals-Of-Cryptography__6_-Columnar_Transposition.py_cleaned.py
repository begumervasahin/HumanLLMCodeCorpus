import math
b1 = "HACK"
def fonk1(b11):
    b2 = ""
    a1 = 0
    b3 = len(b11)
    b4 = list(b11)
    b5 = sorted(list(b1))
    b6 = len(b1)
    b7 = int(math.ceil(b3 / b6))
    b8 = int((b7 * b6) - b3)
    b4.extend('_' * b8)
    b9 = [b4[i: i + b6] for i in range(0, len(b4), b6)]
    for _ in range(b6):
        b10 = b1.index(b5[a1])
        b2 += ''.join([row[b10] for row in b9])
        a1 += 1
    return b2
def fonk2(b2):
    b11 = ""
    a1 = 0
    a2 = 0
    b3 = len(b2)
    b12 = list(b2)
    b6 = len(b1)
    b7 = int(math.ceil(b3 / b6))
    b5 = sorted(list(b1))
    b13 = [[] for _ in range(b7)]
    for _ in range(b6):
        b10 = b1.index(b5[a1])
        for j in range(b7):
            b13[j].append(b12[a2])
            a2 += 1
        a1 += 1
    try:
        b11 = ''.join(sum(b13, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    b14 = b11.count('_')
    if b14 > 0:
        return b11[:-b14]
    return b11
b11 = "HelloWorld Nice"
b15 = fonk1(b11)
print("Encrypted Message: {}".format(b15))
b16 = fonk2(b15)
print("Decrypted Message: {}".format(b16))