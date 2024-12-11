import heapq
class class1:
    b1 = []
    b2 = set()
    b3 = {}
    b4 = {}
    b5 = []
b6 = class1()
def fonk1(file, d):
    b7 = open(file)
    for lines in b7:
        b8 = [x.strip() for x in lines.split(f'{d}')]
        b9 = b8[0]
        b10 = b8[1]
        b11 = b8[2]
        if((int(b11),b10,b9) in b6.b1):
            continue
        heapq.heappush(b6.b1, (int(b11),b9,b10))
        b6.b2.add(b9)
        b6.b2.add(b10)
    return b6.b1
def fonk2(v):
     b6.b3[v] = v
     b6.b4[v] = 0
def fonk3(v):
    if(b6.b3[v] != v):
        b6.b3[v] = fonk3(b6.b3[v])
    return b6.b3[v]
def fonk4(b9, b10):
    b12 = fonk3(b9)
    b13 = fonk3(b10)
    if(b12 != b13):
        if(b6.b4[b12] > b6.b4[b13]):
            b6.b3[b13] = b12
        else:
            b6.b3[b12] = b13
            b6.b4[b13] += 1
def fonk5():
    a1 = 0
    for v in b6.b2:
        fonk2(v)
    while(b6.b1):
        e,b9,b10 = heapq.heappop(b6.b1)
        if(fonk3(b9) != fonk3(b10)):
            fonk4(b9, b10)
            a1 += e
            b6.b5.append((b9, b10, str(e), str(a1)))
    return (b6.b5, a1)
b14 = "graph.txt"
b15 = ","
fonk1(b14, b15)
mst, b16 = fonk5()
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total Weight of b5:", b16)