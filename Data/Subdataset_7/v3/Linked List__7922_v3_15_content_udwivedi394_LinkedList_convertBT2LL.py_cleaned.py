class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        pass
    def fonk4(self):
        b5 = []
        b6 = self.b4
        while len(b5) or b6:
            while b6:
                b5.append(b6)
                b6 = b6.b2
            b6 = b5.pop()
            print(b6.b1, b7 = " ")
            b6 = b6.b3
        print()
def fonk5(b4):
    b5 = []
    b8 = b4
    while True:
        while b8:
            b5.append(b8)
            b8 = b8.b2
        if not b5:
            break
        b8 = b5.pop()
        print(b8.b1, b7 = " ")
        b8 = b8.b3
    print()
def fonk6(b4):
    b5 = []
    b9 = None
    b10 = None
    b11 = None
    b8 = b4
    while True:
        while b8:
            b5.append(b8)
            b8 = b8.b2
        if not b5:
            break
        b8 = b5.pop()
        b8.b2 = b9
        if b9:
            b9.b3 = b8
        else:
            b10 = b8
        b9 = b8
        print(b8.b1, b7 = " ")
        if not b8.b3:
            b11 = b8
        b8 = b8.b3
    b11.b3 = b10
    b10.b2 = b11
    print()
    return b10
def fonk7(b4):
    b6 = b4
    b12 = True
    while b6 and (b12 or b6 != b4):
        print(b6.b1, "->", b7 = " ")
        b6 = b6.b3
        b12 = False
    print("None")
b4 = class1(10)
b4.b2 = class1(12)
b4.b2.b2 = class1(25)
b4.b2.b3 = class1(30)
b4.b3 = class1(15)
b4.b3.b2 = class1(36)
print("In-order Traversal of the Binary Tree:")
fonk5(b4)
print("\nConversion of Binary Tree to Doubly Linked List:")
b10 = fonk6(b4)
print("\nTraversal of the Doubly Linked List:")
fonk7(b10)