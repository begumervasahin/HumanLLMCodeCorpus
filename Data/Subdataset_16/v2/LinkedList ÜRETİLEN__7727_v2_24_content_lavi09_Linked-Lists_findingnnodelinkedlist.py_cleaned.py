class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, new_data):
        b4 = class1(new_data)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self):
        b5 = self.b3
        while b5:
            print(b5.b1)
            b5 = b5.b2
    def fonk5(self, n):
        b6 = self.b3
        b7 = self.b3
        a1 = 0
        while a1 < n:
            if b7 is None:
                print(f"The list has fewer than {n} elements.")
                return
            b7 = b7.b2
            a1 += 1
        while b7 is not None:
            b6 = b6.b2
            b7 = b7.b2
        if b6 is not None:
            print(b6.b1)
        else:
            print(f"The list has fewer than {n} elements.")
if b8 = = "__main__":
    b9 = class2()
    b9.fonk3(6)
    b9.fonk3(5)
    b9.fonk3(4)
    b9.fonk3(3)
    b9.fonk3(2)
    b9.fonk3(1)
    print("The linked list is:")
    b9.fonk4()
    print("\nThe 2nd node from the end is:")
    b9.fonk5(2)