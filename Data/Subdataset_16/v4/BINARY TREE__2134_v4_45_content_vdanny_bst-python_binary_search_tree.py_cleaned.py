import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b10, b1):
        if b10 is None:
            return class1(b1)
        else:
            if b1 <= b10.b1:
                b10.b2 = self.fonk2(b10.b2, b1)
            else:
                b10.b3 = self.fonk2(b10.b3, b1)
        return b10
    def fonk3(self, b10):
        if b10 is None:
            return -1
        else:
            b4 = self.fonk3(b10.b2)
            b5 = self.fonk3(b10.b3)
            return max(b4, b5) + 1
    def fonk4(self, b10):
        if b10 is not None:
            self.fonk4(b10.b2)
            sys.stdout.write(str(b10.b1) + " ")
            sys.stdout.flush()
            self.fonk4(b10.b3)
    def fonk5(self, b10):
        if b10 is not None:
            self.fonk5(b10.b2)
            self.fonk5(b10.b3)
            sys.stdout.write(str(b10.b1) + " ")
            sys.stdout.flush()
    def fonk6(self, b10):
        if b10 is not None:
            sys.stdout.write(str(b10.b1) + " ")
            sys.stdout.flush()
            self.fonk6(b10.b2)
            self.fonk6(b10.b3)
    def fonk7(self, b10):
        if b10 is not None:
            b6 = [b10]
            a1 = 0
            while a1 < len(b6):
                b7 = b6[a1]
                sys.stdout.write(str(b7.b1) + " ")
                sys.stdout.flush()
                if b7.b2 is not None:
                    b6.append(b7.b2)
                if b7.b3 is not None:
                    b6.append(b7.b3)
                a1 += 1
if b8 = = "__main__":
    b9 = class2()
    b10 = None
    b11 = [5, 3, 8, 2, 4, 7, 9]
    for b1 in b11:
        b10 = b9.fonk2(b10, b1)
    print("InOrder Traversal: ", b12 = "")
    b9.fonk4(b10)
    print("\nPostOrder Traversal: ", b12 = "")
    b9.fonk5(b10)
    print("\nPreOrder Traversal: ", b12 = "")
    b9.fonk6(b10)
    print("\nLevelOrder Traversal: ", b12 = "")
    b9.fonk7(b10)
    print("\nTree Height:", b9.fonk3(b10))