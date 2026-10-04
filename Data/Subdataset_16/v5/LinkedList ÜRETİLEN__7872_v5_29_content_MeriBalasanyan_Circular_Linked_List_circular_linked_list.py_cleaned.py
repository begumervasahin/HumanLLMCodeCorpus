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
        if self.b6 is None:
            print("List is empty.")
            return
        b7 = self.b6
        while True:
            print(f"b3: {b7.b1.b3}, b4: {b7.b1.b4}, b5: {b7.b1.b5}")
            b7 = b7.b2
            if b7 = = self.b6:
                break
        print("----------")
    def fonk6(self, new_student):
        b8 = class1(new_student)
        if self.b6 is None:
            self.b6 = b8
            b8.b2 = b8
        else:
            b7 = self.b6
            while b7.b2 != self.b6:
                b7 = b7.b2
            b7.b2 = b8
            b8.b2 = self.b6
    def fonk7(self, prev_student_name, prev_student_ID, new_student):
        b8 = class1(new_student)
        b9 = self.fonk4(prev_student_name, prev_student_ID)
        if b9 is None:
            print("This student is not in the list.")
            return
        b8.b2 = b9.b2
        b9.b2 = b8
    def fonk8(self, b3, b4):
        if self.b6 is None:
            return
        b7 = self.b6
        b10 = None
        while True:
            if b7.b1.b3 = = b3 and b7.b1.b4 == b4:
                if b10:
                    b10.b2 = b7.b2
                else:
                    b11 = self.b6
                    while b11.b2 != self.b6:
                        b11 = b11.b2
                    if self.b6 = = self.b6.b2:
                        self.b6 = None
                    else:
                        b11.b2 = self.b6.b2
                        self.b6 = self.b6.b2
                return
            b10 = b7
            b7 = b7.b2
            if b7 = = self.b6:
                break
    def fonk9(self):
        if self.b6 is None:
            return
        b10 = None
        b12 = self.b6
        b13 = self.b6
        while True:
            b14 = b12.b2
            b12.b2 = b10
            b10 = b12
            b12 = b14
            if b12 = = b13:
                break
        self.b6.b2 = b10
        self.b6 = b10
    def fonk10(self, b3, b4):
        b15 = self.fonk4(b3, b4)
        if b15:
            self.b6 = b15
def fonk11():
    b16 = class3()
    b17 = class2("meri", "111", "3.0")
    b16.fonk6(b17)
    b18 = class2("john", "112", "3.5")
    b16.fonk6(b18)
    b19 = class2("doe", "113", "3.8")
    b16.fonk6(b19)
    print("Original List:")
    b16.fonk5()
    b16.fonk9()
    print("Reversed List:")
    b16.fonk5()
    b20 = class2("jane", "114", "3.7")
    b16.fonk7("john", "112", b20)
    print("After Appending Jane after John:")
    b16.fonk5()
    b16.fonk8("meri", "111")
    print("After Deleting Meri:")
    b16.fonk5()
    b16.fonk10("jane", "114")
    print("After Changing Head to Jane:")
    b16.fonk5()
if b21 = = "__main__":
    fonk11()