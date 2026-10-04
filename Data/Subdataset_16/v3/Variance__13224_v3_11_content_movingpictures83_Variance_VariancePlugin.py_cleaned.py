import numpy as np
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
    def fonk2(self, filename):
        self.b3 = filename
    def fonk3(self):
        with open(self.b3, 'r') as file:
            b4 = file.readline().strip()
            self.b1 = [name for name in b4.split(',') if name != '\"\"']
            b5 = len(self.b1)
            self.b2 = [[] for _ in range(b5)]
            for line in file:
                b6 = line.strip().split(',')
                for index in range(1, len(b6)):
                    self.b2[index - 1].append(float(b6[index]))
    def fonk4(self, filename):
        b7 = []
        for index, b6 in enumerate(self.b2):
            if b6:
                b8 = np.var(b6)
                b7.append((b8, self.b1[index]))
        b7.sort(b9 = True)
        with open(filename, 'w') as file:
            file.write("Element\tVariance\n\n")
            for b8, name in b7:
                file.write(f"{name}\t{b8:.6f}\n")
