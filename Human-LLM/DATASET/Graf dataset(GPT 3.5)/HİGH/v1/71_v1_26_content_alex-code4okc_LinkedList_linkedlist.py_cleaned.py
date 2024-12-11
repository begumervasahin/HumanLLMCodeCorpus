class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
    def fonk2(self):
        self.b4 = self.class2(None)
        self.b5 = self.class2(None)
        self.a1 = 0
    def fonk3(self, b2):
        b6 = self.class2(b2)
        if self.b5.b1 is None:
            self.b4.b3 = b6
            self.b5.b1 = b6
            self.a1 += 1
        else:
            self.b5.b1.b3 = b6
            b6.b1 = self.b5.b1
            self.b5.b1 = b6
            self.a1 += 1
    def fonk4(self, b2):
        b6 = self.class2(b2)
        if self.fonk12():
            self.b4.b3 = b6
            self.b5.b1 = b6
            self.a1 += 1
        else:
            b7 = self.b4.b3
            self.b4.b3 = b6
            b6.b3 = b7
            b7.b1 = b6
            self.a1 += 1
    def fonk5(self):
        if self.a1 = = 0:
            return "Linked List is empty!"
        return self.b4.b3.b2
    def fonk6(self):
        if self.a1 = = 0:
            return "Linked List is empty!"
        return self.b5.b1.b2
    def fonk7(self):
        return self.a1
    def fonk8(self):
        if self.b4.b3 is None:
            return "Linked List is empty!"
        else:
            b8 = ""
            b9 = self.b4.b3
            while b9 is not None:
                b8 += str(b9.b2)
                if b9.b3 is not None:
                    b8 += ", "
                b9 = b9.b3
            return b8
    def fonk9(self, b2, b10):
        if self.fonk12():
            self.fonk3(b2)
        elif b10 = = 0:
            self.fonk4(b2)
        elif b10 = = -1:
            self.fonk3(b2)
        elif b10 = = self.fonk7():
            self.fonk3(b2)
        elif b10 < self.fonk7():
            b6 = self.class2(b2)
            a2 = 0
            b9 = self.b4.b3
            while b9.b3 is not None:
                a2 += 1
                b9 = b9.b3
                if b10 = = a2:
                    b7 = b9
                    b7.b1.b3 = b6
                    b6.b1 = b7.b1
                    b6.b3 = b7
                    b7.b1 = b6
        else:
            print("Attempted to element beyond the length of the list")
    def fonk10(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            if self.fonk7() == 1:
                self.b4.b3 = None
                self.b5.b1 = None
            else:
                b11 = self.b4.b3
                b12 = b11.b3
                self.b4.b3 = b12
                b12.b1 = None
                b11.b3 = None
                self.a1 -= 1
    def fonk11(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            if self.fonk7() == 1:
                self.b4.b3 = None
                self.b5.b1 = None
                self.a1 -= 1
            else:
                b11 = self.b5.b1
                b13 = b11.b1
                self.b5.b1 = b13
                b13.b3 = None
                b11.b1 = None
                self.a1 -= 1
    def fonk12(self):
        return self.a1 = = 0
if b14 = = "__main__":
    b15 = class1()
    b15.fonk3(1)
    b15.fonk3(2)
    b15.fonk3(3)
    b15.fonk4(0)
    print(b15)
    b15.fonk10()
    b15.fonk11()
    print(b15)
    print(b15.fonk5())
    print(b15.fonk6())
