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
        if not self.b4:
            self.b4 = self.b5 = b6
        else:
            self.b5.b2 = b6
            b6.b3 = self.b5
            self.b5 = b6
    def fonk4(self, b1):
        b6 = class1(b1)
        if not self.b4:
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
        for _ in range(b7 - 1):
            if b8 is None:
                print("INVALID POSITION")
                return
            b8 = b8.b2
        if b8 is None:
            print("INVALID POSITION")
            return
        b6.b2 = b8.b2
        if b8.b2:
            b8.b2.b3 = b6
        b8.b2 = b6
        b6.b3 = b8
    def fonk6(self):
        b8 = self.b4
        print("\nDoubly Linked List:")
        if not b8:
            print("Empty!!!")
            return
        while b8:
            print("<=>", b8.b1, b9 = " ")
            b8 = b8.b2
    def fonk7(self):
        b8 = self.b5
        print("\nDoubly Linked List in Reverse:")
        if not b8:
            print("Empty!!!")
            return
        while b8:
            print("<=>", b8.b1, b9 = " ")
            b8 = b8.b3
    def fonk8(self):
        if not self.b4:
            print("List is Empty")
            return
        self.b4 = self.b4.b2
        if self.b4:
            self.b4.b3 = None
        else:
            self.b5 = None
    def fonk9(self):
        if not self.b4:
            print("List is Empty")
            return
        self.b5 = self.b5.b3
        if self.b5:
            self.b5.b2 = None
        else:
            self.b4 = None
    def fonk10(self, b7):
        if not self.b4:
            print("List is Empty")
            return
        if b7 = = 0:
            self.fonk8()
            return
        b8 = self.b4
        for _ in range(b7):
            if b8 is None:
                print("Invalid Position")
                return
            b8 = b8.b2
        if b8 is None:
            print("Invalid Position")
            return
        if b8.b2 is None:
            b8.b3.b2 = None
            self.b5 = b8.b3
        else:
            b8.b3.b2 = b8.b2
            b8.b2.b3 = b8.b3
def fonk11():
    b10 = class2()
    while True:
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
        b11 = int(input("Enter b11: "))
        if b11 = = 1:
            b1 = int(input("Enter b1: "))
            b10.fonk3(b1)
        elif b11 = = 2:
            b1 = int(input("Enter b1: "))
            b10.fonk4(b1)
        elif b11 = = 3:
            b1 = int(input("Enter b1: "))
            b10.fonk3(b1)
        elif b11 = = 4:
            b7 = int(input("Enter position (0 ......n): "))
            b1 = int(input("Enter b1: "))
            b10.fonk5(b7, b1)
        elif b11 = = 5:
            b10.fonk6()
        elif b11 = = 6:
            b10.fonk7()
        elif b11 = = 7:
            b10.fonk8()
        elif b11 = = 8:
            b10.fonk9()
        elif b11 = = 9:
            b7 = int(input("Enter position (0 ......n): "))
            b10.fonk10(b7)
        else:
            break
        b12 = input("\nEnter 'y' to continue: ")
if b13 = = "__main__":
    fonk11()