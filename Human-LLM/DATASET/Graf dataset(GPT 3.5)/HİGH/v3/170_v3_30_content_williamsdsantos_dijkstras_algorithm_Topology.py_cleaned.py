class class1:
    def fonk1(self, filename):
        self.b1 = []
        self.b2 = []
        with open(filename, 'r') as topology_file:
            for _ in range(3):
                next(topology_file)
            for line in topology_file:
                b3 = line.split()
                if not b3:
                    break
                b4 = b3[2]
                self.b1.append(b4)
            for _ in range(3):
                next(topology_file)
            for line in topology_file:
                b3 = line.split()
                if not b3:
                    break
                origin, destination, b5 = b3[2:5]
                self.b2.append([origin, destination, b5])
b6 = class1('b3/topologies/PacificBell')
print("Nodes:", b6.b1)
print("Links:", b6.b2)