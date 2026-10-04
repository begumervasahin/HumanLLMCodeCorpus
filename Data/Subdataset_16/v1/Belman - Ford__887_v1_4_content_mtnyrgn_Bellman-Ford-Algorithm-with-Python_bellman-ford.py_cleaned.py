class class1:
    def fonk1(self, b4):
        self.b1 = b4
        self.b2 = []
    def fonk2(self, b7, b8, b9):
        self.b2.append([b7, b8, b9])
    def fonk3(self, b3):
        print("Distance from source to each vertex:")
        for i in range(self.b1):
            print(f"{i} \t\t {b3[i]}")
    def fonk4(self, b10):
        b3 = [float("Inf")] * self.b1
        b3[b10] = 0
        for _ in range(self.b1 - 1):
            for b7, b8, b9 in self.b2:
                if b3[b7] != float("Inf") and b3[b7] + b9 < b3[b8]:
                    b3[b8] = b3[b7] + b9
        for b7, b8, b9 in self.b2:
            if b3[b7] != float("Inf") and b3[b7] + b9 < b3[b8]:
                print("class1 contains a negative-weight cycle")
                return
        self.fonk3(b3)
def fonk5():
    b4 = int(input("Enter number of b4:\n"))
    b5 = int(input("Enter number of b5:\n"))
    b6 = class1(b4)
    for i in range(b5):
        b7 = int(input("Source vertex:\n"))
        b8 = int(input("Destination vertex:\n"))
        b9 = int(input("Weight of edge:\n"))
        b6.fonk2(b7, b8, b9)
    b10 = int(input("Enter the source vertex:\n"))
    b6.fonk4(b10)
if b11 = = "__main__":
    fonk5()