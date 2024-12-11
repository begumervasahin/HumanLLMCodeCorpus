class class1:
    def fonk1(self, b1 = 10):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, data):
        if len(self.b2) >= self.b1:
            raise ValueError("Stack Overflow")
        self.b2.append(data)
        print("Stack After Push:", self.b2)
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
    b4 = class1(5)
    print("Is the stack empty?", b4.fonk3())
    b4.fonk2(5)
    b4.fonk2(6)
    b4.fonk2(7)
    print("Top element of the stack:", b4.fonk5())
    b4.fonk4()
    b4.fonk7()