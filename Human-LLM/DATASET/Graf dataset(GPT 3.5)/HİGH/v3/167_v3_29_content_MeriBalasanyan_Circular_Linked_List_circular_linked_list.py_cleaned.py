class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3: str, b4: str, b5: str):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
class class3:
    def fonk3(self):
        self.b6 = None
    def fonk4(self, b3: str, b4: str) -> class1 or None:
        b7 = self.b6
        while b7 and (b7.b1.b3 != b3 or b7.b1.b4 != b4):
            b7 = b7.b2
            if b7 = = self.b6:
                return None
        return b7
    def fonk5(self) -> None:
        if not self.b6:
            print("List is empty")
            return
        b7 = self.b6
        while True:
            print(f"Name: {b7.b1.b3}, b4: {b7.b1.b4}, b5: {b7.b1.b5}")
            b7 = b7.b2
            if b7 = = self.b6:
                break
        print("----------")
    def fonk6(self, new_student: class2) -> None:
        b8 = class1(new_student)
        if not self.b6:
            b8.b2 = b8
            self.b6 = b8
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b8
            b8.b2 = self.b6
    def fonk7(self) -> None:
        if not self.b6:
            print("List is empty")
            return
        b9 = None
        b7 = self.b6
        while b7.b2 != self.b6:
            b10 = b7.b2
            b7.b2 = b9
            b9 = b7
            b7 = b10
        b7.b2 = b9
        self.b6.b2 = b7
        self.b6 = b7
def fonk8():
    b11 = class3()
    b12 = class2("Meri", "111", "3.0")
    b11.fonk6(b12)
    b11.fonk5()
    b11.fonk7()
    b11.fonk5()
if b13 = = "__main__":
    fonk8()