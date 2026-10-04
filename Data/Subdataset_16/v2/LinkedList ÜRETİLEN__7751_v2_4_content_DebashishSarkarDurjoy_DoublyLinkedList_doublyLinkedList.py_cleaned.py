class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b1):
        self.b4 = class1(b1)
        self.b5 = self.b4
    def fonk3(self, b1):
        b6 = class1(b1)
        self.b5.b2 = b6
        b6.b3 = self.b5
        self.b5 = b6
    def fonk4(self, target_value, new_value):
        b6 = class1(new_value)
        b7 = self.b4
        while b7 and b7.b1 != target_value:
            b7 = b7.b2
        if not b7:
            print(f"Value {target_value} not found in the list.")
            return
        b6.b2 = b7.b2
        if b6.b2:
            b6.b2.b3 = b6
        b7.b2 = b6
        b6.b3 = b7
        if b7 = = self.b5:
            self.b5 = b6
    def fonk5(self, b1):
        b7 = self.b4
        while b7 and b7.b1 != b1:
            b7 = b7.b2
        if not b7:
            print(f"Value {b1} not found in the list.")
            return
        if b7.b3:
            b7.b3.b2 = b7.b2
        else:
            self.b4 = b7.b2
        if b7.b2:
            b7.b2.b3 = b7.b3
        else:
            self.b5 = b7.b3
    def fonk6(self):
        b7 = self.b5
        while b7:
            print(b7.b1, b8 = " ")
            b7 = b7.b3
        print()
    def fonk7(self):
        b7 = self.b4
        while b7:
            print(b7.b1, b8 = " ")
            b7 = b7.b2
        print()
if b9 = = "__main__":
    b10 = class2(10)
    b10.fonk3(20)
    b10.fonk3(30)
    b10.fonk3(40)
    b10.fonk5(40)
    print("Forward traversal:")
    b10.fonk7()
    print("Reverse traversal:")
    b10.fonk6()