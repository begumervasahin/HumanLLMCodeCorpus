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
        if not self.b4:
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
        if not self.b4:
            print("No Tree")
            return
        print("\nLevel Order:")
        b9 = [self.b4]
        while b9:
            b10 = len(b9)
            for _ in range(b10):
                b5 = b9.pop(0)
                if b5.b2:
                    b9.append(b5.b2)
                if b5.b3:
                    b9.append(b5.b3)
                print(b5.b1, b7 = " ")
            print()
    def fonk6(self, b1, b11 = False):
        b5 = self.b4
        b6 = None
        while b5:
            if b5.b1 = = b1:
                print(f"{b1} b18!")
                return b6 if b11 else True
            b6 = b5
            if b1 < b5.b1:
                b5 = b5.b2
            else:
                b5 = b5.b3
        print(f"{b1} not present")
        return None if b11 else False
    def fonk7(self, b1):
        b6 = self.fonk6(b1, b11=True)
        if b6 is None and (not self.b4 or self.b4.b1 != b1):
            print("class1 to be deleted not b18!")
            return False
        b12 = self.b4 if b6 is None else (b6.b2 if b1 < b6.b1 else b6.b3)
        b13 = b6 is not None and b1 < b6.b1
        if b12.b2 is None or b12.b3 is None:
            b14 = b12.b2 if b12.b2 else b12.b3
            if b6:
                if b13:
                    b6.b2 = b14
                else:
                    b6.b3 = b14
            else:
                self.b4 = b14
            return
        b15 = b12
        b16 = b12.b3
        while b16.b2:
            b15 = b16
            b16 = b16.b2
        b12.b1, b16.b1 = b16.b1, b12.b1
        if b15.b2 = = b16:
            b15.b2 = b16.b3
        else:
            b15.b3 = b16.b3
    def fonk8(self, b17):
        b8 = []
        b5 = self.b4
        while True:
            while b5:
                b8.append(b5)
                b5 = b5.b2
            if not b8:
                break
            b5 = b8.pop()
            b17 -= 1
            if b17 = = 0:
                print(b5.b1)
                return
            b5 = b5.b3
    def fonk9(self, b17):
        b5 = self.b4
        b16 = None
        b18 = False
        while b5:
            if b17 = = b5.b1:
                b18 = True
                break
            elif b17 < b5.b1:
                b16 = b5
                b5 = b5.b2
            else:
                b5 = b5.b3
        if not b18:
            print("Element not b18")
            return False
        if b5.b3:
            b5 = b5.b3
            while b5.b2:
                b5 = b5.b2
            return b5.b1
        if b16:
            return b16.b1
        print("Last class1, no b16 present!")
        return False
    def fonk10(self):
        return self.b4