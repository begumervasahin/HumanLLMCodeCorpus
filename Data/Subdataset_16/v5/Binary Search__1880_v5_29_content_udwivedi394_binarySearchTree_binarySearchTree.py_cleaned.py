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
                if b5.b2 is None:
                    b5.b2 = class1(b1)
                    break
                b5 = b5.b2
            else:
                if b5.b3 is None:
                    b5.b3 = class1(b1)
                    break
                b5 = b5.b3
    def fonk4(self):
        if not self.b4:
            print("Tree is empty")
            return
        print("\nIn Order:", b6 = " ")
        b7 = []
        b5 = self.b4
        while b7 or b5:
            while b5:
                b7.append(b5)
                b5 = b5.b2
            b5 = b7.pop()
            print(b5.b1, b6 = " ")
            b5 = b5.b3
        print()
    def fonk5(self):
        if not self.b4:
            print("Tree is empty")
            return
        print("\nLevel Order:")
        b8 = [self.b4]
        while b8:
            b5 = b8.pop(0)
            print(b5.b1, b6 = " ")
            if b5.b2:
                b8.append(b5.b2)
            if b5.b3:
                b8.append(b5.b3)
        print()
    def fonk6(self, b1):
        b5 = self.b4
        while b5:
            if b5.b1 = = b1:
                print(f"{b1} found!")
                return True
            b5 = b5.b2 if b1 < b5.b1 else b5.b3
        print(f"{b1} not found")
        return False
    def fonk7(self, b1):
        b5 = self.b4
        b9 = None
        while b5 and b5.b1 != b1:
            b9 = b5
            b5 = b5.b2 if b1 < b5.b1 else b5.b3
        return b9, b5
    def fonk8(self, b1):
        b9, b10 = self.fonk7(b1)
        if b10 is None:
            print(f"class1 with b1 {b1} not found!")
            return False
        if b10.b2 is None or b10.b3 is None:
            b11 = b10.b2 if b10.b2 else b10.b3
            if b9 is None:
                self.b4 = b11
            elif b10 = = b9.b2:
                b9.b2 = b11
            else:
                b9.b3 = b11
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
    def fonk9(self, k):
        b7 = []
        b5 = self.b4
        a1 = 0
        while b7 or b5:
            while b5:
                b7.append(b5)
                b5 = b5.b2
            b5 = b7.pop()
            a1 += 1
            if a1 = = k:
                print(f"{k}-th smallest element is {b5.b1}")
                return b5.b1
            b5 = b5.b3
        print(f"{k}-th smallest element not found")
        return None
    def fonk10(self, b1):
        b5 = self.b4
        b13 = None
        while b5:
            if b1 < b5.b1:
                b13 = b5
                b5 = b5.b2
            elif b1 > b5.b1:
                b5 = b5.b3
            else:
                if b5.b3:
                    b13 = b5.b3
                    while b13.b2:
                        b13 = b13.b2
                break
        if b13:
            print(f"In-order b13 of {b1} is {b13.b1}")
            return b13.b1
        else:
            print(f"No b13 found for {b1}")
            return None
    def fonk11(self):
        return self.b4