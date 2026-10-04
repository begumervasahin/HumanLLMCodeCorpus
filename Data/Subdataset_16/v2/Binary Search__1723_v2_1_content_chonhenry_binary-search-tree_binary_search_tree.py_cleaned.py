class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        b5 = class1(b1)
        if self.b4 is None:
            self.b4 = b5
        else:
            b6 = self.b4
            while True:
                if b1 < b6.b1:
                    if b6.b2 is None:
                        b6.b2 = b5
                        break
                    b6 = b6.b2
                elif b1 > b6.b1:
                    if b6.b3 is None:
                        b6.b3 = b5
                        break
                    b6 = b6.b3
                else:
                    break
    def fonk4(self, b1):
        b6 = self.b4
        while b6 is not None:
            if b1 < b6.b1:
                b6 = b6.b2
            elif b1 > b6.b1:
                b6 = b6.b3
            else:
                print(f'Value {b1} found:')
                print(f'Left child: {b6.b2.b1 if b6.b2 else "None"}')
                print(f'Right child: {b6.b3.b1 if b6.b3 else "None"}')
                return
        print('Value not found')
    def fonk5(self, b1):
        b7 = None
        b6 = self.b4
        while b6 is not None:
            if b1 < b6.b1:
                b7 = b6
                b6 = b6.b2
            elif b1 > b6.b1:
                b7 = b6
                b6 = b6.b3
            else:
                if b6.b2 is None and b6.b3 is None:
                    if b7 is None:
                        self.b4 = None
                    elif b7.b2 = = b6:
                        b7.b2 = None
                    else:
                        b7.b3 = None
                elif b6.b2 is None:
                    if b7 is None:
                        self.b4 = b6.b3
                    elif b7.b2 = = b6:
                        b7.b2 = b6.b3
                    else:
                        b7.b3 = b6.b3
                elif b6.b3 is None:
                    if b7 is None:
                        self.b4 = b6.b2
                    elif b7.b2 = = b6:
                        b7.b2 = b6.b2
                    else:
                        b7.b3 = b6.b2
                else:
                    b8 = self.fonk6(b6.b3)
                    b9 = b8.b1
                    self.fonk5(b9)
                    b6.b1 = b9
                return
        print("Value not found")
    def fonk6(self, node):
        b6 = node
        while b6.b2 is not None:
            b6 = b6.b2
        return b6
    def fonk7(self):
        b6 = self.b4
        b10 = []
        b11 = []
        if b6:
            b11.append(b6)
        while b11:
            b6 = b11.pop(0)
            b10.append(b6.b1)
            if b6.b2 is not None:
                b11.append(b6.b2)
            if b6.b3 is not None:
                b11.append(b6.b3)
        return b10
    def fonk8(self, b11, b10):
        if not b11:
            return b10
        b6 = b11.pop(0)
        b10.append(b6.b1)
        if b6.b2 is not None:
            b11.append(b6.b2)
        if b6.b3 is not None:
            b11.append(b6.b3)
        return self.fonk8(b11, b10)
    def fonk9(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.fonk9(node.b2), self.fonk9(node.b3))
def fonk10(b4):
    if b4:
        fonk10(b4.b2)
        print(b4.b1)
        fonk10(b4.b3)
def fonk11(b4):
    if b4:
        print(b4.b1)
        fonk11(b4.b2)
        fonk11(b4.b3)
def fonk12(b4):
    if b4:
        fonk12(b4.b2)
        fonk12(b4.b3)
        print(b4.b1)
if b12 = = "__main__":
    b13 = class2()
    b14 = [
        50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93, 3, 10, 15, 21,
        30, 38, 42, 46, 54, 60, 67, 72, 80, 84, 92, 96, 13, 29, 55, 56
    ]
    for el in b14:
        b13.fonk3(el)
    b13.fonk5(15)
    print("Breadth-First Search:", b13.fonk7())
    print('Height of the b13:', b13.fonk9(b13.b4))
    print("Breadth-First Search (Recursive):", b13.fonk8([b13.b4], []))
    print('In-Order Traversal:')
    fonk10(b13.b4)
    print('Pre-Order Traversal:')
    fonk11(b13.b4)
    print('Post-Order Traversal:')
    fonk12(b13.b4)