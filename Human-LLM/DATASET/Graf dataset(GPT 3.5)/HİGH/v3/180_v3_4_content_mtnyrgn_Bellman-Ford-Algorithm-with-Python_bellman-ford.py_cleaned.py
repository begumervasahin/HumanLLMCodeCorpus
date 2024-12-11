class class1:
    def fonk1(self, b4):
        self.b1 = b4
        self.b2 = []
    def fonk2(self, b7, b8, b9):
        self.b2.append([b7, b8, b9])
    def fonk3(self, b3):
        print("Distance:")
        for i in range(self.b1):
            print("%d \t\t %d" % (i, b3[i]))
    def fonk4(self, src):
        b3 = [float("Inf")] * self.b1
        b3[src] = 0
        for _ in range(self.b1 - 1):
            for b7, b8, b9 in self.b2:
                if b3[b7] != float("Inf") and b3[b7] + b9 < b3[b8]:
                    b3[b8] = b3[b7] + b9
        for b7, b8, b9 in self.b2:
            if b3[b7] != float("Inf") and b3[b7] + b9 < b3[b8]:
                print("class1 contains negative cycle!!")
                return
        self.fonk3(b3)
b4 = int(input("Enter number of b4: "))
b5 = int(input("Enter number of b5: "))
b6 = class1(b4)
for i in range(b5):
    b7 = int(input("Source vertex: "))
    b8 = int(input("Destination vertex: "))
    b9 = int(input("Weight of Edge: "))
    b6.fonk2(b7, b8, b9)
b6.fonk4(0)