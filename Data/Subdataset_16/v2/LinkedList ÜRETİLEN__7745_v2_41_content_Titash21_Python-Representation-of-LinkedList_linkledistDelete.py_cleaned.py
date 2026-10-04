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
            print("You are trying to delete from an empty list")
            return
        if self.b3.b1 = = b1:
            self.b3 = self.b3.b2
            return
        b5 = self.b3
        b6 = None
        while b5 and b5.b1 != b1:
            b6 = b5
            b5 = b5.b2
        if b5 is None:
            print("The b1 you want to delete is not in the list")
            return
        b6.b2 = b5.b2
    def fonk5(self):
        if self.b3 is None:
            print("Empty linked list")
            return
        b5 = self.b3
        while b5:
            print(b5.b1, b7 = " -> ")
            b5 = b5.b2
        print("None")
def fonk6():
    b8 = class2()
    while True:
        print("\nOPTIONS FOR THIS PROGRAM")
        print("1. Insert at front")
        print("2. Delete a particular node")
        print("3. Print contents of the linked list")
        print("4. Exit")
        try:
            b9 = int(input("Enter your b9: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if b9 = = 1:
            try:
                b10 = int(input("Enter b1 to add in front: "))
                b8.fonk3(b10)
                b8.fonk5()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif b9 = = 2:
            try:
                b10 = int(input("Enter b1 to delete: "))
                b8.fonk4(b10)
                b8.fonk5()
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif b9 = = 3:
            b8.fonk5()
        elif b9 = = 4:
            break
        else:
            print("Wrong input! Please try again.")
if b11 = = "__main__":
    fonk6()