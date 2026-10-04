class class1:
    def fonk1(self, b10):
        self.b1 = []
        self.b2 = []
        with open(b10, 'r') as topology_data:
            b3 = [topology_data.readline() for _ in range(3)]
            for line in topology_data:
                b4 = line.split()
                if len(b4) < 3:
                    break
                b5 = b4[2]
                self.b1.append(b5)
            b3 += [topology_data.readline() for _ in range(3)]
            for line in topology_data:
                b4 = line.split()
                if len(b4) < 5:
                    break
                b6 = b4[2]
                b7 = b4[3]
                b8 = b4[4]
                b9 = [b6, b7, b8]
                self.b2.append(b9)
def fonk2():
    b10 = 'b4/topologies/PacificBell'
    b11 = class1(b10)
    print("b1:", b11.b1)
    print("b2:", b11.b2)
if b12 = = "__main__":
    fonk2()