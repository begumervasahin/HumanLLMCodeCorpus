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
            print("The list is empty.")
        elif self.b3.b1 = = b1:
            self.b3 = self.b3.b2
        else:
            b5 = self.b3
            b6 = None
            while b5 and b5.b1 != b1:
                b6 = b5
                b5 = b5.b2
            if b5 is None:
                print("The b1 you want to delete is not in the list.")
            else:
                b6.b2 = b5.b2
                del b5
    def fonk5(self):
        if self.b3 is None:
            print("The list is empty.")
        else:
            b5 = self.b3
            while b5:
                print(b5.b1)
                b5 = b5.b2
def fonk6():
    b7 = class2()
    while True:
        print("OPTIONS FOR THIS PROGRAM")
        print("1. Insert at the front")
        print("2. Delete a particular node")
        print("3. Print contents of the linked list")
        b8 = int(input("Enter your b8: "))
        if b8 = = 1:
            b9 = int(input("Enter b1 to add at the front: "))
            b7.fonk3(b9)
            b7.fonk5()
        elif b8 = = 2:
            b9 = int(input("Enter b1 to delete: "))
            b7.fonk4(b9)
            b7.fonk5()
        elif b8 = = 3:
            b7.fonk5()
        else:
            print("Wrong input! Exiting...")
            break
if b10 = = "__main__":
    fonk6()