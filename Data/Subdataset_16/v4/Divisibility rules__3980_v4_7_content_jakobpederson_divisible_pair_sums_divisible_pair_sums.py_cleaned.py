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
        b6 = [
            (x.value, y.value) for x in self.b5
            for y in self.b5
            if (x.value + y.value) % self.b3 = = 0 and x.index < y.index
        ]
        return len(b6)
    def fonk3(self):
        return 2 <= self.b2 <= 100 and 1 <= self.b3 <= 100 and len(self.b4) <= 100
if b7 = = "__main__":
    b2 = 6
    b3 = 3
    b4 = [1, 3, 2, 6, 1, 2]
    b8 = class1(b2, b3, b4)
    b9 = b8.fonk2()
    print(b9)
