class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"class1: {self.b1} --({self.b3})--> {self.b2}"
b4 = [
    class1('a', 'b', 5),
    class1('b', 'c', 7),
    class1('c', 'd', 3)
]
for edge in b4:
    print(edge)