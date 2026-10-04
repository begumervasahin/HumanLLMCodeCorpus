class class1:
    class class2:
        def fonk1(self, b2, b1 = None, b3=None):
            self.b2 = b2
            self.b1 = b1
            self.b3 = b3
    def fonk2(self):
        self.b4 = self.class2(None)
        self.b5 = self.class2(None)
        self.b4.b3 = self.b5
        self.b5.b1 = self.b4
        self.a1 = 0
    def fonk3(self, b2):
        b6 = self.class2(b2, b1=self.b5.b1, b3=self.b5)
        self.b5.b1.b3 = b6
        self.b5.b1 = b6
        self.a1 += 1
    def fonk4(self, b2):
        b6 = self.class2(b2, b3=self.b4.b3, b1=self.b4)
        self.b4.b3.b1 = b6
        self.b4.b3 = b6
        self.a1 += 1
    def fonk5(self):
        return self.b4.b3.b2 if not self.fonk12() else "Linked List is empty!"
    def fonk6(self):
        return self.b5.b1.b2 if not self.fonk12() else "Linked List is empty!"
    def fonk7(self):
        return self.a1
    def fonk8(self):
        if self.fonk12():
            return "Linked List is empty!"
        else:
            b7 = []
            b8 = self.b4.b3
            while b8 != self.b5:
                b7.append(str(b8.b2))
                b8 = b8.b3
            return ", ".join(b7)
    def fonk9(self, b2, b9):
        if b9 < 0 or b9 > self.a1:
            print("Attempted to insert element beyond the length of the list")
            return
        if b9 = = 0:
            self.fonk4(b2)
        elif b9 = = self.a1:
            self.fonk3(b2)
        else:
            b8 = self.b4.b3
            for _ in range(b9):
                b8 = b8.b3
            b6 = self.class2(b2, b1=b8.b1, b3=b8)
            b8.b1.b3 = b6
            b8.b1 = b6
            self.a1 += 1
    def fonk10(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            b10 = self.b4.b3
            self.b4.b3 = b10.b3
            b10.b3.b1 = self.b4
            self.a1 -= 1
    def fonk11(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            b11 = self.b5.b1
            self.b5.b1 = b11.b1
            b11.b1.b3 = self.b5
            self.a1 -= 1
    def fonk12(self):
        return self.a1 = = 0
if b12 = = "__main__":
    b13 = class1()
    b13.fonk4(1)
    b13.fonk3(2)
    b13.fonk3(3)
    b13.fonk9(4, 2)
    print(b13)
    b13.fonk10()
    print(b13)
    b13.fonk11()
    print(b13)
    print("First b2:", b13.fonk5())
    print("Last b2:", b13.fonk6())
    print("List a1:", b13.fonk7())
