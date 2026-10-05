class class1:
    def fonk1(self, filename):
        self.b1 = []
        self.b2 = []
        with open(filename, 'r') as topology_file:
            self.fonk2(topology_file, 3)
            self.fonk3(topology_file)
            self.fonk2(topology_file, 3)
            self.fonk4(topology_file)
    def fonk2(self, file_obj, num_lines):
        for _ in range(num_lines):
            next(file_obj)
    def fonk3(self, file_obj):
        for line in file_obj:
            b3 = line.split()
            if not b3:
                break
            try:
                b4 = b3[2]
                self.b1.append(b4)
            except IndexError:
                break
    def fonk4(self, file_obj):
        for line in file_obj:
            b3 = line.split()
            if not b3:
                break
            try:
                origin, destination, b5 = b3[2:5]
                b6 = [origin, destination, b5]
                self.b2.append(b6)
            except IndexError:
                break
