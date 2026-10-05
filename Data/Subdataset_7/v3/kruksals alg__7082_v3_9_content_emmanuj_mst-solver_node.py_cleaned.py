class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self
        self.a1 = 0
    def fonk2(self):
        return f"class1(b1 = {self.b1}, a1={self.a1}, b2={self.b2.b1})"
b3 = [
    class1('A'),
    class1('B'),
    class1('C')
]
for node in b3:
    print(node)