class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3 = None):
        self.b4 = None
        self.a1 = 0
        if b3:
            for b1 in b3:
                self.fonk4(b1)
    def fonk3(self, b1):
        b5 = class1(b1)
        b5.b2 = self.b4
        self.b4 = b5
        self.a1 += 1
    def fonk4(self, b1):
        b5 = class1(b1)
        if not self.b4:
            self.b4 = b5
        else:
            b6 = self.b4
            while b6.b2:
                b6 = b6.b2
            b6.b2 = b5
        self.a1 += 1
    def fonk5(self):
        return self.a1
    def fonk6(self):
        return self.b4 is None
    def fonk7(self):
        if not self.b4:
            return None
        b7 = self.b4.b1
        b6 = self.b4.b2
        while b6:
            if b6.b1 > b7:
                b7 = b6.b1
            b6 = b6.b2
        return b7
    def fonk8(self, b1):
        b6 = self.b4
        b8 = None
        while b6:
            if b6.b1 = = b1:
                if not b8:
                    self.b4 = b6.b2
                else:
                    b8.b2 = b6.b2
                self.a1 -= 1
                return b6
            b8 = b6
            b6 = b6.b2
        return None
def fonk9(b10, expected):
    b6 = b10
    for index, b1 in enumerate(expected):
        assert b6 is not None and b6.b1 = = b1, f"Element number {index + 1} should be {b1}, got {b6.b1 if b6 else 'None'}"
        b6 = b6.b2
def fonk10(linked_list, expected_length):
    assert linked_list.fonk5() == expected_length, f"Length should be {expected_length}, got {linked_list.fonk5()}"
def fonk11(b10, expected, b9 = ""):
    assert b10 = = expected, f"{b9} should be {expected}, got {b10}"
def fonk12(linked_list, expected):
    b11 = linked_list.fonk7()
    fonk11(b11, expected, "Wrong maximum")
def fonk13(b3):
    return class2(b3)
if b12 = = "__main__":
    b13 = class1(4)
    b13.b2 = class1(1)
    b13.b2.b2 = class1(7)
    fonk9(b13, [4, 1, 7])
    print("Test 1: class1 class class3")
    b14 = class2()
    b14.fonk3(6)
    b14.fonk3(4)
    b14.fonk3(2)
    fonk9(b14.b4, [2, 4, 6])
    fonk10(b14, 3)
    print("Test 2: add_first & class2 class class4")
    b15 = class2()
    b15.fonk4(6)
    b15.fonk4(4)
    b15.fonk4(2)
    fonk9(b15.b4, [6, 4, 2])
    fonk10(b15, 3)
    print("Test 3: add_last class4")
    b14 = class2()
    fonk10(b14, 0)
    b14.fonk3(6)
    fonk9(b14.b4, [6])
    fonk10(b14, 1)
    b14.fonk3(4)
    fonk9(b14.b4, [4, 6])
    fonk10(b14, 2)
    b14.fonk4(8)
    fonk9(b14.b4, [4, 6, 8])
    fonk10(b14, 3)
    print("Test 4: a1 class4")
    b14 = fonk13([2, 4, 6, 8])
    b16 = b14.fonk8(3)
    fonk11(b16, None)
    b16 = b14.fonk8(4)
    fonk11(b16.b1, 4)
    fonk9(b14.b4, [2, 6, 8])
    fonk10(b14, 3)
    b16 = b14.fonk8(2)
    fonk11(b16.b1, 2)
    fonk9(b14.b4, [6, 8])
    fonk10(b14, 2)
    b16 = b14.fonk8(8)
    fonk11(b16.b1, 8)
    fonk9(b14.b4, [6])
    fonk10(b14, 1)
    b16 = b14.fonk8(6)
    fonk11(b16.b1, 6)
    fonk10(b14, 0)
    assert b14.fonk6() is True, "List should be empty"
    print("Test 5: remove class4")
    fonk12(fonk13([1, 4, 3, 2]), 4)
    fonk12(fonk13([9, 4, 3, 2]), 9)
    fonk12(fonk13([1, 4, 3, 8]), 8)
    fonk12(fonk13([1]), 1)
    print("Test 6: find max class4")
    fonk9(fonk13([1, 4, 3, 2]).b4, [1, 4, 3, 2])
    fonk9(fonk13([9, 4, 3, 2]).b4, [9, 4, 3, 2])
    fonk9(fonk13([1, 4, 3, 8]).b4, [1, 4, 3, 8])
    fonk9(fonk13([1]).b4, [1])
    print("Test 7: Create linked list from list class4")