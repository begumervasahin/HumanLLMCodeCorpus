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
    def fonk5(self, a2):
        b6 = self.b3
        b5 = self.b3
        a1 = 0
        if self.b3:
            while a1 < a2:
                if b6 is None:
                    return
                b6 = b6.b2
                a1 += 1
        while b6 is not None:
            b5 = b5.b2
            b6 = b6.b2
        print(f"{a2}th node from the end: {b5.b1}")
if b7 = = "__main__":
    b8 = class2()
    for i in range(1, 7):
        b8.fonk3(i)
    print("class2:")
    b8.fonk4()
    a2 = 2
    print(f"Data of {a2}th node from the end:")
    b8.fonk5(a2)