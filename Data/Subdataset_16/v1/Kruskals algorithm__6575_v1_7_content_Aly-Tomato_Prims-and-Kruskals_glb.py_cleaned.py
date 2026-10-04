b1 = {}
b2 = []
b3 = []
b4 = {}
b5 = {}
b6 = []
b7 = set()
def fonk1():
    b8 = "Vertex 1"
    b9 = "Vertex 2"
    b10 = "Distance"
    b11 = "Cumulative Distance"
    print("******************************************************************************")
    print(b8.ljust(15, ' '), "\t", b9.ljust(15, ' '), "\t", b10.ljust(10, ' '), "\t", b11.ljust(10, ' '))
    print("******************************************************************************")
    for m in b2:
        v1, v2, w, b12 = m
        print(v1.ljust(15, ' '), "\t", v2.ljust(15, ' '), "\t", str(w).ljust(10, ' '), "\t", str(b12).ljust(15, ' '))
def fonk2(vertice):
    b4[vertice] = vertice
    b5[vertice] = 0
def fonk3(vertice):
    if b4[vertice] != vertice:
        b4[vertice] = fonk3(b4[vertice])
    return b4[vertice]
def fonk4(vertice1, vertice2):
    b13 = fonk3(vertice1)
    b14 = fonk3(vertice2)
    if b13 != b14:
        if b5[b13] < b5[b14]:
            b4[b13] = b14
        else:
            b4[b14] = b13
            if b5[b13] == b5[b14]:
                b5[b13] += 1
def fonk5():
    global b2
    a1 = 0
    for vertice in b7:
        fonk2(vertice)
    b6.sort(b15 = lambda x: x[2])
    for edge in b6:
        v1, v2, b16 = edge
        if fonk3(v1) != fonk3(v2):
            fonk4(v1, v2)
            a1 += b16
            b2.append((v1, v2, b16, a1))
if b17 = = "__main__":
    b7 = {'A', 'B', 'C', 'D', 'E'}
    b6 = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 2),
        ('B', 'D', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'E', 5)
    ]
    fonk5()
    fonk1()