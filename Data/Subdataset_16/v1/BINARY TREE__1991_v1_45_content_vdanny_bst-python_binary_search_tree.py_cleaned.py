import sys
class class1:
    def fonk1(self, b2):
        self.b1 = self.b4 = None
        self.b2 = b2
class class2:
    def fonk2(self, b8, b2):
        if b8 is None:
            return class1(b2)
        else:
            if b2 <= b8.b2:
                b3 = self.fonk2(b8.b4, b2)
                b8.b4 = b3
            else:
                b3 = self.fonk2(b8.b1, b2)
                b8.b1 = b3
        return b8
    def fonk3(self, b8):
        if b8 is None:
            return -1
        else:
            b4 = self.fonk3(b8.b4)
            b1 = self.fonk3(b8.b1)
            if b4 > b1:
                return b4 + 1
            else:
                return b1 + 1
    def fonk4(self, b8):
        if b8 is not None:
            self.fonk4(b8.b4)
            sys.stdout.write(str(b8.b2) + " ")
            sys.stdout.flush()
            self.fonk4(b8.b1)
    def fonk5(self, b8):
        if b8 is not None:
            self.fonk5(b8.b4)
            self.fonk5(b8.b1)
            sys.stdout.write(str(b8.b2) + " ")
            sys.stdout.flush()
    def fonk6(self, b8):
        if b8 is not None:
            sys.stdout.write(str(b8.b2) + " ")
            sys.stdout.flush()
            self.fonk6(b8.b4)
            self.fonk6(b8.b1)
    def fonk7(self, b8):
        b5 = []
        if b8 is not None:
            b5.append(b8)
            a1 = 0
            b3 = b5[a1]
            while b3 is not None:
                sys.stdout.write(str(b3.b2) + " ")
                sys.stdout.flush()
                if b3.b4 is not None:
                    b5.append(b3.b4)
                if b3.b1 is not None:
                    b5.append(b3.b1)
                a1 += 1
                if a1 < len(b5):
                    b3 = b5[a1]
                else:
                    b3 = None
if b6 = = "__main__":
    b7 = class2()
    b8 = None
    b9 = [3, 5, 2, 1, 4, 6, 7]
    for b2 in b9:
        b8 = b7.fonk2(b8, b2)
    print("In-order traversal:")
    b7.fonk4(b8)
    print("\nPost-order traversal:")
    b7.fonk5(b8)
    print("\nPre-order traversal:")
    b7.fonk6(b8)
    print("\nLevel-order traversal:")
    b7.fonk7(b8)
    print("\nHeight of b7:", b7.fonk3(b8))