class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        b3 = []
        with open('data/topologies/PacificBell', 'r') as TopologyData:
            b4 = TopologyData.readline()
            b5 = TopologyData.readline()
            b6 = TopologyData.readline()
            for line in TopologyData:
                b7 = line.split()
                try:
                    b8 = b7[2]
                    self.b1.append(b8)
                except:
                    break
            b9 = TopologyData.readline()
            b10 = TopologyData.readline()
            b11 = TopologyData.readline()
            for line in TopologyData:
                b7 = line.split()
                try:
                    b12 = b7[2]
                    b13 = b7[3]
                    b14 = b7[4]
                    b3 = [b12, b13, b14]
                    self.b2.append(b3)
                except:
                    break