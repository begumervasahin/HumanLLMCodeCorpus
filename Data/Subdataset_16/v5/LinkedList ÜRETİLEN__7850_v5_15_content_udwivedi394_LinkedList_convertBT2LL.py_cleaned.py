class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        if not self.b4:
            self.b4 = class1(b1)
        else:
            self.fonk4(self.b4, b1)
    def fonk4(self, current_node, b1):
        if b1 < current_node.b1:
            if current_node.b2:
                self.fonk4(current_node.b2, b1)
            else:
                current_node.b2 = class1(b1)
        else:
            if current_node.b3:
                self.fonk4(current_node.b3, b1)
            else:
                current_node.b3 = class1(b1)
    def fonk5(self):
        if not self.b4:
            return None
        b5 = []
        b6 = self.b4
        b7 = None
        b8 = None
        b9 = None
        while True:
            while b6:
                b5.append(b6)
                b6 = b6.b2
            if not b5:
                break
            b6 = b5.pop()
            b6.b2 = b7
            if b7:
                b7.b3 = b6
            else:
                b8 = b6
            b7 = b6
            if not b6.b3:
                b9 = b6
            b6 = b6.b3
        if b9 and b8:
            b9.b3 = b8
            b8.b2 = b9
        return b8
def fonk6(b4):
    b6 = b4
    b5 = []
    while True:
        while b6:
            b5.append(b6)
            b6 = b6.b2
        if not b5:
            break
        b6 = b5.pop()
        print(b6.b1, b10 = " ")
        b6 = b6.b3
def fonk7(b8):
    b6 = b8
    b11 = True
    while b6 and (b11 or b6 != b8):
        print(b6.b1, b10 = " -> ")
        b6 = b6.b3
        b11 = False
    print("None")
b4 = class1(10)
b4.b2 = class1(12)
b4.b2.b2 = class1(25)
b4.b2.b3 = class1(30)
b4.b3 = class1(15)
b4.b3.b2 = class1(36)
print("In-order Traversal of the class2:")
fonk6(b4)
print("\n")
print("Converting class2 to DLL and displaying the DLL:")
b12 = class2()
b12.b4 = b4
b8 = b12.fonk5()
print("\n")
print("Traversal of the Circular DLL:")
fonk7(b8)