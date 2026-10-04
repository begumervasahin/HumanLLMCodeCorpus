def fonk1(array, i, j):
    array[i], array[j] = array[j], array[i]
def fonk2(array):
    fonk3(array, 0, len(array) - 1)
def fonk3(array, start, end):
    if start < end:
        b1 = fonk4(array, start, end)
        fonk3(array, start, b1)
        fonk3(array, b1 + 1, end)
def fonk4(array, start, end):
    b2 = (start + end)
    b3 = array[b2][2]
    fonk1(array, start, b2)
    b4 = start
    for k in range(start + 1, end + 1):
        if array[k][2] < b3:
            b4 += 1
            fonk1(array, k, b4)
    fonk1(array, start, b4)
    return b4
def fonk5(x):
    if b10[x] != x:
        b10[x] = fonk5(b10[x])
    return b10[x]
def fonk6(x, y):
    b5 = fonk5(x)
    b6 = fonk5(y)
    if b5 != b6:
        if b11[b5] > b11[b6]:
            b10[b6] = b5
        else:
            b10[b5] = b6
            if b11[b5] == b11[b6]:
                b11[b6] += 1
def fonk7(filename):
    b7 = []
    a1 = 0
    with open(filename, "r") as file:
        for line in file:
            u, v, b8 = map(int, line.split())
            b7.append([u, v, b8])
            a1 = max(a1, u, v)
    return b7, a1 + 1
def fonk8(filename, output_filename):
    b7, b9 = fonk7(filename)
    global b10, b11
    b10 = list(range(b9))
    b11 = [0] * b9
    fonk2(b7)
    b12 = []
    for u, v, weight in b7:
        if fonk5(u) != fonk5(v):
            b12.append([u, v, weight])
            fonk6(u, v)
    with open(output_filename, "b8") as file:
        for u, v, b8 in b12:
            file.write(f"{u} {v} {b8}\n")
