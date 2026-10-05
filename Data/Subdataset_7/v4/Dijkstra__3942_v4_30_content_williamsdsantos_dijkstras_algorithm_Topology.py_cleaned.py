class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        with open('b3/topologies/PacificBell', 'r') as topology_data:
            for _ in range(3):
                next(topology_data)
            for line in topology_data:
                b3 = line.split()
                if not b3:
                    break
                try:
                    b4 = b3[2]
                    self.b1.append(b4)
                except IndexError:
                    break
            for _ in range(3):
                next(topology_data)
            for line in topology_data:
                b3 = line.split()
                if not b3:
                    break
                try:
                    b5 = b3[2]
                    b6 = b3[3]
                    b7 = b3[4]
                    b8 = [b5, b6, b7]
                    self.b2.append(b8)
                except IndexError:
                    break
