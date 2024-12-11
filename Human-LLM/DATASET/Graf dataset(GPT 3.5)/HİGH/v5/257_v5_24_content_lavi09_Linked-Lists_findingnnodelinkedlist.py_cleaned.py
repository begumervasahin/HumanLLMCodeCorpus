class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, new_data):
        b4 = class1(new_data)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2
    def fonk5(self, n):
        if not self.b3:
            return None
        b6 = self.b3
        b7 = self.b3
        for _ in range(n):
            if b7 is None:
                return None
            b7 = b7.b2
        while b7:
            b6 = b6.b2
            b7 = b7.b2
        return b6.b1
b8 = class2()
b8.fonk3(6)
b8.fonk3(5)
b8.fonk3(4)
b8.fonk3(3)
b8.fonk3(2)
b8.fonk3(1)
b8.fonk4()
print("2nd node from the end:", b8.fonk5(2))