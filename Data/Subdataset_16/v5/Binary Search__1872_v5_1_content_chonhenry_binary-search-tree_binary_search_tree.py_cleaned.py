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
        while b6:
            if b1 < b6.b1:
                b6 = b6.b2
            elif b1 > b6.b1:
                b6 = b6.b3
            else:
                print(f"Value {b1} found.")
                b7 = b6.b2.b1 if b6.b2 else 'None'
                b8 = b6.b3.b1 if b6.b3 else 'None'
                print(f"Left child: {b7}")
                print(f"Right child: {b8}")
                return b6
        print("Value not found.")
        return None
    def fonk5(self, b1):
        b9 = None
        b6 = self.b4
        while b6:
            if b1 < b6.b1:
                b9 = b6
                b6 = b6.b2
            elif b1 > b6.b1:
                b9 = b6
                b6 = b6.b3
            else:
                if b6.b2 is None and b6.b3 is None:
                    self.fonk6(b9, b6)
                elif b6.b2 is None:
                    self.fonk7(b9, b6, b6.b3)
                elif b6.b3 is None:
                    self.fonk7(b9, b6, b6.b2)
                else:
                    self.fonk8(b6)
                return
        print("Value not found in the b15.")
    def fonk6(self, b9, b6):
        if b9 is None:
            self.b4 = None
        elif b9.b2 = = b6:
            b9.b2 = None
        else:
            b9.b3 = None
        del b6
    def fonk7(self, b9, b6, child):
        if b9 is None:
            self.b4 = child
        elif b9.b2 = = b6:
            b9.b2 = child
        else:
            b9.b3 = child
        del b6
    def fonk8(self, b6):
        b10 = b6
        b11 = b6.b3
        while b11.b2:
            b10 = b11
            b11 = b11.b2
        b6.b1 = b11.b1
        if b10.b2 = = b11:
            b10.b2 = b11.b3
        else:
            b10.b3 = b11.b3
        del b11
    def fonk9(self):
        if self.b4 is None:
            return []
        b12 = [self.b4]
        b13 = []
        while b12:
            b6 = b12.pop(0)
            b13.append(b6.b1)
            if b6.b2:
                b12.append(b6.b2)
            if b6.b3:
                b12.append(b6.b3)
        return b13
    def fonk10(self, b12, arr):
        if not b12:
            return arr
        b6 = b12.pop(0)
        arr.append(b6.b1)
        if b6.b2:
            b12.append(b6.b2)
        if b6.b3:
            b12.append(b6.b3)
        return self.fonk10(b12, arr)
    def fonk11(self, node):
        if node is None:
            return 0
        return 1 + max(self.fonk11(node.b2), self.fonk11(node.b3))
def fonk12(b4):
    if b4:
        fonk12(b4.b2)
        print(b4.b1)
        fonk12(b4.b3)
def fonk13(b4):
    if b4:
        print(b4.b1)
        fonk13(b4.b2)
        fonk13(b4.b3)
def fonk14(b4):
    if b4:
        fonk14(b4.b2)
        fonk14(b4.b3)
        print(b4.b1)
if b14 = = "__main__":
    b15 = class2()
    b16 = [
        50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93,
        3, 10, 15, 21, 30, 38, 42, 46, 54, 60, 67, 72, 80, 84, 92,
        96, 13, 29, 55, 56
    ]
    for b1 in b16:
        b15.fonk3(b1)
    b15.fonk5(15)
    print("Breadth-first search:", b15.fonk9())
    print("Height of the b15:", b15.fonk11(b15.b4))
    print("Breadth-first search (recursive):", b15.fonk10([b15.b4], []))
    print("\nIn-order traversal:")
    fonk12(b15.b4)
    print("\nPre-order traversal:")
    fonk13(b15.b4)
    print("\nPost-order traversal:")
    fonk14(b15.b4)