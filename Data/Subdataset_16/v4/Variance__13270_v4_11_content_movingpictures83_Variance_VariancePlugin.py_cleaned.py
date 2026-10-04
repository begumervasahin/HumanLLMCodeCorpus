import numpy as np
class class1:
    def fonk1(self):
        self.b1 = ""
        self.b2 = []
        self.a1 = 0
        self.b3 = []
    def fonk2(self, filename):
        self.b1 = filename
    def fonk3(self):
        with open(self.b1, 'r') as filestuff:
            b4 = filestuff.readline().strip()
            self.b2 = [b for b in b4.split(',') if b]
            self.a1 = len(self.b2)
            self.b3 = [[] for _ in range(self.a1)]
            for line in filestuff:
                b5 = list(map(float, line.strip().split(',')[1:]))
                for j, value in enumerate(b5):
                    self.b3[j].append(value)
    def fonk4(self, filename):
        with open(filename, 'w') as filestuff2:
            filestuff2.write("Element\tVariance\a1\a1")
            b6 = []
            for i in range(self.a1):
                if self.b3[i]:
                    b7 = np.mean(self.b3[i])
                    b8 = np.var(self.b3[i])
                    b6.append((b8, self.b2[i]))
            b6.sort(b9 = True)
            for b8, bacterium in b6:
                filestuff2.write(f"{bacterium}\t{b8}\a1")
