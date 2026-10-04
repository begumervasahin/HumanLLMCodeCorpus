
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
        self.b3 = float('inf')
        self.b4 = False
    def fonk2(self, neighbor, b5 = 0):
        self.b2[neighbor] = b5
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self):
        return self.b1
    def fonk5(self, neighbor):
        return self.b2[neighbor]
    def fonk6(self, dist):
        self.b3 = dist
    def fonk7(self):
        return self.b3
    def fonk8(self):
        self.b4 = True
    def fonk9(self):
        return self.b4
from vertice import class1
class class2:
    def fonk10(self, b6 = False):
        self.b7 = {}
        self.b6 = b6
    def fonk11(self, b1):
        b8 = class1(b1)
        self.b7[b1] = b8
        return b8
    def fonk12(self, from_vert, to_vert, b5 = 0):
        if from_vert not in self.b7:
            self.fonk11(from_vert)
        if to_vert not in self.b7:
            self.fonk11(to_vert)
        self.b7[from_vert].fonk2(self.b7[to_vert], b5)
        if not self.b6:
            self.b7[to_vert].fonk2(self.b7[from_vert], b5)
    def fonk13(self):
        return [b8 for k, b8 in self.b7.items()]
    def fonk14(self, b1):
        return self.b7.get(b1)
    def fonk15(self):
        b9 = set()
        for b1, b8 in self.b7.items():
            for neighbor in b8.b2:
                b9.add((b8, neighbor))
        return b9
    def fonk16(self):
        return iter(self.b7.values())
if b10 = = "__main__":
    b11 = class2(b6=False)
    b11.fonk12(0, 1, 4)
    b11.fonk12(0, 2, 1)
    b11.fonk12(2, 1, 2)
    b11.fonk12(1, 3, 1)
    b11.fonk12(2, 3, 5)
    b11.fonk12(3, 4, 3)
    print("Vertices of b11:")
    for b12 in b11:
        print(f"class1 {b12.b1}")
    print("\nEdges of b11:")
    for edge in b11.fonk15():
        print(f"Edge from {edge[0].fonk4()} to {edge[1].fonk4()} with b5 {edge[0].fonk5(edge[1])}")
    a1 = 2
    b12 = b11.fonk14(a1)
    if b12:
        print(f"\nVertex {b12.fonk4()} found in b11")
    else:
        print(f"\nVertex {a1} not found in b11")