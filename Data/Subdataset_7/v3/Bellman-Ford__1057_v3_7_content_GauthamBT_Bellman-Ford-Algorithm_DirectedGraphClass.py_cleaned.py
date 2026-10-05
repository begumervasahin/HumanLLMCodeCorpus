import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = [{} for _ in range(b1)]
        self.b3 = [sys.maxsize] * b1
        self.b4 = [False] * b1
        self.b5 = []
    def fonk2(self):
        for vertex, neighbors in enumerate(self.b2):
            print(f"Adjacent vertices for {vertex}: {neighbors}")
    def fonk3(self):
        for vertex, shortest_dist in enumerate(self.b3):
            print(f"Bellman-Ford shortest path to {vertex}: {shortest_dist}")
def fonk4(b7, src, dest, weight):
    b7.b2[src][dest] = weight
def fonk5(b7):
    while b7.b5:
        fonk6(b7, b7.b5.pop())
def fonk6(b7, source):
    if b7.b4[source]:
        return
    for dest, weight in b7.b2[source].items():
        b6 = b7.b3[source] + weight
        if b7.b3[dest] > b6:
            b7.b3[dest] = b6
            b7.b5.insert(0, dest)
            b7.b4[dest] = False
    b7.b4[source] = True
def fonk7(b7, source):
    b7.b3[source] = 0
    b7.b5.insert(0, source)
    fonk4(b7, 0, 1, 4)
    fonk4(b7, 0, 2, 2)
    fonk4(b7, 1, 2, 3)
    fonk4(b7, 1, 3, 2)
    fonk4(b7, 1, 4, 3)
    fonk4(b7, 2, 1, 1)
    fonk4(b7, 2, 3, 4)
    fonk4(b7, 2, 4, 5)
    fonk4(b7, 4, 3, -5)
b7 = class1(5)
fonk7(b7, 0)
fonk5(b7)
b7.fonk3()