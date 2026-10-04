
import collections
def fonk1(b13):
    b1 = {}
    with open(b13, "r") as f:
        b2 = f.readlines()
        b3 = int(b2[0])
        b4 = int(b2[b3 + 1])
        for i in range(b3 + b12, b3 + b12 + b4):
            wrestler1, b5 = b2[i].strip().split(" ")
            b1.setdefault(wrestler1, []).append(b5)
            b1.setdefault(b5, []).append(wrestler1)
    return b1
def fonk2(graph, start):
    b6 = collections.deque([start])
    b7 = {start: 0}
    b8 = set([start])
    b9 = []
    b10 = []
    while b6:
        b11 = b6.popleft()
        if b7[b11] % b12 = = 0:
            b9.append(b11)
        else:
            b10.append(b11)
        for neighbor in graph[b11]:
            if neighbor not in b8:
                b6.append(neighbor)
                b8.add(neighbor)
                b7[neighbor] = b7[b11] + 1
    return b9, b10, b8
def fonk3():
    b13 = "b5.txt"
    b1 = fonk1(b13)
    b14 = []
    b15 = []
    b16 = set()
    for wrestler in b1.keys():
        if wrestler not in b16:
            b9, b10, b8 = fonk2(b1, wrestler)
            b14.extend(b9)
            b15.extend(b10)
            b16.update(b8)
    if len(b14) + len(b15) == len(b1):
        print("Yes, possible")
        print("Baby Faces:", b14)
        print("Heels:", b15)
    else:
        print("Not possible")
if b17 = = "__main__":
    fonk3()
