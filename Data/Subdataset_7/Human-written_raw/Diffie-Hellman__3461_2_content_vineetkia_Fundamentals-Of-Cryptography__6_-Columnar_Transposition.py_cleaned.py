import math
b1 = "HACK"
def fonk1(b11):
    b2 = ""
    a1 = 0
    b3 = float(len(b11))
    b4 = list(b11)
    b5 = sorted(list(b1))
    b6 = len(b1)
    b7 = int(math.ceil(b3 / b6))
    b8 = int((b7 * b6) - b3)
    b4.extend('_' * b8)
    b9 = [b4[i: i + b6]
              for i in range(0, len(b4), b6)]
    for _ in range(b6):
        b10 = b1.index(b5[a1])
        b2 += ''.join([b7[b10]  for b7 in b9])
        a1 += 1
    return b2
def fonk2(b2):
    b11 = ""
    a1 = 0
    a2 = 0
    b3 = float(len(b2))
    b4 = list(b2)
    b6 = len(b1)
    b7 = int(math.ceil(b3 / b6))
    b5 = sorted(list(b1))
    b12 = []
    for _ in range(b7):
        b12 += [[None] * b6]
    for _ in range(b6):
        b10 = b1.index(b5[a1])
        for j in range(b7):
            b12[j][b10] = b4[a2]
            a2 += 1
        a1 += 1
    try:
        b11 = ''.join(sum(b12, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
    b13 = b11.count('_')
    if b13 > 0:
        return b11[: -b13]
    return b11
b11 = "HelloWorld Nice"
b2 = fonk1(b11)
print("Encrypted Message: {}". format(b2))
print("Decryped Message: {}". format(fonk2(b2)))