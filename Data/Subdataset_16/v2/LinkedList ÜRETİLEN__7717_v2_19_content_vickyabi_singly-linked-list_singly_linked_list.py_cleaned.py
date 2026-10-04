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
    def fonk4(self, b1, b10):
        b4 = class1(b1)
        b5 = self.b3
        if self.b3 is None:
            print("The list is empty.")
            return
        while b5 is not None and b5.b1 != b10:
            b5 = b5.b2
        if b5 is None:
            print(f"class1 with b1 {b10} not found.")
        else:
            b4.b2 = b5.b2
            b5.b2 = b4
    def fonk5(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
        else:
            b6 = self.b3
            while b6.b2 is not None:
                b6 = b6.b2
            b6.b2 = b4
    def fonk6(self):
        if self.b3 is None:
            print("The list is empty.")
            return
        b5 = self.b3
        while b5 is not None:
            print(b5.b1, b7 = ' -> ')
            b5 = b5.b2
        print("None")
def fonk7():
    b8 = class2()
    while True:
        print("\nMenu:")
        print("1. Insert at beginning")
        print("2. Insert at position")
        print("3. Insert at b7")
        print("4. Display list")
        print("5. Exit")
        try:
            b9 = int(input("Enter your b9: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if b9 = = 1:
            b1 = input("Enter the element to insert: ")
            b8.fonk3(b1)
        elif b9 = = 2:
            b1 = input("Enter the element to insert: ")
            b10 = input("Enter the element after which to insert: ")
            b8.fonk4(b1, b10)
        elif b9 = = 3:
            b1 = input("Enter the element to insert: ")
            b8.fonk5(b1)
        elif b9 = = 4:
            b8.fonk6()
        elif b9 = = 5:
            print("Exiting...")
            break
        else:
            print("Invalid b9. Please try again.")
if b11 = = "__main__":
    fonk7()