class class1:
    def fonk1(self, b4):
        self.b1 = b4
        self.b2 = []
    def fonk2(self, b6, b7, b8):
        self.b2.append([b6, b7, b8])
    def fonk3(self, b3):
        print("Vertex Distance from Source")
        for i in range(self.b1):
            print(f"{i}\t\t{b3[i]}")
    def fonk4(self, b9):
        b3 = [float("inf")] * self.b1
        b3[b9] = 0
        for _ in range(self.b1 - 1):
            for b6, b7, b8 in self.b2:
                if b3[b6] != float("inf") and b3[b6] + b8 < b3[b7]:
                    b3[b7] = b3[b6] + b8
        for b6, b7, b8 in self.b2:
            if b3[b6] != float("inf") and b3[b6] + b8 < b3[b7]:
                print("class1 contains a negative-weight cycle")
                return
        self.fonk3(b3)
def fonk5():
    b4 = int(input("Enter the number of b4: "))
    b5 = int(input("Enter the number of b5: "))
    b2 = class1(b4)
    for _ in range(b5):
        b6 = int(input("Enter the source vertex: "))
        b7 = int(input("Enter the destination vertex: "))
        b8 = int(input("Enter the weight of the edge: "))
        b2.fonk2(b6, b7, b8)
    b9 = int(input("Enter the source vertex for Bellman-Ford algorithm: "))
    b2.fonk4(b9)
if b10 = = "__main__":
    fonk5()