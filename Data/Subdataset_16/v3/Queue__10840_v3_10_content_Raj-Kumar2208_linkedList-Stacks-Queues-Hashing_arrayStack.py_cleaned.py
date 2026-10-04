
class class1:
    def fonk1(self, b1 = 10):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, data):
        if self.fonk6() >= self.b1:
            raise ValueError("Stack Overflow")
        self.b2.append(data)
        print(f"Stack After Push: {self.b2}")
    def fonk3(self):
        return len(self.b2) == 0
    def fonk4(self):
        if self.fonk3():
            raise ValueError("Stack Underflow")
        return self.b2.fonk4()
    def fonk5(self):
        if self.fonk3():
            raise ValueError("Stack Underflow")
        return self.b2[-1]
    def fonk6(self):
        return len(self.b2)
    def fonk7(self):
        print(self.b2)
if b3 = = "__main__":
    b2 = class1(5)
    print(f"Is b2 empty? {b2.fonk3()}")
    b2.fonk2(5)
    b2.fonk2(6)
    b2.fonk2(7)
    print(f"Top element is: {b2.fonk5()}")
    b2.fonk4()
    b2.fonk7()