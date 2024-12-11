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
        b6 = class1(b1)
        if b7 = = 0:
            self.fonk4(b1)
        else:
            b8 = self.b4
            a1 = 0
            while b8 is not None and a1 != b7 - 1:
                a1 += 1
                b8 = b8.b2
            if b8 is None and b7 > a1:
                print("INVALID POSITION")
            else:
                b6.b3 = b8
                b6.b2 = b8.b2
                b8.b2.b3 = b6
                b8.b2 = b6
    def fonk6(self):
        b8 = self.b4
        print("\nDoubly Linked List:")
        if b8 is None:
            print("Empty!!!")
        while b8 is not None:
            print("<=>", b8.b1, b9 = " ")
            b8 = b8.b2
    def fonk7(self):
        b8 = self.b5
        print("\nDoubly Linked List in Reverse:")
        if b8 is None:
            print("Empty!!!")
        while b8 is not None:
            print("<=>", b8.b1, b9 = " ")
            b8 = b8.b3
    def fonk8(self):
        if self.b4 is None:
            print("List is Empty")
        else:
            self.b4 = self.b4.b2
            if self.b4:
                self.b4.b3 = None
            else:
                self.b5 = None
    def fonk9(self):
        if self.b4 is None:
            print("List is Empty")
        else:
            self.b5 = self.b5.b3
            if self.b5:
                self.b5.b2 = None
            else:
                self.b4 = None
    def fonk10(self, b7):
        if self.b4 is None:
            print("List is Empty")
        elif b7 = = 0:
            self.fonk8()
        else:
            b8 = self.b4
            a1 = 0
            while b8 is not None and b7 != a1:
                a1 += 1
                b8 = b8.b2
            if b8 is None and b7 >= a1:
                print("Invalid Position")
            elif b8.b2.b2 is None and a1 = = b7 - 1:
                b8.b2 = None
                self.b5 = b8
            else:
                b8.b2.b2.b3 = b8
                b8.b2 = b8.b2.b2
def fonk11():
    b10 = class2()
    b11 = 'y'
    while b11 = = 'y':
        print('''1. Insertion
2. Insert at beginning
3. Insert at b9
4. Insert at position
5. Display list
6. Display in reverse order
7. Delete from beginning
8. Delete from b9
9. Delete from position
10. EXIT''')
        b12 = int(input("Enter b12: "))
        if b12 = = 1:
            b1 = int(input("Enter b1: "))
            b10.fonk3(b1)
        elif b12 = = 2:
            b1 = int(input("Enter b1: "))
            b10.fonk4(b1)
        elif b12 = = 3:
            b1 = int(input("Enter b1: "))
            b10.fonk3(b1)
        elif b12 = = 4:
            b7 = int(input("Enter position (0 ......n): "))
            b1 = int(input("Enter b1: "))
            b10.fonk5(b7, b1)
        elif b12 = = 5:
            b10.fonk6()
        elif b12 = = 6:
            b10.fonk7()
        elif b12 = = 7:
            b10.fonk8()
        elif b12 = = 8:
            b10.fonk9()
        elif b12 = = 9:
            b7 = int(input("Enter position (0 ......n): "))
            b10.fonk10(b7)
        else:
            break
        b11 = input("\nEnter 'y' to continue: ")
if b13 = = "__main__":
    fonk11()