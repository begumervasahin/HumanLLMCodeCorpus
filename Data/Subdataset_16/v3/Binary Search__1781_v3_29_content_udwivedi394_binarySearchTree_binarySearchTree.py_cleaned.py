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
            return
        b5 = self.b4
        while True:
            if b1 < b5.b1:
                if b5.b2:
                    b5 = b5.b2
                else:
                    b5.b2 = class1(b1)
                    break
            else:
                if b5.b3:
                    b5 = b5.b3
                else:
                    b5.b3 = class1(b1)
                    break
    def fonk4(self):
        def fonk5(node):
            if node:
                fonk5(node.b2)
                print(node.b1, b6 = " ")
                fonk5(node.b3)
        if not self.b4:
            print("Nothing to print")
            return
        print("In-Order Traversal:", b6 = " ")
        fonk5(self.b4)
        print()
    def fonk6(self):
        if not self.b4:
            print("Tree is empty")
            return
        print("Level-Order Traversal:")
        b7 = [self.b4]
        while b7:
            b5 = b7.pop(0)
            print(b5.b1, b6 = " ")
            if b5.b2:
                b7.append(b5.b2)
            if b5.b3:
                b7.append(b5.b3)
        print()
    def fonk7(self, b1, b8 = False):
        b5 = self.b4
        b9 = None
        while b5:
            if b5.b1 = = b1:
                if b8:
                    return b9
                print(f"{b1} found!")
                return True
            b9 = b5
            if b1 < b5.b1:
                b5 = b5.b2
            else:
                b5 = b5.b3
        print(f"{b1} not present")
        return None if b8 else False
    def fonk8(self, b1):
        b9 = self.fonk7(b1, b8=True)
        if b9 is None and (not self.b4 or self.b4.b1 != b1):
            print("class1 to be deleted not found!")
            return False
        b10 = self.b4 if b9 is None else (
            b9.b2 if b1 < b9.b1 else b9.b3)
        if b10 is None:
            print("class1 to be deleted not found!")
            return False
        if not (b10.b2 or b10.b3):
            if b9:
                if b9.b2 = = b10:
                    b9.b2 = None
                else:
                    b9.b3 = None
            else:
                self.b4 = None
        elif b10.b2 is None or b10.b3 is None:
            b11 = b10.b2 if b10.b2 else b10.b3
            if b9:
                if b9.b2 = = b10:
                    b9.b2 = b11
                else:
                    b9.b3 = b11
            else:
                self.b4 = b11
        else:
            b12 = b10
            b13 = b10.b3
            while b13.b2:
                b12 = b13
                b13 = b13.b2
            b10.b1 = b13.b1
            if b12.b2 = = b13:
                b12.b2 = b13.b3
            else:
                b12.b3 = b13.b3
    def fonk9(self, b14):
        def fonk10(node):
            nonlocal b14
            if node is None or b14 = = 0:
                return None
            b15 = fonk10(node.b2)
            if b15 is not None:
                return b15
            b14 -= 1
            if b14 = = 0:
                return node.b1
            return fonk10(node.b3)
        b15 = fonk10(self.b4)
        if b15 is not None:
            print(f"{b14}-th node: {b15}")
        else:
            print(f"No {b14}-th element found")
    def fonk11(self, b1):
        b5 = self.b4
        b13 = None
        while b5:
            if b1 = = b5.b1:
                break
            elif b1 < b5.b1:
                b13 = b5
                b5 = b5.b2
            else:
                b5 = b5.b3
        if not b5:
            print("Element not found")
            return None
        if b5.b3:
            b13 = b5.b3
            while b13.b2:
                b13 = b13.b2
            return b13.b1
        return b13.b1 if b13 else None
    def fonk12(self):
        return self.b4
if b16 = = "__main__":
    b17 = class2()
    b17.fonk3(10)
    b17.fonk3(5)
    b17.fonk3(20)
    b17.fonk3(15)
    b17.fonk3(25)
    b17.fonk4()
    b17.fonk6()
    b17.fonk7(15)
    b17.fonk9(3)
    b13 = b17.fonk11(15)
    if b13:
        print(f"In-order b13 of 15: {b13}")
    b17.fonk8(20)
    b17.fonk6()