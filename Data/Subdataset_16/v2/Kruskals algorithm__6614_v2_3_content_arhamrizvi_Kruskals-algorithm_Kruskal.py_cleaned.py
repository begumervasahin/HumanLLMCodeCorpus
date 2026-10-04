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
def fonk5(x, b10):
    if b10[x] != x:
        b10[x] = fonk5(b10[x], b10)
    return b10[x]
def fonk6(x, y, b10, b11):
    b5 = fonk5(x, b10)
    b6 = fonk5(y, b10)
    if b5 != b6:
        if b11[b5] > b11[b6]:
            b10[b6] = b5
        elif b11[b5] < b11[b6]:
            b10[b5] = b6
        else:
            b10[b6] = b5
            b11[b5] += 1
def fonk7(b13, b14):
    b7 = []
    with open(b13, 'r') as file:
        for line in file:
            u, v, b8 = map(int, line.split())
            b7.append([u, v, b8])
    b9 = max(max(u, v) for u, v, _ in b7) + 1
    b10 = list(range(b9))
    b11 = [0] * b9
    fonk2(b7)
    b12 = []
    for u, v, b8 in b7:
        if fonk5(u, b10) != fonk5(v, b10):
            b12.append([u, v, b8])
            fonk6(u, v, b10, b11)
    with open(b14, 'b8') as file:
        for u, v, b8 in b12:
            file.write(f"{u} {v} {b8}\n")
b13 = 'inputgraphfile.txt'
b14 = 'output_kruskal.txt'
fonk7(b13, b14)