
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        return (
            f"class1(b1: {self.b1}, "
            f"a1: {self.a1}, "
            f"b2: {self.b2.b1})"
        )