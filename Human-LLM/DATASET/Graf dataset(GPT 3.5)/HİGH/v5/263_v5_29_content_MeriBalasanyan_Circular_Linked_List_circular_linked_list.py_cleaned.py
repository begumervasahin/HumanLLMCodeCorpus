class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
class class3:
    def fonk3(self):
        self.b6 = None
    def fonk4(self, b3, b4):
        b7 = self.b6
        while b7 is not None and (b7.b1.b3 != b3 or b7.b1.b4 != b4):
            b7 = b7.b2
            if b7 = = self.b6:
                return None
        return b7
    def fonk5(self):
        b7 = self.b6
        while True:
            print(f"Name: {b7.b1.b3}, b4: {b7.b1.b4}, b5: {b7.b1.b5}")
            b7 = b7.b2
            if b7 = = self.b6:
                break
        print("----------")
    def fonk6(self, new_student):
        b8 = class1(new_student)
        if self.b6 is None:
            b8.b2 = b8
            self.b6 = b8
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b8
            b8.b2 = self.b6
    def fonk7(self, prev_name, prev_ID, new_student):
        b9 = self.fonk4(prev_name, prev_ID)
        if b9 is None:
            print("Previous student not found in the list")
            return
        b8 = class1(new_student)
        b8.b2 = b9.b2
        b9.b2 = b8
    def fonk8(self, b3, b4):
        b7 = self.b6
        b10 = None
        while b7 is not None and (b7.b1.b3 != b3 or b7.b1.b4 != b4):
            b10 = b7
            b7 = b7.b2
            if b7 = = self.b6:
                break
        if b7 is None:
            print("class2 not found in the list")
            return
        if b10 is not None:
            b10.b2 = b7.b2
        else:
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = self.b6.b2
            self.b6 = self.b6.b2
    def fonk9(self):
        if self.b6 is None:
            return
        b10 = None
        b7 = self.b6
        while True:
            b11 = b7.b2
            b7.b2 = b10
            b10 = b7
            b7 = b11
            if b7 = = self.b6:
                break
        self.b6 = b10
    def fonk10(self, b3, b4):
        b12 = self.fonk4(b3, b4)
        if b12 is None:
            print("class2 not found in the list")
            return
        self.b6 = b12
def fonk11():
    b13 = class3()
    b14 = class2("Meri", "111", "3.0")
    b15 = class2("John", "222", "3.5")
    b13.fonk6(b14)
    b13.fonk6(b15)
    b13.fonk9()
    b13.fonk7("Meri", "111", class2("Alice", "333", "4.0"))
    b13.fonk8("John", "222")
    b13.fonk10("Alice", "333")
    b13.fonk9()
    b13.fonk5()
if b16 = = "__main__":
    fonk11()