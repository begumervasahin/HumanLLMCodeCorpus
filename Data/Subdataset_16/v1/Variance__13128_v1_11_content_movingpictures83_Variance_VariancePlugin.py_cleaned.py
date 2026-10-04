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
            self.b1 = [item for item in b4.split(',') if item != '\"\"']
            self.b5 = len(self.b1)
            self.b2 = [[] for _ in range(self.b5)]
            for line in file:
                b6 = line.strip().split(',')
                for j in range(1, len(b6)):
                    b7 = float(b6[j])
                    self.b2[j-1].append(b7)
    def fonk4(self, filename):
        b8 = []
        for i in range(self.b5):
            if len(self.b2[i]) > 0:
                b9 = np.array(self.b2[i])
                b10 = np.var(b9)
                b8.append((b10, self.b1[i]))
        b8.sort(b11 = True)
        with open(filename, 'w') as file:
            file.write("Element\tVariance\b5\b5")
            for b10, name in b8:
                file.write(f"{name}\t{b10:.6f}\b5")
