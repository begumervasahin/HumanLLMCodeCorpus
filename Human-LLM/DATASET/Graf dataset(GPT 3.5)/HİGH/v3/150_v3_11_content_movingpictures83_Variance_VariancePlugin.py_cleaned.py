class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = []
        self.b3 = []
    def fonk2(self, b1):
        self.b1 = b1
    def fonk3(self):
        with open(self.b1, 'r') as file:
            b4 = file.readlines()
            self.b2 = b4[0].strip().split(',')
            self.b2 = [bacterium for bacterium in self.b2 if bacterium != '""']
            for line in b4[1:]:
                b5 = [float(value) for value in line.strip().split(',')[1:]]
                self.b3.append(b5)
    def fonk4(self, b3):
        b6 = sum(b3) / len(b3)
        b7 = sum((b6 - value) ** 2 for value in b3) / len(b3)
        return b7
    def fonk5(self, b1):
        with open(b1, 'w') as file:
            file.write("Element\tVariance\n\n")
            b8 = []
            for i in range(len(self.b2)):
                if self.b3[i]:
                    b7 = self.fonk4(self.b3[i])
                    b8.append((b7, self.b2[i]))
            b8.sort(b9 = True)
            for b7, bacterium in b8:
                file.write(f"{bacterium}\t{b7}\n")
if b10 = = "__main__":
    b11 = class1()
    b11.fonk2("b3.txt")
    b11.fonk3()
    b11.fonk5("output.txt")