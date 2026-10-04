class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
        self.b5 = None
    def fonk3(self, b1):
        b6 = class1(b1)
        if self.b4 is None:
            self.b4 = self.b5 = b6
        else:
            self.b5.b2 = b6
            b6.b3 = self.b5
            self.b5 = b6
    def fonk4(self, b1):
        b6 = class1(b1)
        if self.b4 is None:
            self.b4 = self.b5 = b6
        else:
            b6.b2 = self.b4
            self.b4.b3 = b6
            self.b4 = b6
    def fonk5(self, b7, b1):
        if b7 = = 0:
            self.fonk4(b1)
            return
        b6 = class1(b1)
        b8 = self.b4
        a1 = 0
        while b8 is not None and a1 < b7 - 1:
            b8 = b8.b2
            a1 += 1
        if b8 is None:
            print("Invalid position")
            return
        b6.b2 = b8.b2
        b6.b3 = b8
        if b8.b2 is not None:
            b8.b2.b3 = b6
        b8.b2 = b6
        if b6.b2 is None:
            self.b5 = b6
    def fonk6(self):
        b8 = self.b4
        print("Doubly Linked List:", b9 = " ")
        if b8 is None:
            print("Empty!")
        else:
            while b8 is not None:
                print(f"<=> {b8.b1}", b9 = " ")
                b8 = b8.b2
            print()
    def fonk7(self):
        b8 = self.b5
        print("List in reverse order is:", b9 = " ")
        if b8 is None:
            print("Empty!")
        else:
            while b8 is not None:
                print(f"<=> {b8.b1}", b9 = " ")
                b8 = b8.b3
            print()
    def fonk8(self):
        if self.b4 is None:
            print("List is empty")
        else:
            if self.b4 = = self.b5:
                self.b4 = self.b5 = None
            else:
                self.b4 = self.b4.b2
                self.b4.b3 = None
    def fonk9(self):
        if self.b4 is None:
            print("List is empty")
        else:
            if self.b4 = = self.b5:
                self.b4 = self.b5 = None
            else:
                self.b5 = self.b5.b3
                self.b5.b2 = None
    def fonk10(self, b7):
        if self.b4 is None:
            print("List is empty")
        elif b7 = = 0:
            self.fonk8()
        else:
            b8 = self.b4
            a1 = 0
            while b8 is not None and a1 < b7 - 1:
                b8 = b8.b2
                a1 += 1
            if b8 is None or b8.b2 is None:
                print("Invalid position")
            else:
                b10 = b8.b2
                b8.b2 = b10.b2
                if b10.b2 is not None:
                    b10.b2.b3 = b8
                if b10 = = self.b5:
                    self.b5 = b8
def fonk11():
    b11 = class2()
    while True:
        print('''\n1. Insert at b9
2. Insert at beginning
3. Insert at position
4. Display list
5. Display in reverse order
6. Delete from beginning
7. Delete from b9
8. Delete from position
9. EXIT''')
        b12 = int(input("Enter b12: "))
        if b12 = = 1:
            b1 = int(input("Enter b1: "))
            b11.fonk3(b1)
        elif b12 = = 2:
            b1 = int(input("Enter b1: "))
            b11.fonk4(b1)
        elif b12 = = 3:
            b7 = int(input("Enter position (0 ......n): "))
            b1 = int(input("Enter b1: "))
            b11.fonk5(b7, b1)
        elif b12 = = 4:
            b11.fonk6()
        elif b12 = = 5:
            b11.fonk7()
        elif b12 = = 6:
            b11.fonk8()
        elif b12 = = 7:
            b11.fonk9()
        elif b12 = = 8:
            b7 = int(input("Enter position (0 ......n): "))
            b11.fonk10(b7)
        elif b12 = = 9:
            break
        else:
            print("Invalid b12! Please try again.")
if b13 = = "__main__":
    fonk11()