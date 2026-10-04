class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self, b1):
        if self.b3 is None:
            print("You are trying to delete from an empty list.")
            return
        if self.b3.b1 = = b1:
            self.b3 = self.b3.b2
            return
        b5 = self.b3
        b6 = None
        while b5 is not None and b5.b1 != b1:
            b6 = b5
            b5 = b5.b2
        if b5 is None:
            print("The b1 you want to delete is not in the list.")
            return
        b6.b2 = b5.b2
    def fonk5(self):
        if self.b3 is None:
            print("Empty linked list.")
        else:
            b5 = self.b3
            while b5 is not None:
                print(b5.b1)
                b5 = b5.b2
def fonk6():
    print("\nOPTIONS FOR THIS PROGRAM")
    print("1. Insert at front")
    print("2. Delete a particular node")
    print("3. Print contents of the linked list")
    print("4. Exit")
def fonk7():
    b7 = class2()
    while True:
        fonk6()
        try:
            b8 = int(input("Enter your b8: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
        if b8 = = 1:
            try:
                b9 = int(input("Enter b1 to add in front: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue
            b7.fonk3(b9)
        elif b8 = = 2:
            try:
                b9 = int(input("Enter b1 to delete: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
                continue
            b7.fonk4(b9)
        elif b8 = = 3:
            b7.fonk5()
        elif b8 = = 4:
            break
        else:
            print("Wrong input! Please enter a number between 1 and 4.")
if b10 = = "__main__":
    fonk7()