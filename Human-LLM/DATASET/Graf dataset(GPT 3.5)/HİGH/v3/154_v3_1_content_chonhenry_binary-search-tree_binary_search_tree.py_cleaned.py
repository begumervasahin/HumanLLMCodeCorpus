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
        self.b4, b7 = self.fonk6(self.b4, b1)
    def fonk6(self, b4, b1):
        if b4 is None:
            return b4, False
        if b1 < b4.b1:
            b4.b2, b8 = self.fonk6(b4.b2, b1)
        elif b1 > b4.b1:
            b4.b3, b8 = self.fonk6(b4.b3, b1)
        else:
            if b4.b2 is None:
                return b4.b3, True
            elif b4.b3 is None:
                return b4.b2, True
            b9 = self.fonk7(b4.b3)
            b4.b1 = b9.b1
            b4.b3, b7 = self.fonk6(b4.b3, b9.b1)
            b8 = True
        return b4, b8
    def fonk7(self, b4):
        b6 = b4
        while b6.b2:
            b6 = b6.b2
        return b6
    def fonk8(self):
        if self.b4 is None:
            return []
        b10 = []
        b11 = [self.b4]
        while b11:
            b6 = b11.pop(0)
            b10.append(b6.b1)
            if b6.b2:
                b11.append(b6.b2)
            if b6.b3:
                b11.append(b6.b3)
        return b10
    def fonk9(self):
        return self.fonk10(self.b4)
    def fonk10(self, node):
        if node is None:
            return 0
        else:
            b12 = self.fonk10(node.b2)
            b13 = self.fonk10(node.b3)
            return max(b12, b13) + 1
def fonk11(b4):
    if b4:
        fonk11(b4.b2)
        print(b4.b1, b14 = " ")
        fonk11(b4.b3)
def fonk12(b4):
    if b4:
        print(b4.b1, b14 = " ")
        fonk12(b4.b2)
        fonk12(b4.b3)
def fonk13(b4):
    if b4:
        fonk13(b4.b2)
        fonk13(b4.b3)
        print(b4.b1, b14 = " ")
def fonk14():
    b15 = class2()
    b16 = [50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93, 3, 10, 15, 21, 30, 38, 42, 46,
                54, 60, 67, 72, 80, 84, 92, 96, 13, 29, 55, 56]
    for element in b16:
        b15.fonk3(element)
    b15.fonk5(15)
    b17 = b15.fonk8()
    b18 = b15.fonk9()
    print("Breadth-First Search Result:", b17)
    print("Height of the Tree:", b18)
    print("In-order Traversal:")
    fonk11(b15.b4)
    print("\nPre-order Traversal:")
    fonk12(b15.b4)
    print("\nPost-order Traversal:")
    fonk13(b15.b4)
if b19 = = "__main__":
    fonk14()