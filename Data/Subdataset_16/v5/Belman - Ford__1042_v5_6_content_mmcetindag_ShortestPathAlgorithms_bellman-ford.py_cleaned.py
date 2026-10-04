class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, source, destination, weight):
        self.b2.append([source, destination, weight])
    def fonk3(self, b3):
        print("Vertex Distance from Source")
        for vertex, distance in enumerate(b3):
            print(f"{vertex}\t\t{distance}")
    def fonk4(self, source):
        b3 = [float("inf")] * self.b1
        b3[source] = 0
        for _ in range(self.b1 - 1):
            for u, v, w in self.b2:
                if b3[u] != float("inf") and b3[u] + w < b3[v]:
                    b3[v] = b3[u] + w
        for u, v, w in self.b2:
            if b3[u] != float("inf") and b3[u] + w < b3[v]:
                print("class1 contains a negative weight cycle")
                return
        self.fonk3(b3)
def fonk5():
    b4 = class1(5)
    b2 = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for source, destination, weight in b2:
        b4.fonk2(source, destination, weight)
    a1 = 0
    b4.fonk4(a1)
if b5 = = "__main__":
    fonk5()