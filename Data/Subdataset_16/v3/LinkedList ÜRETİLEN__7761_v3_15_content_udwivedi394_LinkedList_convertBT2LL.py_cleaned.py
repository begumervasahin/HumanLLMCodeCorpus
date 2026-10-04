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
        while b5:
            pass
def fonk5(b4):
    b6 = b4
    b5 = []
    while True:
        while b6:
            b5.append(b6)
            b6 = b6.b2
        if not b5:
            break
        b6 = b5.pop()
        print(b6.b1, b7 = ' ')
        b6 = b6.b3
def fonk6(b4):
    if not b4:
        return None
    b6 = b4
    b5 = []
    b8 = None
    b9 = None
    b10 = None
    while True:
        while b6:
            b5.append(b6)
            b6 = b6.b2
        if not b5:
            break
        b6 = b5.pop()
        b6.b2 = b8
        if b8:
            b8.b3 = b6
        else:
            b9 = b6
        b8 = b6
        if not b6.b3:
            b10 = b6
        b6 = b6.b3
    if b9 and b10:
        b9.b2 = b10
        b10.b3 = b9
    return b9
def fonk7(b9):
    if not b9:
        return
    b6 = b9
    while True:
        print(f"{b6.b1} ->", b7 = ' ')
        b6 = b6.b3
        if b6 = = b9:
            break
    print("None")
if b11 = = "__main__":
    b4 = class1(10)
    b4.b2 = class1(12)
    b4.b2.b2 = class1(25)
    b4.b2.b3 = class1(30)
    b4.b3 = class1(15)
    b4.b3.b2 = class1(36)
    print("In-order Traversal of Binary Tree:")
    fonk5(b4)
    print("\n")
    print("Converting Binary Tree to Circular Doubly Linked List:")
    b9 = fonk6(b4)
    print("\n")
    print("Traversal of Circular Doubly Linked List:")
    fonk7(b9)