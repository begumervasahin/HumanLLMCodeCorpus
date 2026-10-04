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
        b6 = self.class2(b2)
        b7 = self.b5.b1
        b7.b3 = b6
        b6.b1 = b7
        b6.b3 = self.b5
        self.b5.b1 = b6
        self.a1 += 1
    def fonk4(self, b2):
        b6 = self.class2(b2)
        b8 = self.b4.b3
        self.b4.b3 = b6
        b6.b1 = self.b4
        b6.b3 = b8
        b8.b1 = b6
        self.a1 += 1
    def fonk5(self):
        if self.fonk12():
            return "Linked List is empty!"
        return self.b4.b3.b2
    def fonk6(self):
        if self.fonk12():
            return "Linked List is empty!"
        return self.b5.b1.b2
    def fonk7(self):
        return self.a1
    def fonk8(self):
        if self.fonk12():
            return "Linked List is empty!"
        else:
            b9 = []
            b10 = self.b4.b3
            while b10 != self.b5:
                b9.append(str(b10.b2))
                b10 = b10.b3
            return ", ".join(b9)
    def fonk9(self, b2, b11):
        if self.fonk12():
            self.fonk3(b2)
        elif b11 = = 0:
            self.fonk4(b2)
        elif b11 = = -1 or b11 == self.a1:
            self.fonk3(b2)
        elif b11 < self.a1:
            b6 = self.class2(b2)
            b10 = self.b4.b3
            for _ in range(b11):
                b10 = b10.b3
            b1 = b10.b1
            b1.b3 = b6
            b6.b1 = b1
            b6.b3 = b10
            b10.b1 = b6
            self.a1 += 1
        else:
            print("Attempted to insert element beyond the length of the list")
    def fonk10(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            b8 = self.b4.b3
            b12 = b8.b3
            self.b4.b3 = b12
            b12.b1 = self.b4
            b8.b3 = None
            b8.b1 = None
            self.a1 -= 1
    def fonk11(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            b7 = self.b5.b1
            b13 = b7.b1
            self.b5.b1 = b13
            b13.b3 = self.b5
            b7.b3 = None
            b7.b1 = None
            self.a1 -= 1
    def fonk12(self):
        return self.a1 = = 0
if b14 = = "__main__":
    b15 = class1()
    b15.fonk3(1)
    b15.fonk3(2)
    b15.fonk4(0)
    print(b15)
    b15.fonk9(1.5, 2)
    print(b15)
    b15.fonk10()
    print(b15)
    b15.fonk11()
    print(b15)
