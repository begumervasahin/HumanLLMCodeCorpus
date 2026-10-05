class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
        else:
            b4.b2 = self.b3
            self.b3 = b4
    def fonk4(self, b1):
        if self.b3 is None:
            print("You are trying to delete from an empty list")
        elif self.b3.b1 = = b1:
            self.b3 = self.b3.b2
        else:
            b5 = self.b3
            b6 = self.b3
            while b5.b2 is not None and b5.b1 != b1:
                b6 = b5
                b5 = b5.b2
            if b5.b1 != b1 and b5.b2 is None:
                print("The b1 you want to delete is not in the list")
            b6.b2 = b5.b2
            b5 = None
    def fonk5(self):
        if self.b3 is None:
            print("Empty linked list")
        else:
            b7 = self.b3
            while b7:
                print(b7.b1)
                b7 = b7.b2
b8 = class2()
def fonk6():
    print("OPTIONS FOR THIS PROGRAM")
    print("1. To insert at front")
    print("2. Delete a particular node")
    print("3. Print contents of the linked list")
    b9 = int(input("Enter now: "))
    if b9 > 4:
        print("Wrong input! Exiting..........")
    else:
        fonk7(b9)
def fonk7(b9):
    if b9 = = 1:
        b10 = int(input("Enter b1 to add in front: "))
        b8.fonk3(b10)
        b8.fonk5()
    elif b9 = = 2:
        b10 = int(input("Enter b1 to delete: "))
        b8.fonk4(b10)
        b8.fonk5()
    elif b9 = = 3:
        b8.fonk5()
    b11 = int(input("Want to enter again? Then print 1 or 0: "))
    if b11 = = 1:
        fonk6()
    else:
        b8.fonk5()
if b12 = = "__main__":
    fonk6()