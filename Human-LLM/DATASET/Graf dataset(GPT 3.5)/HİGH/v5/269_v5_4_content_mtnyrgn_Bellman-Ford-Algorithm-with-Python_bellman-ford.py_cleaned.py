class class1:
    def fonk1(self, vertices):
        self.b1 = vertices
        self.b2 = []
    def fonk2(self, u, v, weight):
        self.b2.append((u, v, weight))
    def fonk3(self, b3):
        print("Distances:")
        for i, distance in enumerate(b3):
            print(f"{i}\t\t{distance}")
    def fonk4(self, source):
        b3 = [float("inf")] * self.b1
        b3[source] = 0
        for _ in range(self.b1 - 1):
            for u, v, weight in self.b2:
                if b3[u] != float("inf") and b3[u] + weight < b3[v]:
                    b3[v] = b3[u] + weight
        for u, v, weight in self.b2:
            if b3[u] != float("inf") and b3[u] + weight < b3[v]:
                print("class1 contains negative cycle!!")
                return
        self.fonk3(b3)
b1 = int(input("Enter number of vertices: "))
b4 = int(input("Enter number of b2: "))
b5 = class1(b1)
for _ in range(b4):
    b6 = int(input("Source vertex: "))
    b7 = int(input("Destination vertex: "))
    b8 = int(input("Weight of Edge: "))
    b5.fonk2(b6, b7, b8)
b5.fonk4(0)