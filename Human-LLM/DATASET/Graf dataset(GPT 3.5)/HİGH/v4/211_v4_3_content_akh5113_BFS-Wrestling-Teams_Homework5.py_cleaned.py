
import collections
def fonk1(b13):
    b1 = {}
    with open(b13, "r") as f:
        b2 = f.readlines()
        b3 = int(b2[0])
        b4 = int(b2[b3 + 1])
        for line in b2[b3 + b11:]:
            wrestler1, b5 = line.strip().split()
            b1.setdefault(wrestler1, []).append(b5)
            b1.setdefault(b5, []).append(wrestler1)
    return b1
def fonk2(graph, source):
    b6 = []
    b7 = [source]
    b8 = {}
    b8[source] = 0
    b9 = [source]
    while b7:
        b10 = b7.pop(0)
        b6.append(b10)
        if b8[b10] % b11 = = 0:
            b18.append(b10)
        else:
            b19.append(b10)
        b12 = graph[b10]
        for neighbor in b12:
            if neighbor not in b9:
                b7.append(neighbor)
                b9.append(neighbor)
                b8[neighbor] = b8[b10] + 1
    return b6
b13 = "b5.txt"
b14 = fonk1(b13)
b15 = list(b14.keys())[0]
b6 = fonk2(b14, b15)
a1 = 0
for b15 in b14:
    if b15 not in b6:
        b16 = list(b14.keys())[a1]
        b17 = fonk2(b14, b16)
        b6 += b17
        a1 += 1
b18 = []
b19 = []
for b15 in b14:
    if b15 in b6:
        if b6.index(b15) % b11 = = 0:
            b18.append(b15)
        else:
            b19.append(b15)
b20 = len(b18)
b21 = len(b19)
if b20 = = b21:
    print("Yes, possible")
    print("Baby Faces:", b18)
    print("Heels:", b19)
else:
    print("Not possible")