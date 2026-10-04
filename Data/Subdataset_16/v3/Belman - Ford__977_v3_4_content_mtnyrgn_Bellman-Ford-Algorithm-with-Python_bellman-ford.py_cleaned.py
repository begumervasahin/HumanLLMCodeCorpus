class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, b5, b6, b7):
        self.b2.append([b5, b6, b7])
    def fonk3(self, b3):
        print("Vertex Distance from Source")
        for vertex, distance in enumerate(b3):
            print(f"{vertex}\t\t{distance}")
    def fonk4(self, b5):
        b3 = [float("inf")] * self.b1
        b3[b5] = 0
        for _ in range(self.b1 - 1):
            for u, v, w in self.b2:
                if b3[u] != float("inf") and b3[u] + w < b3[v]:
                    b3[v] = b3[u] + w
        for u, v, w in self.b2:
            if b3[u] != float("inf") and b3[u] + w < b3[v]:
                print("class1 contains a negative-b7 cycle")
                return
        self.fonk3(b3)
def fonk5():
    b1 = int(input("Enter the number of b1: "))
    b2 = int(input("Enter the number of b2: "))
    b4 = class1(b1)
    for _ in range(b2):
        b5 = int(input("Enter the b5 vertex: "))
        b6 = int(input("Enter the b6 vertex: "))
        b7 = int(input("Enter the b7 of the edge: "))
        b4.fonk2(b5, b6, b7)
    b8 = int(input("Enter the b5 vertex for the Bellman-Ford algorithm: "))
    b4.fonk4(b8)
if b9 = = "__main__":
    fonk5()