import sys
class class1:
    def fonk1(self, v):
        self.b1 = v
        self.b2 = [{} for _ in range(v)]
        self.b3 = [sys.maxsize] * v
        self.b4 = [False] * v
        self.b5 = []
    def fonk2(self):
        for i in range(self.b1):
            print("For", i, "=", self.b2[i])
    def fonk3(self):
        for i in range(self.b1):
            print("Bellman-Ford", i, "=", self.b3[i])
def fonk4(b9, src, dest, weight):
    b9.b2[src][dest] = weight
def fonk5(b9):
    while b9.b5:
        fonk6(b9, b9.b5.pop())
def fonk6(b9, source):
    if b9.b4[source]:
        return
    b6 = []
    a1 = 0
    b7 = sys.maxsize
    for dest, weight in b9.b2[source].items():
        b8 = b9.b3[source] + weight
        b6.append(b8)
        if b9.b3[dest] > b8:
            b9.b3[dest] = b8
            b9.b5.insert(0, dest)
            b9.b4[dest] = False
    for dest, _ in b9.b2[source].items():
        if not b9.b4[dest] and dest not in b9.b5:
            b9.b5.insert(0, dest)
    b9.b4[source] = True
def fonk7(b9, source):
    b9.b3[source] = 0
    b9.b5.insert(0, source)
    fonk4(b9, 0, 1, 4)
    fonk4(b9, 0, 2, 2)
    fonk4(b9, 1, 2, 3)
    fonk4(b9, 1, 3, 2)
    fonk4(b9, 1, 4, 3)
    fonk4(b9, 2, 1, 1)
    fonk4(b9, 2, 3, 4)
    fonk4(b9, 2, 4, 5)
    fonk4(b9, 4, 3, -5)
b9 = class1(5)
fonk7(b9, 0)
fonk5(b9)
b9.fonk3()