from collections import namedtuple
b1 = namedtuple('b1', ['index', 'value'])
class class1:
    def fonk1(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = [b1(index, value) for index, value in enumerate(b4)]
    def fonk2(self):
        if not self.fonk3():
            return "Error: invalid input"
        a1 = 0
        for i in range(len(self.b5)):
            for j in range(i + 1, len(self.b5)):
                if (self.b5[i].value + self.b5[j].value) % self.b3 = = 0:
                    a1 += 1
        return a1
    def fonk3(self):
        return 2 <= self.b2 <= 100 and 1 <= self.b3 <= 100 and len(self.b4) <= 100
if b6 = = "__main__":
    b2 = 6
    b3 = 3
    b4 = [1, 3, 2, 6, 1, 2]
    b7 = class1(b2, b3, b4)
    b8 = b7.fonk2()
    print(b8)
