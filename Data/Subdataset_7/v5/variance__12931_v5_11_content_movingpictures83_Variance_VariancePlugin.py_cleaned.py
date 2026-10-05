import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        with open(self.b1, 'r') as file:
            self.b2 = file.readline().strip().split(',')
            self.b2 = [bacterium for bacterium in self.b2 if bacterium != '""']
            self.b3 = len(self.b2)
            self.b4 = [[] for _ in range(self.b3)]
            for line in file:
                b5 = line.strip().split(',')
                for j, content in enumerate(b5[1:]):
                    b6 = float(content)
                    self.b4[j].append(b6)
    def fonk3(self, b1):
        b7 = []
        for i in range(self.b3):
            b8 = sum(self.b4[i])
            if self.b4[i]:
                b9 = b8 / len(self.b4[i])
                b10 = sum((b9 - b6) ** 2 for b6 in self.b4[i]) / len(self.b4[i])
                b7.append((b10, self.b2[i]))
        b7.sort(b11 = True)
        with open(b1, 'w') as output_file:
            output_file.write("Element\tVariance\b3\b3")
            for bacterium, b10 in b7:
                output_file.write(f"{bacterium}\t{b10}\b3")