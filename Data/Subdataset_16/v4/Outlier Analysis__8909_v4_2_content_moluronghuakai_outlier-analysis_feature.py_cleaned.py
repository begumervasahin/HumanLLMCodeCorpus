import math
a1 = 0
a2 = 1
a3 = 2
a4 = 0.1
def fonk1(data, max_d):
    b1 = [data[0]]
    b2 = [0]
    b3 = a1
    a5 = 0.0
    for index in range(1, len(data)):
        if b3 = = a1:
            if data[index] > data[index - 1]:
                b3 = a2
            elif data[index] < data[index - 1]:
                b3 = a3
            continue
        if b3 = = a2 and data[index] < data[index - 1]:
            b3 = a3
            a5 = (data[index - 1] - b1[-1]) / max_d
            if a5 >= a4:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
        if b3 = = a3 and data[index] > data[index - 1]:
            b3 = a2
            a5 = (b1[-1] - data[index - 1]) / max_d
            if a5 >= a4:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
    return b1, b2
def fonk2(peak):
    b4 = []
    for index in range(1, len(peak[0])):
        b5 = (peak[0][index] - peak[0][index - 1]) / (peak[1][index] - peak[1][index - 1])
        b4.append(b5)
    return b4
def fonk3(data, peak):
    b6 = []
    for i in range(1, len(peak[0])):
        b7 = sum(data[peak[1][i-1]:peak[1][i]])
        b8 = b7 / (peak[1][i] - peak[1][i-1])
        b6.append(b8)
    return b6
def fonk4(b4, b12, b6):
    b9 = []
    for index in range(1, len(b4)):
        b10 = math.sqrt(
            (b4[index] - b4[index - 1]) ** 2 +
            (b12[1][index] - b12[1][index - 1]) ** 2 +
            (b6[index] - b6[index - 1]) ** 2
        )
        b9.append(b10)
    return b9
b11 = [10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0]
b12 = fonk1(b11, max_d=100.0)
b4 = fonk2(b12)
b6 = fonk3(b11, b12)
b9 = fonk4(b4, b12, b6)
print(b9)