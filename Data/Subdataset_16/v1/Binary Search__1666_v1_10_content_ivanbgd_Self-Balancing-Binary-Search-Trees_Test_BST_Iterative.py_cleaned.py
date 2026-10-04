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
            child.b4 = self
    def fonk4(self, child):
        self.b3 = child
        if child:
            child.b4 = self
    def fonk5(self):
        b5 = self.b4.b1 if self.b4 else None
        print(f"class1 {self.b1}: Parent {b5}, Left Child {self.b2.b1 if self.b2 else None}, Right Child {self.b3.b1 if self.b3 else None}")
class class2:
    def fonk6(self, b6):
        self.b6 = b6
    def fonk7(self, b1):
        b7 = class1(b1)
        b8 = self.b6
        while True:
            if b1 < b8.b1:
                if b8.b2 is None:
                    b8.fonk3(b7)
                    break
                b8 = b8.b2
            else:
                if b8.b3 is None:
                    b8.fonk4(b7)
                    break
                b8 = b8.b3
    def fonk8(self, b1):
        b8 = self.b6
        while b8 and b8.b1 != b1:
            if b1 < b8.b1:
                b8 = b8.b2
            else:
                b8 = b8.b3
        return b8
    def fonk9(self, b13):
        def fonk10(b9, b7):
            if b9.b4 is None:
                self.b6 = b7
            elif b9 = = b9.b4.b2:
                b9.b4.b2 = b7
            else:
                b9.b4.b3 = b7
            if b7:
                b7.b4 = b9.b4
        if b13.b2 is None:
            fonk10(b13, b13.b3)
        elif b13.b3 is None:
            fonk10(b13, b13.b2)
        else:
            b10 = self.fonk11(b13.b3)
            if b10.b4 != b13:
                fonk10(b10, b10.b3)
                b10.b3 = b13.b3
                b10.b3.b4 = b10
            fonk10(b13, b10)
            b10.b2 = b13.b2
            b10.b2.b4 = b10
    def fonk11(self, b13):
        b8 = b13
        while b8.b2 is not None:
            b8 = b8.b2
        return b8
    def fonk12(self):
        def fonk13(b13):
            return fonk13(b13.b2) + [b13.b1] + fonk13(b13.b3) if b13 else []
        return fonk13(self.b6)
    def fonk14(self):
        def fonk15(b13):
            return [b13.b1] + fonk15(b13.b2) + fonk15(b13.b3) if b13 else []
        return fonk15(self.b6)
    def fonk16(self):
        def fonk17(b13):
            return fonk17(b13.b2) + fonk17(b13.b3) + [b13.b1] if b13 else []
        return fonk17(self.b6)
    def fonk18(self):
        b11 = [self.b6]
        b12 = []
        while b11:
            b13 = b11.pop(0)
            b12.append(b13.b1)
            if b13.b2:
                b11.append(b13.b2)
            if b13.b3:
                b11.append(b13.b3)
        return b12
    def fonk19(self, b13):
        b14 = b13.b3
        if b14:
            b13.fonk4(b14.b2)
            if b13.b4 is None:
                self.b6 = b14
            elif b13 = = b13.b4.b2:
                b13.b4.fonk3(b14)
            else:
                b13.b4.fonk4(b14)
            b14.fonk3(b13)
    def fonk20(self, b13):
        b14 = b13.b2
        if b14:
            b13.fonk3(b14.b3)
            if b13.b4 is None:
                self.b6 = b14
            elif b13 = = b13.b4.b3:
                b13.b4.fonk4(b14)
            else:
                b13.b4.fonk3(b14)
            b14.fonk4(b13)
    def fonk21(self):
        return self.b6
    def fonk22(self, low, high):
        def fonk23(b13, low, high):
            if not b13:
                return []
            b12 = []
            if low <= b13.b1 <= high:
                b12.append(b13.b1)
            if low < b13.b1:
                b12 += fonk23(b13.b2, low, high)
            if b13.b1 < high:
                b12 += fonk23(b13.b3, low, high)
            return b12
        return fonk23(self.b6, low, high)
def fonk24(b17, b15 = False):
    print()
    print("In order:  ", b17.fonk12())
    print("Pre order: ", b17.fonk14())
    print("BFS:       ", b17.fonk18())
    if b15:
        print("Nodes (in BFS order):")
        b16 = b17.fonk18()
        for node_key in b16:
            b17.fonk8(node_key).fonk5()
    print()
def fonk25():
    b17 = class2(class1(7))
    b17.fonk7(4)
    b17.fonk7(1)
    b17.fonk7(6)
    b17.fonk7(13)
    b17.fonk7(15)
    b17.fonk7(10)
    return b17, b17.fonk21()
def fonk26():
    b17, b6 = fonk25()
    print("\nPrint:")
    print("In order:  ", b17.fonk12())
    print("Pre order: ", b17.fonk14())
    print("Post order:", b17.fonk16())
    print("BFS:       ", b17.fonk18())
    print("Root:", b18 = ' ')
    b6.fonk5()
    print("\nFind:")
    for i in [0, 1, 2, 5, 6, 7, 8, 12, 13, 14, 15, 20]:
        b19 = b17.fonk8(i)
        print(i, b19.b1 if b19 else None)
    print("\nNext:")
    for i in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        b19 = b17.fonk8(i)
        b20 = b17.fonk8(i + 1)
        print(i, b20.b1 if b20 else None)
    print("\nPrevious:")
    for i in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        b19 = b17.fonk8(i)
        b21 = b17.fonk8(i - 1)
        print(i, b21.b1 if b21 else None)
    print("\nRange search:")
    for b13 in b17.fonk22(5, 12):
        print(b13, b18 = ' ')
    print()
    if 0:
        print("\nInsert:")
        print("In order:  ", b17.fonk12())
        print("Pre order: ", b17.fonk14())
        print("BFS:       ", b17.fonk18())
        a1 = 3
        b17.fonk7(a1)
        b13 = b17.fonk8(a1)
        b13.fonk5()
        b13.getParent().fonk5()
        print("Inserting", a1)
        print("In order:  ", b17.fonk12())
        print("Pre order: ", b17.fonk14())
        print("BFS:       ", b17.fonk18())
    if 0:
        print("\nDelete:")
        print("In order:  ", b17.fonk12())
        print("Pre order: ", b17.fonk14())
        print("BFS:       ", b17.fonk18())
        a1 = 7
        b17.fonk9(b17.fonk8(a1))
        print("Deleting", a1)
        print("In order:  ", b17.fonk12())
        print("Pre order: ", b17.fonk14())
        print("BFS:       ", b17.fonk18())
        print("This is the b13 under which the deleted b13, {}, would come: {}.".format(a1, b17.fonk8(a1)))
        b17.fonk8(a1).fonk5()
        try:
            b17.fonk8(a1).getParent().fonk5()
        except:
            print("New b6:", b18 = ' ')
            b17.fonk8(b6.b1).fonk5()
        print("Root is:", b18 = ' ')
        b17.fonk21().fonk5()
    print("\nRotate b3:")
    fonk24(b17, True)
    a1 = 7
    b17.fonk20(b17.fonk8(a1))
    print("Rotating b3", a1)
    fonk24(b17, True)
    b17.fonk8(a1).fonk5()
    print("\nRotate b2:")
    fonk24(b17, True)
    a1 = 1
    b17.fonk19(b17.fonk8(a1))
    print("Rotating b2", a1)
    fonk24(b17, True)
    b17.fonk8(a1).fonk5()
def fonk27():
    b17 = class2(class1(3))
    b17.fonk7(1)
    b17.fonk7(4)
    b17.fonk7(5)
    fonk24(b17, True)
    b17.fonk9(b17.fonk8(3))
    fonk24(b17, True)
def fonk28():
    b17, b6 = fonk25()
    fonk24(b17, True)
    b17.fonk9(b17.fonk8(7))
    fonk24(b17, True)
fonk26()