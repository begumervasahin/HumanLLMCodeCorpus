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
            print(b5.b1, b6 = " -> " if b5.b2 else "\n")
            b5 = b5.b2
    def fonk5(self, n):
        b7 = self.b3
        b8 = self.b3
        a1 = 0
        while a1 < n:
            if b8 is None:
                print(f"The list has fewer than {n} elements.")
                return
            b8 = b8.b2
            a1 += 1
        while b8:
            b7 = b7.b2
            b8 = b8.b2
        if b7:
            print(b7.b1)
        else:
            print(f"The list has fewer than {n} elements.")
if b9 = = "__main__":
    b10 = class2()
    for i in range(6, 0, -1):
        b10.fonk3(i)
    print("The linked list is:")
    b10.fonk4()
    print("\nThe 2nd node from the b6 is:")
    b10.fonk5(2)