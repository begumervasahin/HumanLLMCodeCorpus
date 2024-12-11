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
            print("Cannot delete from an empty list")
        elif self.b3.b1 = = b1:
            self.b3 = self.b3.b2
        else:
            b5 = None
            b6 = self.b3
            while b6 is not None and b6.b1 != b1:
                b5 = b6
                b6 = b6.b2
            if b6 is None:
                print("Data not found in the list")
            else:
                b5.b2 = b6.b2
    def fonk5(self):
        if self.b3 is None:
            print("Empty linked list")
        else:
            b6 = self.b3
            while b6:
                print(b6.b1)
                b6 = b6.b2
def fonk6():
    print("OPTIONS FOR THIS PROGRAM")
    print("1. Insert at the front")
    print("2. Delete a node")
    print("3. Print contents of the linked list")
    b7 = int(input("Enter your b7: "))
    if b7 not in [1, 2, 3]:
        print("Invalid b7! Exiting...")
        return
    b8 = class2()
    if b7 = = 1:
        b9 = int(input("Enter b1 to insert at the front: "))
        b8.fonk3(b9)
    elif b7 = = 2:
        b9 = int(input("Enter b1 to delete: "))
        b8.fonk4(b9)
    b8.fonk5()
    b10 = input("Do you want to continue (yes/no)? ").lower()
    if b10 = = 'yes':
        fonk6()
    else:
        b8.fonk5()
if b11 = = "__main__":
    fonk6()