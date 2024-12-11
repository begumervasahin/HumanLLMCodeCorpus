from random import randint, choice
class class1:
    def fonk1(self, coal, serial):
        self.b1 = serial
        self.b2 = coal
    def fonk2(self):
        return f'class1(b1 = {self.b1}, b2={self.b2})'
    def fonk3(self, other_coal):
        return self.b2 = = other_coal
    def fonk4(self, other_coal):
        return self.b2 > other_coal
    def fonk5(self, other_coal):
        return self.b2 < other_coal
    def fonk6(self, other_coal):
        return self.b2 >= other_coal
    def fonk7(self, other_coal):
        return self.b2 <= other_coal
    def fonk8(self, other_coal):
        return self.b2 != other_coal
class class2:
    def fonk9(self, num_cars):
        self.b3 = [class1(randint(1, 74), randint(1, 1000)) for _ in range(num_cars)]
    def fonk10(self):
        b4 = f'This b7 consists of {len(self.b3)} b3:\n'
        for b6 in self.b3:
            b4 += f'\t{str(b6)}\n'
        return b4
    def fonk11(self, b5, value):
        if b5 = = 'coal':
            b6 = class1(value, randint(1, 1000))
        else:
            b6 = class1(randint(1, 74), value)
        self.b3.append(b6)
        return b6
class class3:
    b7 = None
    @classmethod
    def fonk12(cls, num_cars):
        cls.b7 = class2(num_cars)
    @classmethod
    def fonk13(cls):
        cls.b7 = None
