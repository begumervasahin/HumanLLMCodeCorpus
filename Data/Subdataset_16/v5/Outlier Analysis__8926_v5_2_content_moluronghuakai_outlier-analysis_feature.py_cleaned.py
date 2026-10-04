import math
a1 = 0
a2 = 1
a3 = 2
a4 = 0.1
def fonk1(data, max_d):
    b1 = [data[0]]
    b2 = [0]
    b3 = a1
    for index in range(1, len(data)):
        if b3 = = a1:
            if data[index] > data[index - 1]:
                b3 = a2
            elif data[index] < data[index - 1]:
                b3 = a3
            continue
        if b3 = = a2 and data[index] < data[index - 1]:
            b3 = a3
            if (data[index - 1] - b1[-1]) / max_d >= a4:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
        if b3 = = a3 and data[index] > data[index - 1]:
            b3 = a2
            if (b1[-1] - data[index - 1]) / max_d >= a4:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
    return b1, b2
def fonk2(b8):
    b1, b2 = b8
    b4 = [
        (b1[i] - b1[i - 1]) / (b2[i] - b2[i - 1])
        for i in range(1, len(b1))
    ]
    return b4
def fonk3(data, b8):
    b1, b2 = b8
    b5 = [
        sum(data[b2[i - 1]:b2[i]]) / (b2[i] - b2[i - 1])
        for i in range(1, len(b1))
    ]
    return b5
def fonk4(b4, b8, b5):
    _, b2 = b8
    b6 = [
        math.sqrt(
            (b4[i] - b4[i - 1]) ** 2 +
            (b2[i] - b2[i - 1]) ** 2 +
            (b5[i] - b5[i - 1]) ** 2
        )
        for i in range(1, len(b4))
    ]
    return b6
b7 = [
    10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0,
    79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0
]
b8 = fonk1(b7, max_d=100.0)
b4 = fonk2(b8)
b5 = fonk3(b7, b8)
b6 = fonk4(b4, b8, b5)
print(b6)