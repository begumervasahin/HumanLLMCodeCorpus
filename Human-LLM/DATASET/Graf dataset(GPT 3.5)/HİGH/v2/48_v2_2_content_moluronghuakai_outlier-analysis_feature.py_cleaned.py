from math import sqrt
a1 = 0.1
a2 = 0
a3 = 1
a4 = 2
def fonk1(data, max_d):
    b1 = [data[0]]
    b2 = [0]
    b3 = a2
    a5 = 0.0
    for index in range(1, len(data)):
        if b3 = = a2:
            if data[index] > data[index - 1]:
                b3 = a3
            elif data[index] < data[index - 1]:
                b3 = a4
            continue
        if b3 = = a3 and data[index] < data[index - 1]:
            b3 = a4
            a5 = (data[index - 1] - b1[-1]) / max_d
            if a5 >= a1:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
        if b3 = = a4 and data[index] > data[index - 1]:
            b3 = a3
            a5 = (b1[-1] - data[index - 1]) / max_d
            if a5 >= a1:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
    return b1, b2
def fonk2(b10):
    b4 = []
    for index in range(1, len(b10[0])):
        b5 = (b10[0][index] - b10[0][index - 1]) / (b10[1][index] - b10[1][index - 1])
        b4.append(b5)
    return b4
def fonk3(data, b10):
    b6 = []
    for i in range(1, len(b10[0])):
        a6 = 0.0
        for j in range(b10[1][i-1], b10[1][i]):
            a6 += data[j]
        a6 = a6 / (b10[1][i] - b10[1][i-1])
        b6.append(a6)
    return b6
def fonk4(b4, b10, b6):
    b7 = []
    for index in range(1, len(b4)):
        b8 = sqrt((b4[index] - b4[index-1])**2 + (b10[1][index] - b10[1][index - 1])**2 + (b6[index] - b6[index-1])**2)
        b7.append(b8)
    return b7
b9 = (10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0)
b10 = fonk1(b9, 1)
b4 = fonk2(b10)
b6 = fonk3(b9, b10)
b11 = fonk4(b4, b10, b6)
print(b11)