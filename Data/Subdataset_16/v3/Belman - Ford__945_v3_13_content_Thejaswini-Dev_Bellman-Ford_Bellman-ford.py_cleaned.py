class class1:
    def fonk1(self, vertices):
        self.b1 = vertices
        self.b2 = []
    def fonk2(self, u, v, w):
        self.b2.append([u, v, w])
    def fonk3(self, b3):
        print("Vertex   Distance from Source")
        for i in range(self.b1):
            print(f"{i}\t\t{b3[i]}")
    def fonk4(self, src):
        b3 = [float("Inf")] * self.b1
        b3[src] = 0
        for _ in range(self.b1 - 1):
            for u, v, w in self.b2:
                if b3[u] != float("Inf") and b3[u] + w < b3[v]:
                    b3[v] = b3[u] + w
        for u, v, w in self.b2:
            if b3[u] != float("Inf") and b3[u] + w < b3[v]:
                print("class1 contains a negative weight cycle")
                return
        self.fonk3(b3)
def fonk5():
    b2 = class1(5)
    b4 = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for u, v, w in b4:
        b2.fonk2(u, v, w)
    b2.fonk4(0)
if b5 = = "__main__":
    fonk5()