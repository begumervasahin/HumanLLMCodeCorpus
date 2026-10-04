import sys
class class1:
    def fonk1(self, n):
        self.b1 = [[] for _ in range(n)]
    def fonk2(self, u, b11, b16):
        b2 = class2()
        b2.b3 = b11
        b2.b4 = u
        b2.b5 = b16
        b2.a1 = 0
        self.b1[u - 1].append(b2)
class class2:
    def fonk3(self):
        self.a1 = 0
        self.b4 = 0
        self.b5 = float('inf')
        self.b3 = 0
    def fonk4(self):
        return self.b5
def fonk5(b2):
    b18.append(b2)
    b18[0] = len(b18) - 1
    fonk6(b18[0])
    b17[b2.b3 - 1].a1 = b18[0]
def fonk6(b7):
    while b7 > 1:
        b6 = b7
        if b18[b6].b5 > b18[b7].b5:
            b17[b18[b7].b3 - 1].a1 = b6
            b17[b18[b6].b3 - 1].a1 = b7
            b18[b7], b18[b6] = b18[b6], b18[b7]
            b7 = b6
        else:
            break
def fonk7():
    b17[b18[1].b3 - 1].a1 = 0
    b8 = b18[0]
    b17[b18[b8].b3 - 1].a1 = 1
    b9 = b18[1]
    b18[1] = b18[b8]
    b18[0] -= 1
    if b18[0] > 1:
        fonk9(1)
    b18.pop()
    return b9
def fonk8(heap_index, updated_distance, b4):
    if heap_index > 0:
        b18[heap_index].b5 = updated_distance
        b18[heap_index].b4 = b4
        fonk6(heap_index)
def fonk9(b7):
    while 2 * b7 <= b18[0]:
        if 2 * b7 = = b18[0] or b18[2 * b7].b5 < b18[2 * b7 + 1].b5:
            b6 = 2 * b7
        else:
            b6 = 2 * b7 + 1
        if b18[b6].b5 < b18[b7].b5:
            b17[b18[b7].b3 - 1].a1 = b6
            b17[b18[b6].b3 - 1].a1 = b7
            b18[b7], b18[b6] = b18[b6], b18[b7]
            b7 = b6
        else:
            break
def fonk10(b15, b16):
    fonk5(b16)
    b10 = []
    for i in range(len(b17)):
        if i != b16.b3 - 1:
            b2 = class2()
            b2.b3 = i + 1
            b2.a1 = 0
            b2.b5 = float('inf')
            b2.b4 = 0
            fonk5(b2)
    while len(b18) > 1:
        b11 = fonk7()
        b10.append(b11)
        for b2 in b15.b1[b11.b3 - 1]:
            if b2.b5 < b17[b2.b3 - 1].b5:
                b17[b2.b3 - 1].b5 = b2.b5
                fonk8(b17[b2.b3 - 1].a1, b2.b5, b11.b3)
                b17[b2.b3 - 1].b4 = b11.b3
    return b10
if b12 = = "__main__":
    b13 = int(input("Enter the number of nodes: "))
    b14 = int(input("Enter the number of edges: "))
    b15 = class1(b13)
    for _ in range(b14):
        u, b11, b16 = map(int, input("Enter edge (u, b11, b16): ").split())
        b15.fonk5(u, b11, b16)
        b15.fonk5(b11, u, b16)
    b17 = []
    for i in range(b13):
        b2 = class2()
        b2.b3 = i + 1
        b17.append(b2)
    b2 = class2()
    b2.b3 = 1
    b2.b5 = 0
    b18 = [0]
    b19 = fonk10(b15, b2)
    a2 = 0
    for b2 in b19:
        if b2.b3 != 0 and b2.b4 != 0:
            a2 += b2.b5
    print(f"Total b5 of MST: {a2}")