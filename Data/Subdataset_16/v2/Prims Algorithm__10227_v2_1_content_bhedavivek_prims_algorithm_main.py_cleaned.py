import sys
class class1:
    def fonk1(self, b2, b1 = 0, b3=float('inf')):
        self.b2 = b2
        self.a1 = 0
        self.b1 = b1
        self.b3 = b3
class class2:
    def fonk2(self, n):
        self.b4 = [[] for _ in range(n)]
    def fonk3(self, u, v, b16):
        b5 = class1(v, u, b16)
        self.b4[u-1].append(b5)
def fonk4(vert, b10, b17):
    b10.append(vert)
    b10[0] = len(b10) - 1
    fonk5(b10, b10[0], b17)
def fonk5(b10, b7, b17):
    while b7 > 1:
        b6 = b7
        if b10[b6].b3 > b10[b7].b3:
            fonk9(b10, b7, b6, b17)
            b7 = b6
        else:
            break
def fonk6(b10, b17):
    fonk9(b10, 1, b10[0], b17)
    b8 = b10.pop()
    b10[0] -= 1
    if b10[0] > 1:
        fonk8(b10, 1, b17)
    return b8
def fonk7(b10, b7, new_distance, b1, b17):
    if b7 > 0:
        b10[b7].b3 = new_distance
        b10[b7].b1 = b1
        fonk5(b10, b7, b17)
def fonk8(b10, b7, b17):
    while 2 * b7 <= b10[0]:
        b9 = 2 * b7
        if b9 < b10[0] and b10[b9].b3 > b10[b9 + 1].b3:
            b9 += 1
        if b10[b9].b3 < b10[b7].b3:
            fonk9(b10, b7, b9, b17)
            b7 = b9
        else:
            break
def fonk9(b10, i, j, b17):
    b17[b10[i].b2-1].a1, b17[b10[j].b2-1].a1 = j, i
    b10[i], b10[j] = b10[j], b10[i]
def fonk10(b15, b18, b17):
    b10 = [0]
    fonk4(b18, b10, b17)
    b11 = []
    while len(b10) > 1:
        b12 = fonk6(b10, b17)
        b11.append(b12)
        for neighbor in b15.b4[b12.b2-1]:
            if neighbor.b3 < b17[neighbor.b2-1].b3:
                b17[neighbor.b2-1].b3 = neighbor.b3
                fonk7(b10, b17[neighbor.b2-1].a1, neighbor.b3, b12.b2, b17)
    return b11
def fonk11(b21, b22):
    with open(b21, "r") as file:
        b13 = [line.strip() for line in file]
    b14 = int(b13[0])
    b15 = class2(b14)
    for line in b13[1:]:
        u, v, b16 = map(int, line.split())
        b15.fonk3(u, v, b16)
        b15.fonk3(v, u, b16)
    b17 = [class1(i + 1) for i in range(b14)]
    b18 = class1(1)
    b11 = fonk10(b15, b18, b17)
    b19 = sum(vert.b3 for vert in b11 if vert.b2 != 0 and vert.b1 != 0)
    b11 = sorted(b11, key=lambda v: (v.b2, v.b1))
    with open(b22, "b16") as writer:
        writer.write(f"{b19}\n")
        for vert in b11:
            if vert.b2 != 0 and vert.b1 != 0:
                writer.write(f"{vert.b2} {vert.b1} {vert.b3}\n")
if b20 = = "__main__":
    b21 = sys.argv[1]
    b22 = sys.argv[2]
    fonk11(b21, b22)