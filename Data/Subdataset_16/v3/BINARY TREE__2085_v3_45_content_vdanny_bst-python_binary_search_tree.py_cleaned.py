class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
class class2:
    def fonk2(self, b11, b3):
        if b11 is None:
            return class1(b3)
        if b3 <= b11.b3:
            b11.b2 = self.fonk2(b11.b2, b3)
        else:
            b11.b1 = self.fonk2(b11.b1, b3)
        return b11
    def fonk3(self, b11):
        if b11 is None:
            return -1
        b4 = self.fonk3(b11.b2)
        b5 = self.fonk3(b11.b1)
        return max(b4, b5) + 1
    def fonk4(self, b11):
        if b11:
            self.fonk4(b11.b2)
            print(b11.b3, b6 = " ")
            self.fonk4(b11.b1)
    def fonk5(self, b11):
        if b11:
            self.fonk5(b11.b2)
            self.fonk5(b11.b1)
            print(b11.b3, b6 = " ")
    def fonk6(self, b11):
        if b11:
            print(b11.b3, b6 = " ")
            self.fonk6(b11.b2)
            self.fonk6(b11.b1)
    def fonk7(self, b11):
        if b11 is None:
            return
        b7 = [b11]
        while b7:
            b8 = b7.pop(0)
            print(b8.b3, b6 = " ")
            if b8.b2:
                b7.append(b8.b2)
            if b8.b1:
                b7.append(b8.b1)
if b9 = = "__main__":
    b10 = class2()
    b11 = None
    b12 = [3, 5, 2, 1, 4, 6, 7]
    for b3 in b12:
        b11 = b10.fonk2(b11, b3)
    print("In-order traversal:")
    b10.fonk4(b11)
    print("\nPost-order traversal:")
    b10.fonk5(b11)
    print("\nPre-order traversal:")
    b10.fonk6(b11)
    print("\nLevel-order traversal:")
    b10.fonk7(b11)
    print("\nHeight of b10:", b10.fonk3(b11))