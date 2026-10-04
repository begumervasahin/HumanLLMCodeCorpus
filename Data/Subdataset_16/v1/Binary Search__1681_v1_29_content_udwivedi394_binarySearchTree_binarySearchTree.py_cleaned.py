class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b1):
        if self.b4 is None:
            self.b4 = class1(b1)
            return
        b5 = self.b4
        while b5:
            b6 = b5
            if b1 < b5.b1:
                b5 = b5.b2
            else:
                b5 = b5.b3
        if b1 < b6.b1:
            b6.b2 = class1(b1)
        else:
            b6.b3 = class1(b1)
    def fonk4(self):
        if self.b4 is None:
            print("Nothing to print")
            return
        print("\nIn Order:", b7 = " ")
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            if not b8:
                break
            b5 = b8.pop()
            print(b5.b1, b7 = " ")
            b5 = b5.b3
        print()
    def fonk5(self):
        if self.b4 is None:
            print("No Tree")
            return
        print("\nLevel Order:")
        b9 = []
        b5 = self.b4
        b9.append(b5)
        while b9:
            b10 = len(b9)
            while b10:
                b5 = b9.pop(0)
                if b5.b2:
                    b9.append(b5.b2)
                if b5.b3:
                    b9.append(b5.b3)
                print(b5.b1, b7 = " ")
                b10 -= 1
            print()
    def fonk6(self, b1, b11 = False):
        b5 = self.b4
        b6 = None
        while b5:
            if b5.b1 = = b1:
                print(f"{b1} b15!")
                if b11:
                    return b6
                return True
            b6 = b5
            if b1 < b5.b1:
                b5 = b5.b2
            else:
                b5 = b5.b3
        print(f"{b1} not present")
        if b11:
            return None
        return False
    def fonk7(self, b1):
        b6 = self.fonk6(b1, True)
        if b6 is None and (self.b4 is None or self.b4.b1 != b1):
            print("class1 to be deleted not b15!")
            return False
        b2 = True
        if b6 is None:
            b12 = self.b4
        elif b1 < b6.b1:
            b12 = b6.b2
        else:
            b12 = b6.b3
            b2 = False
        if b12 and (b12.b2 is None or b12.b3 is None):
            if b2:
                b6.b2 = b12.b2 if b12.b2 else b12.b3
            else:
                b6.b3 = b12.b2 if b12.b2 else b12.b3
            return
        if b6 is None:
            if b12.b2 is None and b12.b3 is None:
                self.b4 = None
            elif b12.b2 is None:
                self.b4 = b12.b3
            elif b12.b3 is None:
                self.b4 = b12.b2
            return
        b5 = b12.b3
        b6 = b12
        while b5 and b5.b2:
            b6 = b5
            b5 = b5.b2
        b12.b1, b5.b1 = b5.b1, b12.b1
        if b6.b2 = = b5:
            b6.b2 = b5.b3
        else:
            b6.b3 = b5.b3
    def fonk8(self, b13):
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            if not b8:
                break
            b5 = b8.pop()
            b13 -= 1
            if b13 = = 0:
                print(b5.b1)
                return
            b5 = b5.b3
    def fonk9(self, b13):
        b5 = self.b4
        b14 = None
        b15 = False
        while b5:
            if b13 = = b5.b1:
                b15 = True
                break
            elif b13 < b5.b1:
                b14 = b5
                b5 = b5.b2
            else:
                b5 = b5.b3
        if not b15:
            print("Element not b15")
            return False
        if b14 is None:
            print("Last class1, no b14 present!")
            return False
        if b5.b3:
            b5 = b5.b3
            while b5.b2:
                b5 = b5.b2
            return b5.b1
        return b14.b1
    def fonk10(self):
        return self.b4
if b16 = = "__main__":
    b17 = class2()
    b17.fonk3(10)
    b17.fonk3(5)
    b17.fonk3(20)
    b17.fonk3(15)
    b17.fonk3(25)
    b17.fonk4()
    b17.fonk5()
    b17.fonk6(15)
    b17.fonk8(3)
    b14 = b17.fonk9(15)
    if b14:
        print(f"In-order b14 of 15: {b14}")
    b17.fonk7(20)
    b17.fonk5()