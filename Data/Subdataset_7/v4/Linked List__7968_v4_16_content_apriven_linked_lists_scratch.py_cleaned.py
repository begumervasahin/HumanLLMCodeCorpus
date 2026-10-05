class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self, b1):
        b5 = self.b3
        if b5 is None:
            self.b3 = class1(b1)
            return
        while b5.b2:
            b5 = b5.b2
        b5.b2 = class1(b1)
    def fonk5(self):
        a1 = 0
        b5 = self.b3
        while b5:
            a1 += 1
            b5 = b5.b2
        return a1
    def fonk6(self):
        return self.b3 is None
    def fonk7(self):
        if self.fonk6():
            return None
        b5 = self.b3
        b6 = b5.b1
        while b5:
            if b5.b1 > b6:
                b6 = b5.b1
            b5 = b5.b2
        return b6
    def fonk8(self, b1):
        if self.fonk6():
            return None
        if self.b3.b1 = = b1:
            b7 = self.b3
            self.b3 = self.b3.b2
            return b7
        b5 = self.b3
        while b5.b2:
            if b5.b2.b1 = = b1:
                b7 = b5.b2
                b5.b2 = b5.b2.b2
                return b7
            b5 = b5.b2
        return None
def fonk9(b13, expected):
    a2 = 1
    b8 = b13
    for b11 in expected:
        b9 = b8.b1 if b8 else None
        b10 = f"Element b1 {a2} should have the value of {b11}, got {b9}"
        assert b8 and b11 = = b8.b1, b10
        b8 = b8.b2
        a2 += 1
def fonk10(linked_list, expected_length):
    assert linked_list.fonk5() == expected_length, f"Length should be {expected_length}, got {linked_list.fonk5()}"
def fonk11(b13, expected, b12 = ""):
    assert b13 = = expected, f"{b12} should be {expected}, got {b13}"
def fonk12(linked_list, expected):
    b6 = linked_list.fonk7()
    fonk11(b6, expected, "Wrong maximum")
def fonk13(numbers):
    b14 = class2()
    for b1 in numbers:
        b14.fonk4(b1)
    return b14
if b15 = = "__main__":
    b16 = class1(4)
    b16.b2 = class1(1)
    b16.b2.b2 = class1(7)
    fonk9(b16, [4, 1, 7])
    print("Test 1: class1 class class3")
    b17 = class2()
    b17.fonk3(6)
    b17.fonk3(4)
    b17.fonk3(2)
    fonk9(b17.b3, [2, 4, 6])
    print("Test 2: add b16 & class2 class class4")
    b18 = class2()
    b18.fonk4(6)
    b18.fonk4(4)
    b18.fonk4(2)
    fonk9(b18.b3, [6, 4, 2])
    print("Test 3: add last class4")
    b17 = class2()
    fonk10(b17, 0)
    b17.fonk3(6)
    fonk9(b17.b3, [6])
    fonk10(b17, 1)
    b17.fonk3(4)
    fonk9(b17.b3, [4, 6])
    fonk10(b17, 2)
    b17.fonk4(8)
    fonk9(b17.b3, [4, 6, 8])
    fonk10(b17, 3)
    print("Test 4: a1 class4")
    b17 = fonk13([2, 4, 6, 8])
    b7 = b17.fonk8(3)
    fonk11(b7, None)
    b7 = b17.fonk8(4)
    fonk11(b7.b1, 4)
    fonk9(b17.b3, [2, 6, 8])
    fonk10(b17, 3)
    b7 = b17.fonk8(2)
    fonk11(b7.b1, 2)
    fonk9(b17.b3, [6, 8])
    fonk10(b17, 2)
    b7 = b17.fonk8(8)
    fonk11(b7.b1, 8)
    fonk9(b17.b3, [6])
    fonk10(b17, 1)
    b7 = b17.fonk8(6)
    fonk11(b7.b1, 6)
    fonk10(b17, 0)
    assert b17.fonk6(), "List should be empty"
    print("Test 5: remove class4")
    fonk9(fonk13([1,4,3,2]).b3, [1,4,3,2])
    fonk12(fonk13([1,4,3,2]), 4)
    fonk12(fonk13([9,4,3,2]), 9)
    fonk12(fonk13([1,4,3,8]), 8)
    fonk12(fonk13([1]), 1)
    print("Test 6: find max class4")
    fonk9(fonk13([1,4,3,2]).b3, [1,4,3,2])
    fonk9(fonk13([1,4,3,2]).b3, [1,4,3,2])
    fonk9(fonk13([9,4,3,2]).b3, [9,4,3,2])
    fonk9(fonk13([1,4,3,8]).b3, [1,4,3,8])
    fonk9(fonk13([1]).b3, [1])
    print("Test 7: Ninja - create linked list from list class4")