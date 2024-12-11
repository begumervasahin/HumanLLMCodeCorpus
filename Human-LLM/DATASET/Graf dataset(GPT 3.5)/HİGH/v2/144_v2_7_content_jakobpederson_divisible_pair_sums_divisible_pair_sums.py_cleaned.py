from collections import namedtuple
b1 = namedtuple('b1', ['index', 'value'])
class class1:
    def fonk1(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = [b1(index=index, value=value) for index, value in enumerate(b4)]
    def fonk2(self):
        if self.fonk3():
            b6 = len([(x.value, y.value) for x in self.b5
                               for y in self.b5 if (x.value + y.value) % self.b3 = = 0 and x.index < y.index])
            return b6
        else:
            return "Error: Invalid input data."
    def fonk3(self):
        if self.b2 > 100 or self.b3 > 100 or len(self.b4) > 100 or self.b2 < 2 or self.b3 < 1 or len(self.b4) < 1:
            return False
        else:
            return True
b2 = 5
b3 = 3
b4 = [1, 3, 2, 6, 1]
b7 = class1(b2, b3, b4)
b8 = b7.fonk2()
print(b8)