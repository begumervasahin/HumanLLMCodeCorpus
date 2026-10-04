import random
class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
    def fonk2(self, b3):
        if self.b3:
            if b3 < self.b3:
                if self.b1 is None:
                    self.b1 = class1(b3)
                else:
                    self.b1.fonk2(b3)
            elif b3 > self.b3:
                if self.b2 is None:
                    self.b2 = class1(b3)
                else:
                    self.b2.fonk2(b3)
        else:
            self.b3 = b3
    def fonk3(self, value):
        if value < self.b3:
            if self.b1 is None:
                return f"{value} Not Found"
            return self.b1.fonk3(value)
        elif value > self.b3:
            if self.b2 is None:
                return f"{value} Not Found"
            return self.b2.fonk3(value)
        else:
            return f"{self.b3} is found"
    def fonk4(self):
        if self.b1:
            self.b1.fonk4()
        print(self.b3, b4 = ' ')
        if self.b2:
            self.b2.fonk4()
class class2:
    def fonk5(self, rect_params, b7, b8, b9, b10, b5, default):
        self.b5 = b5
        self.x, self.y, self.width, self.b6 = rect_params
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b11 = b5
        self.b12 = default
        self.b13 = default
    def fonk6(self):
        b14 = 200 if len(self.b7) == 3 else self.b7[3]
        fill(self.b7[0], self.b7[1], self.b7[2], b14)
        self.b13 = self.b11 if self.b5 else self.b12
        stroke(self.b13)
        rect(self.x, self.y, self.width, self.b6)
        fill(self.b8)
        textSize(self.b9)
        b10(self.b10, self.x + 5, self.y + 25)
if b15 = = "__main__":
    b16 = class1(14)
    b16.fonk2(6)
    b16.fonk2(18)
    b16.fonk2(3)
    print(b16.fonk3(7))
    print(b16.fonk3(14))
    b16.fonk4()
