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
    def fonk4(self, b1, b9):
        b4 = class1(b1)
        if self.b3 is None:
            print("List is empty")
            return
        b5 = self.b3
        while b5:
            if b5.b1 = = b9:
                break
            b5 = b5.b2
        if b5 is None:
            print("Key not found")
            return
        b4.b2 = b5.b2
        b5.b2 = b4
    def fonk5(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk6(self):
        b6 = self.b3
        while b6:
            print(b6.b1)
            b6 = b6.b2
b7 = class2()
while True:
    print("1. Insert at beginning")
    print("2. Insert at position")
    print("3. Insert at end")
    print("4. Display list")
    print("5. Exit")
    b8 = int(input("Enter your choice: "))
    if b8 = = 1:
        b1 = input("Enter the element to insert: ")
        b7.fonk3(b1)
    elif b8 = = 2:
        b1 = input("Enter the element to insert: ")
        b9 = input("Enter the element after insertion: ")
        b7.fonk4(b1, b9)
    elif b8 = = 3:
        b1 = input("Enter the element to insert: ")
        b7.fonk5(b1)
    elif b8 = = 4:
        print("Linked List:")
        b7.fonk6()
    elif b8 = = 5:
        print("Exiting...")
        break
    else:
        print("Invalid input. Please try again.")