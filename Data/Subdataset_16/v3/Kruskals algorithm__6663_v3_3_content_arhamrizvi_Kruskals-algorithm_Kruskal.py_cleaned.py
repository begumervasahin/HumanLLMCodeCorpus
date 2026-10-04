def fonk1(array, i, j):
    array[i], array[j] = array[j], array[i]
def fonk2(array):
    fonk3(array, 0, len(array) - 1)
def fonk3(array, start, end):
    if start < end:
        b1 = fonk4(array, start, end)
        fonk3(array, start, b1 - 1)
        fonk3(array, b1 + 1, end)
def fonk4(array, start, end):
    b2 = (start + end)
    b3 = array[b2][2]
    fonk1(array, b2, end)
    b4 = start
    for i in range(start, end):
        if array[i][2] < b3:
            fonk1(array, i, b4)
            b4 += 1
    fonk1(array, b4, end)
    return b4
def fonk5(x, b12):
    if b12[x] != x:
        b12[x] = fonk5(b12[x], b12)
    return b12[x]
def fonk6(x, y, b12, b9):
    b5 = fonk5(x, b12)
    b6 = fonk5(y, b12)
    if b5 != b6:
        if b9[b5] > b9[b6]:
            b12[b6] = b5
        elif b9[b5] < b9[b6]:
            b12[b5] = b6
        else:
            b12[b6] = b5
            b9[b5] += 1
def fonk7(b13, b14):
    b7 = fonk8(b13)
    b8 = fonk9(b7)
    b12, b9 = fonk10(b8)
    fonk2(b7)
    b10 = fonk11(b7, b12, b9)
    fonk12(b10, b14)
def fonk8(filename):
    b7 = []
    with open(filename, 'r') as file:
        for line in file:
            u, v, b11 = map(int, line.split())
            b7.append([u, v, b11])
    return b7
def fonk9(b7):
    return max(max(u, v) for u, v, _ in b7) + 1
def fonk10(b8):
    b12 = list(range(b8))
    b9 = [0] * b8
    return b12, b9
def fonk11(b7, b12, b9):
    b10 = []
    for u, v, b11 in b7:
        if fonk5(u, b12) != fonk5(v, b12):
            b10.append([u, v, b11])
            fonk6(u, v, b12, b9)
    return b10
def fonk12(b10, filename):
    with open(filename, 'b11') as file:
        for u, v, b11 in b10:
            file.write(f"{u} {v} {b11}\n")
b13 = 'inputgraphfile.txt'
b14 = 'output_kruskal.txt'
fonk7(b13, b14)