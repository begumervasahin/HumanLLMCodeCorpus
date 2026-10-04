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
            return
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
        while b6:
            if b1 < b6.b1:
                b6 = b6.b2
            elif b1 > b6.b1:
                b6 = b6.b3
            else:
                print(f'Value {b1} found:')
                print(f'Left child: {b6.b2.b1 if b6.b2 else "None"}')
                print(f'Right child: {b6.b3.b1 if b6.b3 else "None"}')
                return b6
        print(f'Value {b1} not found')
        return None
    def fonk5(self, b1):
        parent, b6 = None, self.b4
        while b6:
            if b1 < b6.b1:
                parent, b6 = b6, b6.b2
            elif b1 > b6.b1:
                parent, b6 = b6, b6.b3
            else:
                if b6.b2 is None and b6.b3 is None:
                    self.fonk6(parent, b6, None)
                elif b6.b2 is None:
                    self.fonk6(parent, b6, b6.b3)
                elif b6.b3 is None:
                    self.fonk6(parent, b6, b6.b2)
                else:
                    b7 = self.fonk7(b6.b3)
                    b6.b1 = b7.b1
                    b6.b3 = self.fonk5(b7.b1)
                return b6
        print(f"Value {b1} not found")
        return None
    def fonk6(self, parent, b6, new_child):
        if parent is None:
            self.b4 = new_child
        elif parent.b2 = = b6:
            parent.b2 = new_child
        else:
            parent.b3 = new_child
    def fonk7(self, node):
        b6 = node
        while b6.b2:
            b6 = b6.b2
        return b6
    def fonk8(self):
        if not self.b4:
            return []
        b9, b8 = [self.b4], []
        while b9:
            b6 = b9.pop(0)
            b8.append(b6.b1)
            if b6.b2:
                b9.append(b6.b2)
            if b6.b3:
                b9.append(b6.b3)
        return b8
    def fonk9(self, b9 = None, b8=None):
        if b9 is None:
            b9 = [self.b4] if self.b4 else []
        if b8 is None:
            b8 = []
        if not b9:
            return b8
        b6 = b9.pop(0)
        b8.append(b6.b1)
        if b6.b2:
            b9.append(b6.b2)
        if b6.b3:
            b9.append(b6.b3)
        return self.fonk9(b9, b8)
    def fonk10(self, node):
        if node is None:
            return 0
        return 1 + max(self.fonk10(node.b2), self.fonk10(node.b3))
def fonk11(node):
    if node:
        fonk11(node.b2)
        print(node.b1)
        fonk11(node.b3)
def fonk12(node):
    if node:
        print(node.b1)
        fonk12(node.b2)
        fonk12(node.b3)
def fonk13(node):
    if node:
        fonk13(node.b2)
        fonk13(node.b3)
        print(node.b1)
if b10 = = "__main__":
    b11 = class2()
    b12 = [
        50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93, 3, 10, 15, 21,
        30, 38, 42, 46, 54, 60, 67, 72, 80, 84, 92, 96, 13, 29, 55, 56
    ]
    for el in b12:
        b11.fonk3(el)
    b11.fonk5(15)
    print("Breadth-First Search:", b11.fonk8())
    print('Height of the b11:', b11.fonk10(b11.b4))
    print("Breadth-First Search (Recursive):", b11.fonk9())
    print('In-Order Traversal:')
    fonk11(b11.b4)
    print('Pre-Order Traversal:')
    fonk12(b11.b4)
    print('Post-Order Traversal:')
    fonk13(b11.b4)