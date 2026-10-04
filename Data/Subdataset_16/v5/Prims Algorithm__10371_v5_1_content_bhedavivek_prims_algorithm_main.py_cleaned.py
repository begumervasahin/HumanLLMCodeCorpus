import sys
class class1:
    def fonk1(self, b1 = 0, b2=0, b3=float('inf'), b4=0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
class class2:
    def fonk2(self, n):
        self.b5 = [[] for _ in range(n)]
    def fonk3(self, u, b13, b17):
        b6 = class1(b1=b13, b2=u, b3=b17)
        self.b5[u-1].append(b6)
def fonk4(vertex, b18, b19):
    b19.append(vertex)
    b19[0] = len(b19) - 1
    fonk5(b19[0], b18, b19)
    b18[vertex.b1 - 1].b4 = b19[0]
def fonk5(b8, b18, b19):
    while b8 > 1:
        b7 = b8
        if b19[b7].b3 > b19[b8].b3:
            fonk9(b8, b7, b18, b19)
            b8 = b7
        else:
            break
def fonk6(b18, b19):
    b18[b19[1].b1 - 1].b4 = 0
    b9 = b19[0]
    b18[b19[b9].b1 - 1].b4 = 1
    b10 = b19[1]
    b19[1] = b19[b9]
    b19[0] -= 1
    if b19[0] > 1:
        fonk8(1, b18, b19)
    b19.pop()
    return b10
def fonk7(heap_index, updated_distance, b2, b18, b19):
    if heap_index > 0:
        b19[heap_index].b3 = updated_distance
        b19[heap_index].b2 = b2
        fonk5(heap_index, b18, b19)
def fonk8(b8, b18, b19):
    while 2 * b8 <= b19[0]:
        b11 = 2 * b8
        if b11 < b19[0] and b19[b11].b3 > b19[b11 + 1].b3:
            b11 += 1
        if b19[b11].b3 < b19[b8].b3:
            fonk9(b8, b11, b18, b19)
            b8 = b11
        else:
            break
def fonk9(index1, index2, b18, b19):
    b18[b19[index1].b1 - 1].b4 = index2
    b18[b19[index2].b1 - 1].b4 = index1
    b19[index1], b19[index2] = b19[index2], b19[index1]
def fonk10(b16, b20, b18, b19):
    fonk4(b20, b18, b19)
    b12 = []
    for i in range(len(b18)):
        if i != b20.b1 - 1:
            b6 = class1(b1=i + 1)
            fonk4(b6, b18, b19)
    while len(b19) > 1:
        b13 = fonk6(b18, b19)
        b12.append(b13)
        for b6 in b16.b5[b13.b1 - 1]:
            if b6.b3 < b18[b6.b1 - 1].b3:
                b18[b6.b1 - 1].b3 = b6.b3
                fonk7(b18[b6.b1 - 1].b4, b6.b3, b13.b1, b18, b19)
                b18[b6.b1 - 1].b2 = b13.b1
    return b12
def fonk11(b24, b25):
    with open(b24, "r") as file:
        b14 = file.readlines()
    b15 = int(b14[0].split()[0])
    b16 = class2(b15)
    for line in b14[1:]:
        u, b13, b17 = map(int, line.split())
        b16.fonk4(u, b13, b17)
        b16.fonk4(b13, u, b17)
    global b18, b19
    b18 = [class1(b1=i + 1) for i in range(b15)]
    b19 = [0]
    b20 = class1(b1=1)
    b21 = fonk10(b16, b20, b18, b19)
    b22 = sum(b6.b3 for b6 in b21 if b6.b2 != 0)
    b21 = sorted((b6 for b6 in b21 if b6.b2 != 0), key=lambda b13: (b13.b1, b13.b2))
    with open(b25, "b17") as writer:
        writer.write(str(b22))
        for b6 in b21:
            writer.write(f"\n{b6.b1} {b6.b2} {b6.b3}")
if b23 = = "__main__":
    b24 = sys.argv[1]
    b25 = sys.argv[2]
    fonk11(b24, b25)