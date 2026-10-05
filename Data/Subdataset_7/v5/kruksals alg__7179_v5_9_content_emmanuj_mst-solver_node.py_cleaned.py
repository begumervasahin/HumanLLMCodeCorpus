class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        b3 = self.b2.b1 if self.b2 else None
        return f"class1(b1 = {self.b1}, a1={self.a1}, b2={b3})"