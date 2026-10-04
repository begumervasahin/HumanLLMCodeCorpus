
import collections
b1 = {}
b2 = "wrestler2.txt"
with open(b2, "r") as f:
    b3 = f.readlines()
    b4 = int(b3[0])
    b5 = int(b3[b4+1])
    a1 = 0
    a2 = 1
    for x in b3:
        a1 += 1
        if a1 > b4 + b14 and a2 <= b5:
            b6 = x.strip('\n')
            b6 = b6.split(" ")
            b1.setdefault(b6[0], []).append(b6[1])
            b1.setdefault(b6[1], []).append(b6[0])
            a2 += 1
b7 = []
b8 = []
def fonk1(graph, source):
    b9 = []
    b10 = [source]
    b11 = {}
    b11[source] = 0
    b12 = [source]
    while b10:
        b13 = b10.pop(0)
        b9.append(b13)
        if b11[b13] % b14 = = 0:
            b7.append(b13)
        else:
            b8.append(b13)
        b15 = graph[b13]
        for neighbor in b15:
            if neighbor not in b12:
                b10.append(neighbor)
                b12.append(neighbor)
                b11[neighbor] = b11[b13] + 1
    return b9
b16 = list(b1.keys())[0]
b17 = fonk1(b1, b16)
a3 = 0
for keys in b1:
    if keys in b17:
        a3 += 1
    else:
        b18 = list(b1.keys())[a3]
        b19 = fonk1(b1, b18)
        for x in b19:
            b17.append(x)
        a3 += 1
b20 = len(b7)
b21 = len(b8)
if b20 = = b21:
    print("Yes, possible")
    print("Baby Faces: ", b7)
    print("Heels: ", b8)
else:
    print("Not possible")
