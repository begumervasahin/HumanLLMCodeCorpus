from math import sqrt
a1 = 0.1
a2 = 0
a3 = 1
a4 = 2
def fonk1(data, a5):
    b1 = [data[0]]
    b2 = [0]
    b3 = a2
    for index in range(1, len(data)):
        if b3 = = a2:
            if data[index] > data[index - 1]:
                b3 = a3
            elif data[index] < data[index - 1]:
                b3 = a4
            continue
        if b3 = = a3 and data[index] < data[index - 1]:
            b3 = a4
            b4 = (data[index - 1] - b1[-1]) / a5
            if b4 >= a1:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
        if b3 = = a4 and data[index] > data[index - 1]:
            b3 = a3
            b4 = (b1[-1] - data[index - 1]) / a5
            if b4 >= a1:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
    return b1, b2
def fonk2(b13):
    b1, b2 = b13
    b5 = []
    for index in range(1, len(b1)):
        b6 = (b1[index] - b1[index - 1]) / (b2[index] - b2[index - 1])
        b5.append(b6)
    return b5
def fonk3(data, b13):
    _, b2 = b13
    b7 = []
    for i in range(1, len(b2)):
        b8 = sum(data[b2[i-1]:b2[i]])
        b9 = b8 / (b2[i] - b2[i-1])
        b7.append(b9)
    return b7
def fonk4(b5, b13, b7):
    _, b2 = b13
    b10 = []
    for index in range(1, len(b5)):
        b11 = sqrt(
            (b5[index] - b5[index - 1])**2 +
            (b2[index] - b2[index - 1])**2 +
            (b7[index] - b7[index - 1])**2
        )
        b10.append(b11)
    return b10
b12 = [
    10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0,
    79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0
]
a5 = 50.0
b13 = fonk1(b12, a5)
b5 = fonk2(b13)
b7 = fonk3(b12, b13)
b10 = fonk4(b5, b13, b7)
print("Distances between consecutive b5, b13, and b7:", b10)