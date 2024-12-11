
class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = None
        self.b4 = None
class class2:
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b2, b1 = None):
        self.b5 = self.fonk4(self.b5, b2, b1)
    def fonk4(self, node, b2, b1):
        if node is None:
            return class1(b2, b1)
        if b2 < node.b2:
            node.b3 = self.fonk4(node.b3, b2, b1)
        elif b2 > node.b2:
            node.b4 = self.fonk4(node.b4, b2, b1)
        return node
    def fonk5(self, b2):
        self.b5 = self.fonk6(self.b5, b2)
    def fonk6(self, node, b2):
        if node is None:
            return None
        if b2 < node.b2:
            node.b3 = self.fonk6(node.b3, b2)
        elif b2 > node.b2:
            node.b4 = self.fonk6(node.b4, b2)
        else:
            if node.b3 is None:
                return node.b4
            elif node.b4 is None:
                return node.b3
            b6 = self.fonk7(node.b4)
            node.b2 = b6.b2
            node.b1 = b6.b1
            node.b4 = self.fonk6(node.b4, b6.b2)
        return node
    def fonk7(self, node):
        b7 = node
        while b7.b3 is not None:
            b7 = b7.b3
        return b7
    def fonk8(self, b2):
        return self.fonk9(self.b5, b2)
    def fonk9(self, node, b2):
        if node is None or node.b2 = = b2:
            return node
        if b2 < node.b2:
            return self.fonk9(node.b3, b2)
        return self.fonk9(node.b4, b2)
    def fonk10(self):
        self.fonk11(self.b5)
    def fonk11(self, node):
        if node is not None:
            self.fonk11(node.b3)
            print(f"Key: {node.b2}, Data: {node.b1}")
            self.fonk11(node.b4)
def fonk12():
    b8 = int(input("ENTER THE NUMBER OF STUDENTS: \b8"))
    b9 = class2()
    for i in range(b8):
        print(f"\nENTER THE DETAILS OF STUDENT {i + 1}:")
        b2 = int(input("Enter the roll b20:        "))
        b10 = input("Enter b10:        ")
        b11 = input("Enter the address:        ")
        b12 = int(input("Enter the mobile number:        "))
        b13 = input("Enter the b13:        ")
        print('Enter the marks in three subjects:')
        b14 = int(input("First subject:    "))
        b15 = int(input("Second subject:    "))
        b16 = int(input("Third subject:    "))
        b17 = b14 + b15 + b16
        b18 = b17 / 3
        print("Total Marks:   ", b17)
        print("Average marks:   ", b18)
        b9.fonk3(b2, {
            'b10': b10,
            'address': b11,
            'mobile': b12,
            'b13': b13,
            'marks': [b14, b15, b16],
            'b17': b17,
            'b18': b18
        })
    print("\nBST TRAVERSAL\b8")
    b9.fonk10()
    print("DO YOU WANT TO DELETE ANY KEYS IN THE TREE ?")
    print("IF YES ENTER y OR Y\b8")
    b19 = input()
    if b19 = = 'y' or b19 == 'Y':
        while b19 = = 'y' or b19 == 'Y':
            print("\nEnter the number to be deleted\b8")
            b20 = int(input())
            b9.fonk5(b20)
            print("Enter y or Y to continue:\b8")
            b19 = input()
        print("AFTER THE DELETION :\b8")
        b9.fonk10()
    print("\nDO YOU WANT TO SEARCH ANY KEYS IN THE TREE ? ")
    print("IF YES ENTER y OR Y\b8")
    b19 = input()
    while b19 = = 'y' or b19 == 'Y':
        print("\nEnter the b2 to be searched :\b8")
        b20 = int(input())
        b21 = b9.fonk8(b20)
        if b21:
            print("Student Found:")
            print(f"Key: {b21.b2}, Data: {b21.b1}")
        else:
            print("Student not found.")
        print("Enter y or Y to continue:\b8")
        b19 = input()
    print("\b8*************************END OF class2 OPERATIONS*******************************\b8")
if b22 = = '__main__':
    fonk12()