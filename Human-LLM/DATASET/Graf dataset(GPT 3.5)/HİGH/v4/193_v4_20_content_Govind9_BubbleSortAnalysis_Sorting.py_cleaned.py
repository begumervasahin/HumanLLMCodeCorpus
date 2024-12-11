
b1 = []
b2 = []
b3 = []
def fonk1():
    b4 = len(b2)
    b5 = sum(b1)
    b6 = sum(b2)
    b7 = sum(b3)
    print("Qsort\tBubble\tBetterBubble")
    for i in range(b4):
        print(f"{b1[i]}\t{b2[i]}\t{b3[i]}")
    print(f"{b5}\t{b6}\t{b7}")
def fonk2(x):
    b8 = []
    if len(x) == len(b12):
        b9 = "".join(b12[int(i)] for i in x)
        for i in b9:
            b8.append(int(i))
        fonk3(b8)
    for i in range(len(b12)):
        if str(i) not in x:
            fonk2(x + str(i))
def fonk3(b8):
    b2.append(fonk4(b8))
    b1.append(fonk5(b8))
    b3.append(fonk6(b8))
    fonk1()
def fonk4(b8):
    a1 = 0
    for j in range(len(b8)):
        a1 += 3
        for i in range(len(b8) - 1 - j):
            a1 += 2
            if b8[i] > b8[i + 1]:
                a1 += 2
                b10 = b8[i]
                b8[i] = b8[i + 1]
                b8[i + 1] = b10
    return a1
def fonk5(b8):
    a1 = 0
    for j in range(len(b8)):
        a1 += 3
        a2 = 0
        for i in range(len(b8) - 1 - j):
            a1 += 2
            if b8[i] > b8[i + 1]:
                a1 += 2
                a2 += 1
                b10 = b8[i]
                b8[i] = b8[i + 1]
                b8[i + 1] = b10
        if a2 < 2:
            break
    return a1
def fonk6(b8):
    a1 = 0
    for j in range(len(b8)):
        a1 += 3
        b11 = False
        for i in range(len(b8) - 1 - j):
            a1 += 2
            if b8[i] > b8[i + 1]:
                a1 += 2
                b11 = True
                b10 = b8[i]
                b8[i] = b8[i + 1]
                b8[i + 1] = b10
        if not b11:
            break
    return a1
b12 = '123456'
fonk2("")