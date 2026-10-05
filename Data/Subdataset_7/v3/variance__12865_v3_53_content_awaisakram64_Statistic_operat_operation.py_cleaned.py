class class1:
    def fonk1(self, b10):
        b1 = sorted(b10)
        b2 = len(b1)
        if b2 % b3 = = 0:
            b4 = b2
            return (b1[b4 - 1] + b1[b4]) / b3
        else:
            return b1[b2
    def fonk2(self, b10):
        b5 = {}
        for item in set(b10):
            b5[item] = b10.count(item)
        b6 = max(b5.values())
        if b6 <= 1:
            return [0]
        else:
            return [key for key, b7 in b5.items() if b7 = = b6]
    def fonk3(self, b10):
        return sum(b10) / len(b10)
    def fonk4(self, b10):
        b8 = self.fonk3(b10)
        return sum((item - b8) ** b3 for item in b10) / len(b10)
    def fonk5(self, b10):
        return (self.fonk4(b10)) ** 0.5
def fonk6():
    b9 = class1()
    with open("b10.txt", 'r') as file:
        b10 = [float(line.strip()) for line in file]
    print('Median is %.2f' % (b9.fonk1(b10)))
    print('Mean is %.2f' % (b9.fonk3(b10)))
    print('Mode is ' + (', '.join(map(str, b9.fonk2(b10)))))
    print('Variance is %.2f' % (b9.fonk4(b10)))
    print('Standard Deviation is %.2f' % (b9.fonk5(b10)))
if b11 = = "__main__":
    fonk6()