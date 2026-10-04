
import collections
def fonk1(b19):
    b1 = {}
    with open(b19, "r") as f:
        b2 = f.readlines()
        b3 = int(b2[0])
        b4 = int(b2[b3 + 1])
        for count, line in enumerate(b2):
            if count > b3 + b11 and count <= b3 + b11 + b4:
                wrestler1, b5 = line.strip().split()
                b1.setdefault(wrestler1, []).append(b5)
                b1.setdefault(b5, []).append(wrestler1)
    return b1, b3, b4
def fonk2(graph, source, b12, b13):
    b6 = []
    b7 = collections.deque([source])
    b8 = {source: 0}
    b9 = {source}
    while b7:
        b10 = b7.popleft()
        b6.append(b10)
        if b8[b10] % b11 = = 0:
            b12.append(b10)
        else:
            b13.append(b10)
        for neighbor in graph[b10]:
            if neighbor not in b9:
                b7.append(neighbor)
                b9.add(neighbor)
                b8[neighbor] = b8[b10] + 1
    return b6
def fonk3(b19):
    b1, b3, b4 = fonk1(b19)
    b12 = []
    b13 = []
    b14 = list(b1.keys())[0]
    b15 = fonk2(b1, b14, b12, b13)
    for key in b1:
        if key not in b15:
            b15 += fonk2(b1, key, b12, b13)
    b16 = len(b12)
    b17 = len(b13)
    if b16 = = b17:
        print("Yes, possible")
        print("Baby Faces:", b12)
        print("Heels:", b13)
    else:
        print("Not possible")
if b18 = = "__main__":
    b19 = "b5.txt"
    fonk3(b19)