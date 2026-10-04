
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
            print(b5.b1, b6 = ' ')
            b5 = b5.b2
        print()
    def fonk5(self, a1):
        b7 = self.b3
        b8 = self.b3
        for _ in range(a1):
            if b8 is None:
                print(f"The linked list has less than {a1} elements.")
                return
            b8 = b8.b2
        while b8:
            b7 = b7.b2
            b8 = b8.b2
        print(f"The {a1}th node from the b6 is: {b7.b1}")
if b9 = = "__main__":
    b10 = class2()
    b10.fonk3(6)
    b10.fonk3(5)
    b10.fonk3(4)
    b10.fonk3(3)
    b10.fonk3(2)
    b10.fonk3(1)
    print("Linked List elements:")
    b10.fonk4()
    a1 = 2
    b10.fonk5(a1)