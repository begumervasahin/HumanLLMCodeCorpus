from math import sqrt
a1 = 0
a2 = 1
a3 = 2
def fonk1(b10, a5):
    b1 = [b10[0]]
    b2 = [0]
    b3 = a1
    for index in range(1, len(b10)):
        if b3 = = a1:
            if b10[index] > b10[index - 1]:
                b3 = a2
            elif b10[index] < b10[index - 1]:
                b3 = a3
            continue
        if b3 = = a2 and b10[index] < b10[index - 1]:
            b3 = a3
            b4 = (b10[index - 1] - b1[-1]) / a5
            if b4 >= a6:
                b1.append(b10[index - 1])
                b2.append(index - 1)
            continue
        if b3 = = a3 and b10[index] > b10[index - 1]:
            b3 = a2
            b4 = (b1[-1] - b10[index - 1]) / a5
            if b4 >= a6:
                b1.append(b10[index - 1])
                b2.append(index - 1)
            continue
    return b1, b2
def fonk2(b11):
    b5 = []
    for index in range(1, len(b11[0])):
        b6 = (b11[0][index] - b11[0][index - 1]) / (b11[1][index] - b11[1][index - 1])
        b5.append(b6)
    return b5
def fonk3(b10, b11):
    b7 = []
    for i in range(1, len(b11[0])):
        a4 = 0.0
        for j in range(b11[1][i-1], b11[1][i]):
            a4 += b10[j]
        b8 = a4 / (b11[1][i] - b11[1][i-1])
        b7.append(b8)
    return b7
def fonk4(b5, b11, b7):
    b9 = []
    for index in range(1, len(b5)):
        b4 = sqrt((b5[index] - b5[index - 1]) ** 2 +
                        (b11[1][index] - b11[1][index - 1]) ** 2 +
                        (b7[index] - b7[index - 1]) ** 2)
        b9.append(b4)
    return b9
b10 = (10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0)
a5 = 100
a6 = 0.1
b11 = fonk1(b10, a5)
b5 = fonk2(b11)
b7 = fonk3(b10, b11)
b9 = fonk4(b5, b11, b7)
print(b9)