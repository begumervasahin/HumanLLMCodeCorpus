class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, b1):
        if self.b1 is None:
            self.b1 = b1
        else:
            if b1 < self.b1:
                if self.b2 is None:
                    self.b2 = class1(b1)
                else:
                    self.b2.fonk2(b1)
            elif b1 > self.b1:
                if self.b3 is None:
                    self.b3 = class1(b1)
                else:
                    self.b3.fonk2(b1)
    def fonk3(self, lookup_value):
        if self.b1 is None:
            return str(lookup_value) + " Not Found"
        elif lookup_value < self.b1:
            if self.b2 is None:
                return str(lookup_value) + " Not Found"
            return self.b2.fonk3(lookup_value)
        elif lookup_value > self.b1:
            if self.b3 is None:
                return str(lookup_value) + " Not Found"
            return self.b3.fonk3(lookup_value)
        else:
            return str(self.b1) + " is found"
    def fonk4(self):
        if self.b2:
            self.b2.fonk4()
        print(self.b1)
        if self.b3:
            self.b3.fonk4()
b4 = class1(14)
b4.fonk2(6)
b4.fonk2(18)
b4.fonk2(3)
print(b4.fonk3(7))
print(b4.fonk3(14))
b4.fonk4()