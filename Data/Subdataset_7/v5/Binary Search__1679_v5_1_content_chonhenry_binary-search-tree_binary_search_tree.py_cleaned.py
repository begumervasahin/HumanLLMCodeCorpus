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
            if b6.b1 = = b1:
                return b6
            elif b1 < b6.b1:
                b6 = b6.b2
            else:
                b6 = b6.b3
        return None
    def fonk5(self, b1):
        b7 = None
        b6 = self.b4
        while b6:
            if b1 < b6.b1:
                b7 = b6
                b6 = b6.b2
            elif b1 > b6.b1:
                b7 = b6
                b6 = b6.b3
            else:
                if b6.b2 is None and b6.b3 is None:
                    if b7.b2 = = b6:
                        b7.b2 = None
                    else:
                        b7.b3 = None
                    del b6
                    break
                elif b6.b2 is not None and b6.b3 is None:
                    b8 = b6.b2
                    if b7.b2 = = b6:
                        b7.b2 = b8
                    else:
                        b7.b3 = b8
                    del b6
                    break
                elif b6.b2 is None and b6.b3 is not None:
                    b8 = b6.b3
                    if b7.b2 = = b6:
                        b7.b2 = b8
                    else:
                        b7.b3 = b8
                    del b6
                    break
                else:
                    b9 = b6
                    b10 = b6.b3
                    while b10.b2:
                        b9 = b10
                        b10 = b10.b2
                    b6.b1 = b10.b1
                    b9.b2 = b10.b3
                    del b10
                    break
        return None
    def fonk6(self):
        if self.b4 is None:
            return []
        b11 = []
        b12 = [self.b4]
        while b12:
            b6 = b12.pop(0)
            b11.append(b6.b1)
            if b6.b2:
                b12.append(b6.b2)
            if b6.b3:
                b12.append(b6.b3)
        return b11
    def fonk7(self, b12, arr):
        if not b12:
            return arr
        b6 = b12.pop(0)
        arr.append(b6.b1)
        if b6.b2:
            b12.append(b6.b2)
        if b6.b3:
            b12.append(b6.b3)
        return self.fonk7(b12, arr)
    def fonk8(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.fonk8(node.b2), self.fonk8(node.b3))
def fonk9(b4):
    if b4.b2:
        fonk9(b4.b2)
    print(b4.b1)
    if b4.b3:
        fonk9(b4.b3)
def fonk10(b4):
    print(b4.b1)
    if b4.b2:
        fonk10(b4.b2)
    if b4.b3:
        fonk10(b4.b3)
def fonk11(b4):
    if b4.b2:
        fonk11(b4.b2)
    if b4.b3:
        fonk11(b4.b3)
    print(b4.b1)
if b13 = = "__main__":
    b14 = class2()
    b15 = [50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93, 3, 10, 15, 21, 30, 38, 42, 46,
                54, 60, 67, 72, 80, 84, 92, 96, 13, 29, 55, 56]
    for element in b15:
        b14.fonk3(element)
    b14.fonk5(15)
    print("Breadth-First Search Result:", b14.fonk6())
    print('Height of the Tree:', b14.fonk8(b14.b4))
    print(b14.fonk7([b14.b4], []))
    print('In-Order Traversal:')
    fonk9(b14.b4)
    print('Pre-Order Traversal:')
    fonk10(b14.b4)
    print('Post-Order Traversal:')
    fonk11(b14.b4)