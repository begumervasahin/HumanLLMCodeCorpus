from collections import namedtuple
b1 = namedtuple('b1', ['index', 'value'])
class class1():
    def fonk1(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = [b1(index=index, value=value) for index, value in enumerate(b4)]
    def fonk2(self):
        if self.fonk3():
            return len(
                [
                    (x.value, y.value) for x in self.b5
                    for y in self.b5 if
                    (x.value + y.value) % self.b3 = = 0 and
                    x.index < y.index]
            )
        return "Error: invalid input"
    def fonk3(self):
        if self.b2 > 100 or self.b3 > 100 or len(self.b4) > 100 or self.b2 < 2 or self.b3 < 1 or len(self.b4) < 1:
            return False
        return True