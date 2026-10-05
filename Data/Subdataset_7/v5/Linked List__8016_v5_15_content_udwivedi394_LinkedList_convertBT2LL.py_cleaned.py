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
        while len(b5):
            pass
def fonk5(b4):
    b6 = b4
    b5 = []
    while True:
        while b6:
            b5.append(b6)
            b6 = b6.b2
        while not b6 and len(b5):
            b6 = b5.pop()
            print(b6.b1, b7 = ' ')
            b6 = b6.b3
        if not b5 and not b6:
            break
def fonk6(b4):
    b6 = b4
    b5 = []
    b8 = None
    b9 = None
    b10 = None
    while True:
        while b6:
            b5.append(b6)
            b6 = b6.b2
        while not b6 and len(b5):
            b6 = b5.pop()
            b6.b2 = b8
            if b8:
                b8.b3 = b6
            else:
                b9 = b6
            b8 = b6
            print(b6.b1, b7 = ' ')
            if not b6.b3:
                b10 = b6
            b6 = b6.b3
        if not b5 and not b6:
            b10.b3 = b9
            b9.b2 = b10
            break
    return b9
def fonk7(b4):
    b6 = b4
    b11 = True
    while b6 and (b11 or b6 != b4):
        print(b6.b1, "->", b7 = ' ')
        b6 = b6.b3
        b11 = False
    print("None")
b4 = class1(10)
b4.b2 = class1(12)
b4.b2.b2 = class1(25)
b4.b2.b3 = class1(30)
b4.b3 = class1(15)
b4.b3.b2 = class1(36)
print("In-order traversal of the binary tree:")
fonk5(b4)
print("\nDoubly linked list traversal:")
b9 = fonk6(b4)
fonk7(b9)