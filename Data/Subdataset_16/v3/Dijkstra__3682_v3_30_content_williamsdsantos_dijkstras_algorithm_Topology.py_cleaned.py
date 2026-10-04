class class1:
    def fonk1(self, b8):
        self.b1 = []
        self.b2 = []
        self.fonk2(b8)
    def fonk2(self, b8):
        with open(b8, 'r') as file:
            self.fonk3(file, 3)
            self.fonk4(file)
            self.fonk3(file, 3)
            self.fonk5(file)
    def fonk3(self, file, num_lines):
        for _ in range(num_lines):
            next(file)
    def fonk4(self, file):
        for line in file:
            b3 = line.split()
            if len(b3) < 3:
                break
            b4 = b3[2]
            self.b1.append(b4)
    def fonk5(self, file):
        for line in file:
            b3 = line.split()
            if len(b3) < 5:
                break
            b5 = b3[2]
            b6 = b3[3]
            b7 = b3[4]
            self.b2.append([b5, b6, b7])
def fonk6():
    b8 = 'b3/topologies/PacificBell'
    b9 = class1(b8)
    print("Nodes:", b9.b1)
    print("Links:", b9.b2)
if b10 = = "__main__":
    fonk6()