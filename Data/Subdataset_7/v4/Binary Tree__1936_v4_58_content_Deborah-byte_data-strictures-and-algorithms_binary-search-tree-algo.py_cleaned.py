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
    def fonk3(self, lookup_value):
        if lookup_value < self.b3:
            if self.b1 is None:
                return str(lookup_value) + " Not Found"
            return self.b1.fonk3(lookup_value)
        elif lookup_value > self.b3:
            if self.b2 is None:
                return str(lookup_value) + " Not Found"
            return self.b2.fonk3(lookup_value)
        else:
            return str(self.b3) + " is found"
    def fonk4(self):
        if self.b1:
            self.b1.fonk4()
        print(self.b3, b4 = ' ')
        if self.b2:
            self.b2.fonk4()
b5 = class1(14)
b5.fonk2(6)
b5.fonk2(18)
b5.fonk2(3)
print(b5.fonk3(7))
print(b5.fonk3(14))
b5.fonk4()