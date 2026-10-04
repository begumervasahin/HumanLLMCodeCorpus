class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, start, end, weight):
        self.b2.append((start, end, weight))
    def fonk3(self, b3):
        print("Vertex   Distance from Source")
        for vertex, distance in enumerate(b3):
            print(f"{vertex} \t\t {distance}")
    def fonk4(self, source):
        b3 = [float("inf")] * self.b1
        b3[source] = 0
        for _ in range(self.b1 - 1):
            for start, end, weight in self.b2:
                if b3[start] != float("inf") and b3[start] + weight < b3[end]:
                    b3[end] = b3[start] + weight
        for start, end, weight in self.b2:
            if b3[start] != float("inf") and b3[start] + weight < b3[end]:
                print("class1 contains a negative weight cycle")
                return
        self.fonk3(b3)
if b4 = = "__main__":
    b5 = class1(5)
    b5.fonk2(0, 1, -1)
    b5.fonk2(0, 2, 4)
    b5.fonk2(1, 2, 3)
    b5.fonk2(1, 3, 2)
    b5.fonk2(1, 4, 2)
    b5.fonk2(3, 2, 5)
    b5.fonk2(3, 1, 1)
    b5.fonk2(4, 3, -3)
    b5.fonk4(0)