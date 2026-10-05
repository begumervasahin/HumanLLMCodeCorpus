import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [{} for _ in range(b1)]
        self.b3 = [sys.maxsize] * b1
        self.b4 = [False] * b1
        self.b5 = []
    def fonk2(self):
        for vertex in range(self.b1):
            print(f"For vertex {vertex}, adjacent vertices: {self.b2[vertex]}")
    def fonk3(self):
        for vertex in range(self.b1):
            print(f"Bellman-Ford shortest path to vertex {vertex}: {self.b3[vertex]}")
def fonk4(b8, src, dest, weight):
    b8.b2[src][dest] = weight
def fonk5(b8):
    while b8.b5:
        fonk6(b8, b8.b5.pop())
def fonk6(b8, source):
    if b8.b4[source]:
        return
    b6 = []
    for dest, weight in b8.b2[source].items():
        b7 = b8.b3[source] + weight
        b6.append(b7)
        if b8.b3[dest] > b7:
            b8.b3[dest] = b7
            b8.b5.insert(0, dest)
            b8.b4[dest] = False
    b8.b4[source] = True
def fonk7(b8, source):
    b8.b3[source] = 0
    b8.b5.insert(0, source)
    fonk4(b8, 0, 1, 4)
    fonk4(b8, 0, 2, 2)
    fonk4(b8, 1, 2, 3)
    fonk4(b8, 1, 3, 2)
    fonk4(b8, 1, 4, 3)
    fonk4(b8, 2, 1, 1)
    fonk4(b8, 2, 3, 4)
    fonk4(b8, 2, 4, 5)
    fonk4(b8, 4, 3, -5)
b8 = class1(5)
fonk7(b8, 0)
fonk5(b8)
b8.fonk3()