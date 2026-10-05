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
        if self.fonk12():
            self.b4.b3 = b6
            self.b5.b1 = b6
        else:
            b6.b1 = self.b5.b1
            self.b5.b1.b3 = b6
            self.b5.b1 = b6
        self.a1 += 1
    def fonk4(self, b2):
        b6 = self.class2(b2)
        if self.fonk12():
            self.b4.b3 = b6
            self.b5.b1 = b6
        else:
            b6.b3 = self.b4.b3
            self.b4.b3.b1 = b6
            self.b4.b3 = b6
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
            b7 = self.b4.b3
            b8 = []
            while b7:
                b8.append(str(b7.b2))
                b7 = b7.b3
            return ", ".join(b8)
    def fonk9(self, b2, a2):
        if a2 < 0:
            a2 = 0
        if a2 >= self.a1:
            self.fonk3(b2)
        elif a2 = = 0:
            self.fonk4(b2)
        else:
            b6 = self.class2(b2)
            b7 = self.b4.b3
            for _ in range(a2):
                b7 = b7.b3
            b6.b1 = b7.b1
            b6.b3 = b7
            b7.b1.b3 = b6
            b7.b1 = b6
            self.a1 += 1
    def fonk10(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            self.b4.b3 = self.b4.b3.b3
            if self.b4.b3:
                self.b4.b3.b1 = None
            else:
                self.b5.b1 = None
            self.a1 -= 1
    def fonk11(self):
        if self.fonk12():
            print("List is empty! No elements to remove.")
        else:
            self.b5.b1 = self.b5.b1.b1
            if self.b5.b1:
                self.b5.b1.b3 = None
            else:
                self.b4.b3 = None
            self.a1 -= 1
    def fonk12(self):
        return self.a1 = = 0
if b9 = = "__main__":
    b10 = class1()
    b10.fonk3(1)
    b10.fonk3(2)
    b10.fonk3(3)
    b10.fonk4(0)
    print(b10)
    b10.fonk10()
    b10.fonk11()
    print(b10)
    print(b10.fonk5())
    print(b10.fonk6())
