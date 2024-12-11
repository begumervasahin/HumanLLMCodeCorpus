import sys
class class1:
    def fonk1(self, filename):
        self.b1 = filename
    def fonk2(self):
        with open(self.b1, 'r') as filestuff:
            b2 = filestuff.readline()
            self.b3 = b2.strip().split(',')
            if '\"\"' in self.b3:
                self.b3.remove('\"\"')
            self.b4 = len(self.b3)
            self.b5 = [[] for _ in range(self.b4)]
            for line in filestuff:
                b6 = line.strip().split(',')
                for j in range(len(b6) - 1):
                    b7 = float(b6[j + 1])
                    self.b5[j].append(b7)
    def fonk3(self, filename):
        with open(filename, 'w') as filestuff2:
            filestuff2.write("Element\tVariance\b4\b4")
            b8 = []
            for i in range(self.b4):
                if len(self.b5[i]) != 0:
                    b9 = sum(self.b5[i]) / len(self.b5[i])
                    b10 = sum((b9 - x) ** 2 for x in self.b5[i]) / len(self.b5[i])
                    b8.append((b10, self.b3[i]))
            b8.sort(b11 = True)
            for b10, element in b8:
                filestuff2.write(f"{element}\t{b10}\b4")
if b12 = = "__main__":
    b13 = class1()
    b13.fonk1("data.txt")
    b13.fonk2()
    b13.fonk3("output.txt")