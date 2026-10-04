from collections import deque
class class1:
    def fonk1(self, b7, green, blue):
        self.b1 = b7
        self.b2 = green
        self.b3 = blue
        self.b4 = None
    def fonk2(self):
        return any([
            self.b1 > 0 and self.b2 = = 0 and self.b3 == 0,
            self.b2 > 0 and self.b1 = = 0 and self.b3 == 0,
            self.b3 > 0 and self.b1 = = 0 and self.b2 == 0
        ])
    def fonk3(self):
        return self.fonk7(self.b1 - 1, self.b2 - 1, self.b3 + 2)
    def fonk4(self):
        return self.fonk7(self.b1 + 2, self.b2 - 1, self.b3 - 1)
    def fonk5(self):
        return self.fonk7(self.b1 - 1, self.b2 + 2, self.b3 - 1)
    def fonk6(self):
        b5 = deque([str(self)])
        b4 = self.b4
        while b4:
            b5.appendleft(str(b4))
            b4 = b4.b4
        return b5
    def fonk7(self, b7, green, blue):
        if b7 < 0 or green < 0 or blue < 0:
            raise ValueError('Invalid chameleon count')
        b6 = class1(b7, green, blue)
        b6.b4 = self
        return b6
    def fonk8(self):
        return f'(b7 = {self.b1}, green={self.b2}, blue={self.b3})'
if b8 = = "__main__":
    b9 = class1(b7=13, green=16, blue=17)
    print("Initial state:", b9)
    b10 = b9.fonk3()
    print("Next state:", b10)
    print("Path to next state:", list(b10.fonk6()))