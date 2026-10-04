class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b11, b1):
        if b11 is None:
            return class1(b1)
        else:
            if b1 <= b11.b1:
                b11.b2 = self.fonk2(b11.b2, b1)
            else:
                b11.b3 = self.fonk2(b11.b3, b1)
        return b11
    def fonk3(self, b11):
        if b11 is None:
            return -1
        else:
            b4 = self.fonk3(b11.b2)
            b5 = self.fonk3(b11.b3)
            return max(b4, b5) + 1
    def fonk4(self, b11):
        if b11:
            self.fonk4(b11.b2)
            print(b11.b1, b6 = " ")
            self.fonk4(b11.b3)
    def fonk5(self, b11):
        if b11:
            self.fonk5(b11.b2)
            self.fonk5(b11.b3)
            print(b11.b1, b6 = " ")
    def fonk6(self, b11):
        if b11:
            print(b11.b1, b6 = " ")
            self.fonk6(b11.b2)
            self.fonk6(b11.b3)
    def fonk7(self, b11):
        if b11:
            b7 = [b11]
            while b7:
                b8 = b7.pop(0)
                print(b8.b1, b6 = " ")
                if b8.b2:
                    b7.append(b8.b2)
                if b8.b3:
                    b7.append(b8.b3)
if b9 = = "__main__":
    b10 = class2()
    b11 = None
    b12 = [5, 3, 8, 2, 4, 7, 9]
    for b1 in b12:
        b11 = b10.fonk2(b11, b1)
    print("InOrder Traversal: ", b6 = "")
    b10.fonk4(b11)
    print("\nPostOrder Traversal: ", b6 = "")
    b10.fonk5(b11)
    print("\nPreOrder Traversal: ", b6 = "")
    b10.fonk6(b11)
    print("\nLevelOrder Traversal: ", b6 = "")
    b10.fonk7(b11)
    print("\nTree Height:", b10.fonk3(b11))