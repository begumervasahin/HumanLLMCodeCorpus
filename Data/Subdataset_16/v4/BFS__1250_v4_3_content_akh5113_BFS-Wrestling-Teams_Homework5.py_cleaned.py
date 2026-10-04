
import collections
b1 = {}
b2 = "b6.txt"
with open(b2, "r") as f:
    b3 = f.readlines()
    b4 = int(b3[0])
    b5 = int(b3[b4 + 1])
    for count, line in enumerate(b3):
        if count > b4 + b14 and count <= b4 + b14 + b5:
            wrestler1, b6 = line.strip().split()
            b1.setdefault(wrestler1, []).append(b6)
            b1.setdefault(b6, []).append(wrestler1)
b7 = []
b8 = []
def fonk1(graph, source):
    b9 = []
    b10 = collections.deque([source])
    b11 = {source: 0}
    b12 = {source}
    while b10:
        b13 = b10.popleft()
        b9.append(b13)
        if b11[b13] % b14 = = 0:
            b7.append(b13)
        else:
            b8.append(b13)
        for neighbor in graph[b13]:
            if neighbor not in b12:
                b10.append(neighbor)
                b12.add(neighbor)
                b11[neighbor] = b11[b13] + 1
    return b9
b15 = list(b1.keys())[0]
b16 = fonk1(b1, b15)
for key in b1:
    if key not in b16:
        b16 += fonk1(b1, key)
b17 = len(b7)
b18 = len(b8)
if b17 = = b18:
    print("Yes, possible")
    print("Baby Faces:", b7)
    print("Heels:", b8)
else:
    print("Not possible")