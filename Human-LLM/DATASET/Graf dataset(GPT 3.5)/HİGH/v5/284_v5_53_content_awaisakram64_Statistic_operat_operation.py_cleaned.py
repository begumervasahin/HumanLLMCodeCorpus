class class1:
    def fonk1(self, b10):
        b1 = sorted(b10)
        b2 = len(b1)
        if b2 % b3 = = 0:
            return (b1[b2
        else:
            return b1[b2
    def fonk2(self, b10):
        b4 = {}
        for item in set(b10):
            b4[item] = b10.count(item)
        b5 = max(b4.values())
        if b5 <= 1:
            return [0]
        else:
            return [key for key, b6 in b4.items() if b6 = = b5]
    def fonk3(self, b10):
        return sum(b10) / len(b10)
    def fonk4(self, b10):
        b7 = self.fonk3(b10)
        return sum((x - b7) ** b3 for x in b10) / len(b10)
    def fonk5(self, b10):
        b8 = self.fonk4(b10)
        return b8 ** 0.5
def fonk6():
    b9 = class1()
    with open("b10.txt", 'r') as file:
        b10 = [float(line.strip()) for line in file]
    print('Mean: {:.2f}'.format(b9.fonk3(b10)))
    print('Median: {:.2f}'.format(b9.fonk1(b10)))
    print('Mode: {}'.format(', '.join(map(str, b9.fonk2(b10)))))
    print('Variance: {:.2f}'.format(b9.fonk4(b10)))
    print('Standard Deviation: {:.2f}'.format(b9.fonk5(b10)))
if b11 = = "__main__":
    fonk6()