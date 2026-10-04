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
        while b7:
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                return b7
            b7 = b7.b2
            if b7 = = self.b6:
                break
        return None
    def fonk5(self):
        b8 = self.b6
        if self.b6 is not None:
            while True:
                print(f"b3: {b8.b1.b3}, b4: {b8.b1.b4}, b5: {b8.b1.b5}")
                b8 = b8.b2
                if b8 = = self.b6:
                    break
        print("----------")
    def fonk6(self, new_student):
        b9 = class1(new_student)
        if self.b6 is None:
            self.b6 = b9
            b9.b2 = b9
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b9
            b9.b2 = self.b6
    def fonk7(self, prev_student_name, prev_student_ID, new_student):
        b9 = class1(new_student)
        b10 = self.fonk4(prev_student_name, prev_student_ID)
        if b10 is None:
            print("This student is not in the list")
            return
        b9.b2 = b10.b2
        b10.b2 = b9
    def fonk8(self, b3, b4):
        if self.b6 is None:
            return
        b7 = self.b6
        b11 = None
        while True:
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                if b11:
                    b11.b2 = b7.b2
                else:
                    b12 = self.b6
                    while b12.b2 != self.b6:
                        b12 = b12.b2
                    if self.b6 = = self.b6.b2:
                        self.b6 = None
                    else:
                        b12.b2 = self.b6.b2
                        self.b6 = self.b6.b2
                return
            b11 = b7
            b7 = b7.b2
            if b7 = = self.b6:
                break
    def fonk9(self):
        if self.b6 is None:
            return
        b11 = None
        b13 = self.b6
        b14 = None
        b15 = self.b6
        while True:
            b14 = b13.b2
            b13.b2 = b11
            b11 = b13
            b13 = b14
            if b13 = = b15:
                break
        self.b6.b2 = b11
        self.b6 = b11
    def fonk10(self, b3, b4):
        b16 = self.fonk4(b3, b4)
        if b16:
            self.b6 = b16
def fonk11():
    b17 = class3()
    b18 = class2("meri", "111", "3.0")
    b17.fonk6(b18)
    b19 = class2("john", "112", "3.5")
    b17.fonk6(b19)
    b20 = class2("doe", "113", "3.8")
    b17.fonk6(b20)
    print("Original List:")
    b17.fonk5()
    b17.fonk9()
    print("Reversed List:")
    b17.fonk5()
    b21 = class2("jane", "114", "3.7")
    b17.fonk7("john", "112", b21)
    print("After Appending Jane after John:")
    b17.fonk5()
    b17.fonk8("meri", "111")
    print("After Deleting Meri:")
    b17.fonk5()
    b17.fonk10("jane", "114")
    print("After Changing Head to Jane:")
    b17.fonk5()
if b22 = = "__main__":
    fonk11()