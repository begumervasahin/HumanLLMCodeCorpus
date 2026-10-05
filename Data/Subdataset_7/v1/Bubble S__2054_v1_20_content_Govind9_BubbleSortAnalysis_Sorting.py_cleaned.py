b1 = []
b2 = []
b3 = []
b4 = []
def fonk1():
    b5 = len(b3)
    b6 = B = BB = 0
    print("Qsort\tBubble\tBetterBubble")
    for i in range(b5):
        print(str(b2[i]) + "\t" + str(b3[i]) + "\t" + str(b4[i]))
        b6 += b2[i]
        B += b3[i]
        BB += b4[i]
    print(str(b6) + "\t" + str(B) + "\t" + str(BB))
def fonk2(x):
    global b1
    if len(x) == len(b10):
        b7 = "".join(b10[int(i)] for i in x)
        b1 = [int(i) for i in b7]
        fonk3(b1)
    for i in range(len(b10)):
        if str(i) not in x:
            fonk2(x + str(i))
def fonk3(b1):
    b8 = b1[:]
    b3.append(fonk4(b8))
    b8 = b1[:]
    b2.append(fonk5(b8))
    b8 = b1[:]
    b4.append(fonk6(b8))
    fonk1()
def fonk4(b1):
    a1 = 0
    for j in range(len(b1)):
        a1 += 1
        for i in range(len(b1) - 1 - j):
            a1 += 2
            if b1[i] > b1[i + 1]:
                a1 += 2
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
    return a1
def fonk5(b1):
    a1 = 0
    for j in range(len(b1)):
        a1 += 3
        a2 = 0
        for i in range(len(b1) - 1 - j):
            a1 += 2
            if b1[i] > b1[i + 1]:
                a1 += 2
                a2 += 1
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
        if a2 < 2:
            break
    return a1
def fonk6(b1):
    a1 = 0
    for j in range(len(b1)):
        a1 += 3
        b9 = False
        for i in range(len(b1) - 1 - j):
            a1 += 2
            if b1[i] > b1[i + 1]:
                a1 += 2
                b9 = True
                b1[i], b1[i + 1] = b1[i + 1], b1[i]
        if not b9:
            break
    return a1
b10 = '123456'
fonk2("")