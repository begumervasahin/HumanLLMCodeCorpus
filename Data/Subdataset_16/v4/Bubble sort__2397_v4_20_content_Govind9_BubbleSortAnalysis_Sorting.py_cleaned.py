b1 = []
b2 = []
b3 = []
b4 = []
def fonk1():
    b5 = len(b3)
    b6 = B = BB = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(b5):
        print(f"{b2[i]}\t{b3[i]}\t{b4[i]}")
        b6 += b2[i]
        B += b3[i]
        BB += b4[i]
    print(f"{b6}\t{B}\t{BB}")
def fonk2(x):
    if len(x) == len(b11):
        b7 = "".join(b11[int(i)] for i in x)
        b1 = [int(i) for i in b7]
        fonk3(b1)
    else:
        for i in range(len(b11)):
            if str(i) not in x:
                fonk2(x + str(i))
def fonk3(b1):
    b3.append(fonk4(b1[:]))
    b2.append(fonk5(b1[:]))
    b4.append(fonk6(b1[:]))
    fonk1()
def fonk4(b1):
    a1 = 0
    b8 = len(b1)
    for j in range(b8):
        for i in range(b8 - 1 - j):
            a1 += 1
            if b1[i] > b1[i + 1]:
                a1 += 1
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
        a1 += 1
    return a1
def fonk5(b1):
    a1 = 0
    b8 = len(b1)
    for j in range(b8):
        b9 = False
        for i in range(b8 - 1 - j):
            a1 += 1
            if b1[i] > b1[i + 1]:
                a1 += 1
                b9 = True
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
        if not b9:
            break
        a1 += 1
    return a1
def fonk6(b1):
    a1 = 0
    b8 = len(b1)
    for j in range(b8):
        b10 = False
        for i in range(b8 - 1 - j):
            a1 += 1
            if b1[i] > b1[i + 1]:
                a1 += 1
                b10 = True
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
        if not b10:
            break
        a1 += 1
    return a1
b11 = '123456'
fonk2("")