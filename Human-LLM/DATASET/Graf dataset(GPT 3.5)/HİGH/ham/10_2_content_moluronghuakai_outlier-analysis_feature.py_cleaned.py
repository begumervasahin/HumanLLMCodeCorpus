from math import sqrt
a1 = 0.1
a2 = 0
a3 = 1
a4 = 2
def fonk1(data, max_d):
    "get peak from data"
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
            a5 = (data[index - 1] - b1[len(b1) - 1])/ max_d
            if a5 >= a1:
                b1.append(data[index - 1])
                b2 .append(index - 1)
            continue
        if b3 = = a4 and data[index] > data[index - 1]:
            b3 = a3
            a5 = (b1[len(b1) - 1] - data[index - 1]) / max_d
            if a5 >= a1:
                b1.append(data[index - 1])
                b2.append(index - 1)
            continue
    return (b1, b2)
def fonk2(peak):
    "calc b4 according to peak value"
    b4 = []
    a6 = 0.0
    for index in range(1, len(peak[0])):
        a6 = (peak[0][index] - peak[0][index - 1]) / (peak[1][index] - peak[1][index - 1])
        b4.append(a6)
    return b4
def fonk3(data,peak):
    "calc b5 according to peak value"
    b5 = []
    a7 = 0.0
    for i in range(1, len(peak[0])):
        for j in range(peak[1][i-1],peak[1][i]):
            b6 += data[j]
        b6 = b6 / (peak[1][i] - peak[1][i-1])
        b5.append(b6)
    return b5
def fonk4(b4,peak,b5):
    b7 = []
    a8 = 0.0
    for index in range(1, len(b4)):
        a8 = sqrt((b4[index]-b4[index-1])**2+(peak[1][index] - peak[1][index - 1])**2+(b5[index]-b5[index-1])**2)
        b7.append(a8)
    return b7
"temp data, [0, 100]"
b8 = (10.0, 11.0, 14.0, 13.0, 40.0, 39.0, 38.0, 60.0, 59.0, 62.0, 80.0, 81.0, 79.0, 78.0, 50.0, 52.0, 51.0, 53.0, 10.0, 9.0, 8.0, 50.0)
b9 = fonk4(b8, peak, b5)
print(b9)