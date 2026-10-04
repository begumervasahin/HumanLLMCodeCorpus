class class1:
    def fonk1(self, b9):
        self.b1 = []
        self.b2 = []
        self.fonk2(b9)
    def fonk2(self, b9):
        with open(b9, 'r') as topology_data:
            for _ in range(3):
                next(topology_data)
            self.fonk3(topology_data)
            for _ in range(3):
                next(topology_data)
            self.fonk4(topology_data)
    def fonk3(self, topology_data):
        for line in topology_data:
            b3 = line.split()
            if len(b3) < 3:
                break
            b4 = b3[2]
            self.b1.append(b4)
    def fonk4(self, topology_data):
        for line in topology_data:
            b3 = line.split()
            if len(b3) < 5:
                break
            b5 = b3[2]
            b6 = b3[3]
            b7 = b3[4]
            b8 = [b5, b6, b7]
            self.b2.append(b8)
def fonk5():
    b9 = 'b3/topologies/PacificBell'
    b10 = class1(b9)
    print("Nodes:", b10.b1)
    print("Links:", b10.b2)
if b11 = = "__main__":
    fonk5()