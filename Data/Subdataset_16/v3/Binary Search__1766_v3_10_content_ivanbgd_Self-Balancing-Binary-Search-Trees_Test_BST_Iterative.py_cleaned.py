class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
    def fonk2(self, b4):
        self.b4 = b4
    def fonk3(self, child):
        self.b2 = child
        if child:
            child.fonk2(self)
    def fonk4(self, child):
        self.b3 = child
        if child:
            child.fonk2(self)
    def fonk5(self):
        b5 = self.b4.b1 if self.b4 else None
        b6 = self.b2.b1 if self.b2 else None
        b7 = self.b3.b1 if self.b3 else None
        print(f"class1 {self.b1}: Parent {b5}, Left Child {b6}, Right Child {b7}")
class class2:
    def fonk6(self, b8):
        self.b8 = b8
    def fonk7(self, b1):
        b9 = class1(b1)
        b10 = self.b8
        while True:
            if b1 < b10.b1:
                if b10.b2 is None:
                    b10.fonk3(b9)
                    break
                b10 = b10.b2
            else:
                if b10.b3 is None:
                    b10.fonk4(b9)
                    break
                b10 = b10.b3
    def fonk8(self, b1):
        b10 = self.b8
        while b10 and b10.b1 != b1:
            b10 = b10.b2 if b1 < b10.b1 else b10.b3
        return b10
    def fonk9(self, b15):
        def fonk10(b11, b9):
            if b11.b4 is None:
                self.b8 = b9
            elif b11 = = b11.b4.b2:
                b11.b4.fonk3(b9)
            else:
                b11.b4.fonk4(b9)
            if b9:
                b9.fonk2(b11.b4)
        if b15.b2 is None:
            fonk10(b15, b15.b3)
        elif b15.b3 is None:
            fonk10(b15, b15.b2)
        else:
            b12 = self.fonk11(b15.b3)
            if b12.b4 != b15:
                fonk10(b12, b12.b3)
                b12.fonk4(b15.b3)
            fonk10(b15, b12)
            b12.fonk3(b15.b2)
    def fonk11(self, b15):
        b10 = b15
        while b10.b2 is not None:
            b10 = b10.b2
        return b10
    def fonk12(self):
        def fonk13(b15):
            return fonk13(b15.b2) + [b15.b1] + fonk13(b15.b3) if b15 else []
        return fonk13(self.b8)
    def fonk14(self):
        def fonk15(b15):
            return [b15.b1] + fonk15(b15.b2) + fonk15(b15.b3) if b15 else []
        return fonk15(self.b8)
    def fonk16(self):
        def fonk17(b15):
            return fonk17(b15.b2) + fonk17(b15.b3) + [b15.b1] if b15 else []
        return fonk17(self.b8)
    def fonk18(self):
        b13 = [self.b8]
        b14 = []
        while b13:
            b15 = b13.pop(0)
            b14.append(b15.b1)
            if b15.b2:
                b13.append(b15.b2)
            if b15.b3:
                b13.append(b15.b3)
        return b14
    def fonk19(self, b15):
        b16 = b15.b3
        if b16:
            b15.fonk4(b16.b2)
            if b15.b4 is None:
                self.b8 = b16
            elif b15 = = b15.b4.b2:
                b15.b4.fonk3(b16)
            else:
                b15.b4.fonk4(b16)
            b16.fonk3(b15)
    def fonk20(self, b15):
        b16 = b15.b2
        if b16:
            b15.fonk3(b16.b3)
            if b15.b4 is None:
                self.b8 = b16
            elif b15 = = b15.b4.b3:
                b15.b4.fonk4(b16)
            else:
                b15.b4.fonk3(b16)
            b16.fonk4(b15)
    def fonk21(self, low, high):
        def fonk22(b15, low, high):
            if not b15:
                return []
            b14 = []
            if low <= b15.b1 <= high:
                b14.append(b15.b1)
            if low < b15.b1:
                b14 += fonk22(b15.b2, low, high)
            if b15.b1 < high:
                b14 += fonk22(b15.b3, low, high)
            return b14
        return fonk22(self.b8, low, high)
def fonk23(b18, b17 = False):
    print("\nIn order:  ", b18.fonk12())
    print("Pre order: ", b18.fonk14())
    print("BFS:       ", b18.fonk18())
    if b17:
        print("Nodes (in BFS order):")
        for node_key in b18.fonk18():
            b18.fonk8(node_key).fonk5()
    print()
def fonk24():
    b18 = class2(class1(7))
    b18.fonk7(4)
    b18.fonk7(1)
    b18.fonk7(6)
    b18.fonk7(13)
    b18.fonk7(15)
    b18.fonk7(10)
    return b18, b18.b8
def fonk25():
    b18, b8 = fonk24()
    print("\nTraversal Orders:")
    print("In order:  ", b18.fonk12())
    print("Pre order: ", b18.fonk14())
    print("Post order:", b18.fonk16())
    print("BFS:       ", b18.fonk18())
    print("Root b15:", b19 = ' ')
    b8.fonk5()
    print("\nFind nodes:")
    for i in [0, 1, 2, 5, 6, 7, 8, 12, 13, 14, 15, 20]:
        b20 = b18.fonk8(i)
        print(f"class1 {i}: {'Found' if b20 else 'Not b20'} (Key: {b20.b1 if b20 else 'N/A'})")
    print("\nRange search results (5 to 12):")
    print("Nodes in range:", b18.fonk21(5, 12))
    print("\nRotations:")
    print("Initial tree:")
    fonk23(b18, True)
    print("Rotating b3 around b15 7:")
    b18.fonk20(b18.fonk8(7))
    fonk23(b18, True)
    print("Rotating b2 around b15 1:")
    b18.fonk19(b18.fonk8(1))
    fonk23(b18, True)
def fonk26():
    b18 = class2(class1(3))
    b18.fonk7(1)
    b18.fonk7(4)
    b18.fonk7(5)
    fonk23(b18, True)
    b18.fonk9(b18.fonk8(3))
    fonk23(b18, True)
def fonk27():
    b18, b21 = fonk24()
    fonk23(b18, True)
    b18.fonk9(b18.fonk8(7))
    fonk23(b18, True)
if b22 = = '__main__':
    fonk25()