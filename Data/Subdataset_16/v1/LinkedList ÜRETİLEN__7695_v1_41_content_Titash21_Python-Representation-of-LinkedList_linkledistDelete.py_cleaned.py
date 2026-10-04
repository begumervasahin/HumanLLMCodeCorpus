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
        while b5 is not None and b5.b1 != b1:
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
        b7 = self.b3
        while b7:
            print(b7.b1, b8 = " -> ")
            b7 = b7.b2
        print("None")
def fonk6():
    b9 = class2()
    while True:
        print("\nOPTIONS FOR THIS PROGRAM")
        print("1. To insert at front")
        print("2. Delete a particular node")
        print("3. Print contents of the linked list")
        print("4. Exit")
        b10 = int(input("Enter your b10: "))
        if b10 = = 1:
            b11 = int(input("Enter b1 to add in front: "))
            b9.fonk3(b11)
            b9.fonk5()
        elif b10 = = 2:
            b11 = int(input("Enter b1 to delete: "))
            b9.fonk4(b11)
            b9.fonk5()
        elif b10 = = 3:
            b9.fonk5()
        elif b10 = = 4:
            break
        else:
            print("Wrong input! Please try again.")
if b12 = = "__main__":
    fonk6()