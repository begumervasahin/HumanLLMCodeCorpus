def fonk1(b7):
    a1 = 0
    for j in range(len(b7)):
        a1 += 3
        b1 = False
        for i in range(len(b7) - 1 - j):
            a1 += 2
            if b7[i] > b7[i + 1]:
                a1 += 2
                b1 = True
                b7[i], b7[i + 1] = b7[i + 1], b7[i]
        if not b1:
            break
    return a1
def fonk2(b7):
    a1 = 0
    for j in range(len(b7)):
        a1 += 3
        a2 = 0
        for i in range(len(b7) - 1 - j):
            a1 += 2
            if b7[i] > b7[i + 1]:
                a1 += 2
                a2 += 1
                b7[i], b7[i + 1] = b7[i + 1], b7[i]
        if a2 < 2:
            break
    return a1
def fonk3(b7):
    a1 = 0
    for j in range(len(b7)):
        a1 += 3
        b1 = False
        for i in range(len(b7) - 1 - j):
            a1 += 2
            if b7[i] > b7[i + 1]:
                a1 += 2
                b1 = True
                b7[i], b7[i + 1] = b7[i + 1], b7[i]
        if not b1:
            break
    return a1
def fonk4(b8, b9, b10):
    print("Qsort\tBubble\tBetterBubble")
    for Q, B, BB in zip(b8, b9, b10):
        print(f"{Q}\t{B}\t{BB}")
    b2 = sum(b8)
    b3 = sum(b9)
    b4 = sum(b10)
    print(f"{b2}\t{b3}\t{b4}")
def fonk5(b6, b7, b8, b9, b10):
    if len(b7) == len(b6):
        fonk6(b7, b8, b9, b10)
    for i in range(len(b6)):
        if str(i) not in b7:
            fonk5(b6, b7 + str(i), b8, b9, b10)
def fonk6(b7, b8, b9, b10):
    b5 = b7[:]
    b9.append(fonk1(b5))
    b5 = b7[:]
    b8.append(fonk2(b5))
    b5 = b7[:]
    b10.append(fonk3(b5))
    fonk4(b8, b9, b10)
def fonk7():
    b6 = '123456'
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    fonk5(b6, b7, b8, b9, b10)
if b11 = = "__main__":
    fonk7()