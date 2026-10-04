import sys
class class1:
    def fonk1(self, n):
        self.b1 = [[] for _ in range(n)]
    def fonk2(self, u, v, b19):
        b2 = class2(v, u, b19)
        self.b1[u - 1].append(b2)
class class2:
    def fonk3(self, b3 = 0, b5=0, b6=float('inf')):
        self.b4 = b3
        self.b5 = b5
        self.b6 = b6
        self.a1 = 0
def fonk4(b2):
    b22.append(b2)
    b22[0] = len(b22) - 1
    fonk5(b22[0])
    b20[b2.b4 - 1].a1 = b22[0]
def fonk5(b8):
    while b8 > 1:
        b7 = b8
        if b22[b7].b6 > b22[b8].b6:
            fonk9(b8, b7)
            b8 = b7
        else:
            break
def fonk6():
    b20[b22[1].b4 - 1].a1 = 0
    b9 = b22[0]
    b20[b22[b9].b4 - 1].a1 = 1
    b10 = b22[1]
    b22[1] = b22[b9]
    b22[0] -= 1
    if b22[0] > 1:
        fonk8(1)
    b22.pop()
    return b10
def fonk7(heap_index, updated_distance, b5):
    if heap_index > 0:
        b22[heap_index].b6 = updated_distance
        b22[heap_index].b5 = b5
        fonk5(heap_index)
def fonk8(b8):
    while 2 * b8 <= b22[0]:
        b11 = 2 * b8
        b12 = 2 * b8 + 1
        b13 = b11
        if b12 <= b22[0] and b22[b12].b6 < b22[b11].b6:
            b13 = b12
        if b22[b13].b6 < b22[b8].b6:
            fonk9(b8, b13)
            b8 = b13
        else:
            break
def fonk9(index1, index2):
    b20[b22[index1].b4 - 1].a1 = index2
    b20[b22[index2].b4 - 1].a1 = index1
    b22[index1], b22[index2] = b22[index2], b22[index1]
def fonk10(b18, b21):
    fonk4(b21)
    b14 = []
    for i in range(len(b20)):
        if i != b21.b4 - 1:
            b2 = class2(i + 1)
            fonk4(b2)
    while len(b22) > 1:
        b10 = fonk6()
        b14.append(b10)
        for neighbor in b18.b1[b10.b4 - 1]:
            if neighbor.b6 < b20[neighbor.b4 - 1].b6:
                b20[neighbor.b4 - 1].b6 = neighbor.b6
                fonk7(b20[neighbor.b4 - 1].a1, neighbor.b6, b10.b4)
                b20[neighbor.b4 - 1].b5 = b10.b4
    return b14
if b15 = = "__main__":
    b16 = int(input("Enter the number of nodes: "))
    b17 = int(input("Enter the number of edges: "))
    b18 = class1(b16)
    for _ in range(b17):
        u, v, b19 = map(int, input("Enter edge (u, v, b19): ").split())
        b18.fonk4(u, v, b19)
        b18.fonk4(v, u, b19)
    b20 = [class2(i + 1) for i in range(b16)]
    b21 = class2(1, b6=0)
    b22 = [0]
    b23 = fonk10(b18, b21)
    b24 = sum(b2.b6 for b2 in b23 if b2.b4 != 0 and b2.b5 != 0)
    print(f"Total b6 of MST: {b24}")