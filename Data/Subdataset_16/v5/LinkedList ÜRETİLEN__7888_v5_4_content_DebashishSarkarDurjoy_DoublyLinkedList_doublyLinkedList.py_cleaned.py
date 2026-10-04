class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, val):
        self.b4 = class1(val)
        self.b5 = self.b4
    def fonk3(self, val):
        b6 = class1(val)
        self.b5.b2 = b6
        b6.b3 = self.b5
        self.b5 = b6
    def fonk4(self, val, new_val):
        b7 = self.b4
        while b7 and b7.b1 != val:
            b7 = b7.b2
        if not b7:
            print(f"Value {val} not found in the list.")
            return
        b6 = class1(new_val)
        b6.b2 = b7.b2
        b6.b3 = b7
        if b7.b2:
            b7.b2.b3 = b6
        b7.b2 = b6
        if b7 = = self.b5:
            self.b5 = b6
    def fonk5(self, val):
        b7 = self.b4
        while b7 and b7.b1 != val:
            b7 = b7.b2
        if not b7:
            print(f"Value {val} not found in the list.")
            return
        if b7.b3:
            b7.b3.b2 = b7.b2
        if b7.b2:
            b7.b2.b3 = b7.b3
        if b7 = = self.b4:
            self.b4 = b7.b2
        if b7 = = self.b5:
            self.b5 = b7.b3
    def fonk6(self):
        b7 = self.b5
        b8 = []
        while b7:
            b8.append(b7.b1)
            b7 = b7.b3
        print(" <- ".join(map(str, b8)))
    def fonk7(self):
        b7 = self.b4
        b8 = []
        while b7:
            b8.append(b7.b1)
            b7 = b7.b2
        print(" -> ".join(map(str, b8)))
if b9 = = "__main__":
    b10 = class2(10)
    b10.fonk3(20)
    b10.fonk3(30)
    b10.fonk3(40)
    b10.fonk5(40)
    print("List in order:")
    b10.fonk7()
    print("List in reverse order:")
    b10.fonk6()