class class1:
    def fonk1(self, b1 = 'b4/topologies/PacificBell'):
        self.b2 = []
        self.b3 = []
        self.fonk2(b1)
    def fonk2(self, b1):
        with open(b1, 'r') as topology_data:
            self.fonk3(topology_data, 3)
            self.fonk4(topology_data)
            self.fonk3(topology_data, 3)
            self.fonk5(topology_data)
    def fonk3(self, file, num_lines):
        for _ in range(num_lines):
            next(file)
    def fonk4(self, file):
        for line in file:
            b4 = line.split()
            if len(b4) < 3:
                break
            b5 = b4[2]
            self.b2.append(b5)
    def fonk5(self, file):
        for line in file:
            b4 = line.split()
            if len(b4) < 5:
                break
            b6 = b4[2]
            b7 = b4[3]
            b8 = b4[4]
            self.b3.append([b6, b7, b8])
def fonk6():
    b9 = class1()
    print("Nodes:", b9.b2)
    print("Links:", b9.b3)
if b10 = = "__main__":
    fonk6()