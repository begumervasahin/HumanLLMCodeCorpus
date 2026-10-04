class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b1):
        b4 = class1(b1)
        self.b5 = b4
        self.b6 = b4
    def fonk3(self, b1):
        b7 = class1(b1)
        self.b6.b2 = b7
        b7.b3 = self.b6
        self.b6 = b7
    def fonk4(self, target_value, new_value):
        b8 = self.b5
        while b8 and b8.b1 != target_value:
            b8 = b8.b2
        if not b8:
            print(f"Value {target_value} not found in the list.")
            return
        b7 = class1(new_value)
        b7.b2 = b8.b2
        b7.b3 = b8
        b8.b2 = b7
        if b7.b2:
            b7.b2.b3 = b7
        else:
            self.b6 = b7
    def fonk5(self, b1):
        b8 = self.b5
        while b8 and b8.b1 != b1:
            b8 = b8.b2
        if not b8:
            print(f"Value {b1} not found in the list.")
            return
        if b8.b3:
            b8.b3.b2 = b8.b2
        else:
            self.b5 = b8.b2
        if b8.b2:
            b8.b2.b3 = b8.b3
        else:
            self.b6 = b8.b3
    def fonk6(self):
        b8 = self.b6
        while b8:
            print(b8.b1, b9 = " ")
            b8 = b8.b3
        print()
    def fonk7(self):
        b8 = self.b5
        while b8:
            print(b8.b1, b9 = " ")
            b8 = b8.b2
        print()
if b10 = = "__main__":
    b11 = class2(10)
    b11.fonk3(20)
    b11.fonk3(30)
    b11.fonk3(40)
    b11.fonk5(40)
    print("Forward traversal:")
    b11.fonk7()
    print("Reverse traversal:")
    b11.fonk6()