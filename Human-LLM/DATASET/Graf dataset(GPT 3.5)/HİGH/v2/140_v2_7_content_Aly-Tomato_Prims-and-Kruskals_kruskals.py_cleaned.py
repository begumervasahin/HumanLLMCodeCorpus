import heapq
class class1:
    b1 = []
    b2 = set()
    b3 = {}
    b4 = {}
    b5 = []
b6 = class1()
def fonk1(file, b12):
    with open(file) as file_path:
        for line in file_path:
            v1, b10, b7 = map(str.strip, line.split(b12))
            if (int(b7), b10, v1) in b6.b1:
                continue
            heapq.heappush(b6.b1, (int(b7), v1, b10))
            b6.b2.add(v1)
            b6.b2.add(b10)
    return b6.b1
def fonk2(v):
    b6.b3[v] = v
    b6.b4[v] = 0
def fonk3(v):
    if b6.b3[v] != v:
        b6.b3[v] = fonk3(b6.b3[v])
    return b6.b3[v]
def fonk4(v1, b10):
    b8 = fonk3(v1)
    b9 = fonk3(b10)
    if b8 != b9:
        if b6.b4[b8] > b6.b4[b9]:
            b6.b3[b9] = b8
        else:
            b6.b3[b8] = b9
            if b6.b4[b8] == b6.b4[b9]:
                b6.b4[b9] += 1
def fonk5():
    a1 = 0
    for v in b6.b2:
        fonk2(v)
    while b6.b1:
        b7, v1, b10 = heapq.heappop(b6.b1)
        if fonk3(v1) != fonk3(b10):
            fonk4(v1, b10)
            a1 += b7
            b6.b5.append((v1, b10, str(b7), str(a1)))
    return (b6.b5, a1)
b11 = "graph.txt"
b12 = ","
fonk1(b11, b12)
mst, a1 = fonk5()
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total Weight of b5:", a1)