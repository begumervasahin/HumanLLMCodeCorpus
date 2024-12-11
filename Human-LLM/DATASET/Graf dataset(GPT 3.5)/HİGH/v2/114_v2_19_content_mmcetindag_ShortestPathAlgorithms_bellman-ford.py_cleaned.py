from collections import defaultdict
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, src, dest, weight):
        self.b2.append((src, dest, weight))
    def fonk3(self, b3):
        print("Vertex   Distance from Source")
        for i in range(self.b1):
            print("%d \t\t %d" % (i, b3[i]))
    def fonk4(self, source):
        b3 = [float("inf")] * self.b1
        b3[source] = 0
        for _ in range(self.b1 - 1):
            for u, v, w in self.b2:
                if b3[u] != float("inf") and b3[u] + w < b3[v]:
                    b3[v] = b3[u] + w
        for u, v, w in self.b2:
            if b3[u] != float("inf") and b3[u] + w < b3[v]:
                print("class1 contains negative weight cycle")
                return
        self.fonk3(b3)
b4 = class1(5)
b4.fonk2(0, 1, -1)
b4.fonk2(0, 2, 4)
b4.fonk2(1, 2, 3)
b4.fonk2(1, 3, 2)
b4.fonk2(1, 4, 2)
b4.fonk2(3, 2, 5)
b4.fonk2(3, 1, 1)
b4.fonk2(4, 3, -3)
b4.fonk4(0)