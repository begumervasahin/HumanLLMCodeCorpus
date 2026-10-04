class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.a1 = 0
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
        self.a1 += 1
    def fonk4(self, b1):
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = b4
        self.a1 += 1
    def fonk5(self):
        return self.a1
    def fonk6(self):
        b5 = self.b3
        a2 = 0
        while b5:
            a2 += 1
            b5 = b5.b2
        return a2
    def fonk7(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2
    def fonk8(self, b1):
        if not self.b3:
            print('List is empty')
            return
        b5 = self.b3
        b6 = None
        while b5:
            if b5.b1 = = b1:
                if b6:
                    b6.b2 = b5.b2
                else:
                    self.b3 = b5.b2
                self.a1 -= 1
                return
            b6 = b5
            b5 = b5.b2
        print(f"Data {b1} not found in the list")
def fonk9():
    b7 = class2()
    b7.fonk3(10)
    b7.fonk3(35)
    b7.fonk3(67)
    b7.fonk3(89)
    b7.fonk3(341)
    print("Initial a1 of the list:", b7.fonk5())
    print("Calculated a1 of the list:", b7.fonk6())
    b7.fonk4(671)
    print("Size of the list after inserting at the end:", b7.fonk6())
    print("Traversing the list:")
    b7.fonk7()
    b7.fonk8(20)
    print("Size of the list after attempting to remove 20:", b7.fonk6())
    print("Traversing the list after removal attempt:")
    b7.fonk7()
if b8 = = "__main__":
    fonk9()