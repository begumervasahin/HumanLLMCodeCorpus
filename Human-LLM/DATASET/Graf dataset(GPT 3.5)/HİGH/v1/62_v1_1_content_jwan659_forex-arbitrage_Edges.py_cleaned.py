class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return self.b3
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self):
        return self.b1
    def fonk5(self, b1):
        self.b1 = b1
    def fonk6(self):
        return self.b2
    def fonk7(self, b2):
        self.b2 = b2
if b4 = = "__main__":
    b5 = class1('A', 'B', 10)
    b6 = class1('B', 'C', 5)
    print("Start vertex of b5:", b5.fonk4())
    print("Target vertex of b5:", b5.fonk6())
    print("Weight of b5:", b5.fonk2())
    b5.fonk3(15)
    print("Updated b3 of b5:", b5.fonk2())
    b5.fonk5('X')
    print("Updated b1 vertex of b5:", b5.fonk4())
    b5.fonk7('Y')
    print("Updated b2 vertex of b5:", b5.fonk6())