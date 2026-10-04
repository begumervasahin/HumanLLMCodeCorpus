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
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = b4
    def fonk5(self):
        b5 = self.b3
        a1 = 0
        while b5:
            a1 += 1
            b5 = b5.b2
        return a1
    def fonk6(self):
        return self.b3 is None
    def fonk7(self):
        if not self.b3:
            return None
        b6 = self.b3.b1
        b5 = self.b3.b2
        while b5:
            if b5.b1 > b6:
                b6 = b5.b1
            b5 = b5.b2
        return b6
    def fonk8(self, b1):
        if not self.b3:
            return None
        if self.b3.b1 = = b1:
            b7 = self.b3
            self.b3 = self.b3.b2
            return b7
        b5 = self.b3
        while b5.b2 and b5.b2.b1 != b1:
            b5 = b5.b2
        if b5.b2:
            b7 = b5.b2
            b5.b2 = b5.b2.b2
            return b7
        return None
def fonk9(b12, expected):
    b8 = b12
    for index, expected_number in enumerate(expected, b9 = 1):
        b10 = b8.b1 if b8 else None
        assert b8 and b10 = = expected_number, (
            f"Element b1 {index} should have the value of {expected_number}, got {b10}"
        )
        b8 = b8.b2
def fonk10(b13, expected_length):
    assert b13.fonk5() == expected_length, (
        f"Length should be {expected_length}, got {b13.fonk5()}"
    )
def fonk11(b12, expected, b11 = ""):
    assert b12 = = expected, f"{b11} should be {expected}, got {b12}"
def fonk12(b13, expected):
    b6 = b13.fonk7()
    fonk11(b6, expected, "Wrong maximum")
def fonk13(numbers):
    b13 = class2()
    for b1 in numbers:
        b13.fonk4(b1)
    return b13
if b14 = = "__main__":
    b15 = class1(4)
    b15.b2 = class1(1)
    b15.b2.b2 = class1(7)
    fonk9(b15, [4, 1, 7])
    print("Test 1: class1 class class3")
    b16 = class2()
    b16.fonk3(6)
    b16.fonk3(4)
    b16.fonk3(2)
    fonk9(b16.b3, [2, 4, 6])
    print("Test 2: add_first & class2 class class4")
    b17 = class2()
    b17.fonk4(6)
    b17.fonk4(4)
    b17.fonk4(2)
    fonk9(b17.b3, [6, 4, 2])
    print("Test 3: add_last class4")
    b16 = class2()
    fonk10(b16, 0)
    b16.fonk3(6)
    fonk9(b16.b3, [6])
    fonk10(b16, 1)
    b16.fonk3(4)
    fonk9(b16.b3, [4, 6])
    fonk10(b16, 2)
    b16.fonk4(8)
    fonk9(b16.b3, [4, 6, 8])
    fonk10(b16, 3)
    print("Test 4: get_length class4")
    b16 = fonk13([2, 4, 6, 8])
    b18 = b16.fonk8(3)
    fonk11(b18, None)
    b18 = b16.fonk8(4)
    fonk11(b18.b1, 4)
    fonk9(b16.b3, [2, 6, 8])
    fonk10(b16, 3)
    b18 = b16.fonk8(2)
    fonk11(b18.b1, 2)
    fonk9(b16.b3, [6, 8])
    fonk10(b16, 2)
    b18 = b16.fonk8(8)
    fonk11(b18.b1, 8)
    fonk9(b16.b3, [6])
    fonk10(b16, 1)
    b18 = b16.fonk8(6)
    fonk11(b18.b1, 6)
    fonk10(b16, 0)
    assert b16.fonk6(), "List should be empty"
    print("Test 5: remove class4")
    fonk9(fonk13([1, 4, 3, 2]).b3, [1, 4, 3, 2])
    fonk12(fonk13([1, 4, 3, 2]), 4)
    fonk12(fonk13([9, 4, 3, 2]), 9)
    fonk12(fonk13([1, 4, 3, 8]), 8)
    fonk12(fonk13([1]), 1)
    print("Test 6: find_max class4")
    fonk9(fonk13([1, 4, 3, 2]).b3, [1, 4, 3, 2])
    fonk9(fonk13([9, 4, 3, 2]).b3, [9, 4, 3, 2])
    fonk9(fonk13([1, 4, 3, 8]).b3, [1, 4, 3, 8])
    fonk9(fonk13([1]).b3, [1])
    print("Test 7: create_list class4")