class class1:
    def fonk1(self, b6, b7, a1):
        self.b1 = b6
        self.b2 = b7
        self.b3 = a1
    @property
    def fonk2(self):
        return self.b3
    @a1.setter
    def fonk3(self, value):
        self.b3 = value
    @property
    def fonk4(self):
        return self.b1
    @b6.setter
    def fonk5(self, value):
        self.b1 = value
    @property
    def fonk6(self):
        return self.b2
    @b7.setter
    def fonk7(self, value):
        self.b2 = value
if b4 = = "__main__":
    b5 = class1("A", "B", 5)
    print(f"Start: {b5.b6}")
    print(f"Target: {b5.b7}")
    print(f"Weight: {b5.a1}")
    b5.b6 = "C"
    b5.b7 = "D"
    b5.a1 = 10
    print(f"Updated Start: {b5.b6}")
    print(f"Updated Target: {b5.b7}")
    print(f"Updated Weight: {b5.a1}")
