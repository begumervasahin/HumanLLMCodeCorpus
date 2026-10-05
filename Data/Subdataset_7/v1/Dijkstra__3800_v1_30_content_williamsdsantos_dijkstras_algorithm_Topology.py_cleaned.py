class class1:
    def fonk1(self, filename):
        self.b1 = []
        self.b2 = []
        with open(filename, 'r') as TopologyData:
            next(TopologyData)
            for line in TopologyData:
                b3 = line.split()
                if len(b3) == 0:
                    break
                b4 = b3[2]
                self.b1.append(b4)
            next(TopologyData)
            for line in TopologyData:
                b3 = line.split()
                if len(b3) == 0:
                    break
                origin, destination, b5 = b3[2:5]
                self.b2.append([origin, destination, b5])
b6 = class1('b3/topologies/PacificBell')
print("b1:", b6.b1)
print("b2:", b6.b2)