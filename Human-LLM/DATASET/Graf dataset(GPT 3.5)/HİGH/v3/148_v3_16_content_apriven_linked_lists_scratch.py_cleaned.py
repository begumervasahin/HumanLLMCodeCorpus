class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.a1 = 0
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
        self.a1 += 1
    def fonk4(self, b1):
        if not self.b3:
            self.fonk3(b1)
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = class1(b1)
            self.a1 += 1
    def fonk5(self):
        return self.a1
    def fonk6(self):
        return self.a1 = = 0
    def fonk7(self):
        if self.fonk6():
            return None
        b6 = self.b3.b1
        b5 = self.b3.b2
        while b5:
            if b5.b1 > b6:
                b6 = b5.b1
            b5 = b5.b2
        return b6
    def fonk8(self, b1):
        if self.b3.b1 = = b1:
            b7 = self.b3
            self.b3 = self.b3.b2
            self.a1 -= 1
            return b7
        b5 = self.b3
        while b5.b2:
            if b5.b2.b1 = = b1:
                b7 = b5.b2
                b5.b2 = b5.b2.b2
                self.a1 -= 1
                return b7
            b5 = b5.b2
        return None
def fonk9(b11, expected):
    a2 = 1
    b8 = b11
    for b9 in expected:
        assert b8 is not None and b9 = = b8.b1, f"Element b1 {a2} should have the value of {b9}, got {b8.b1}"
        b8 = b8.b2
        a2 += 1
def fonk10(linked_list, expected_length):
    assert linked_list.fonk5() == expected_length, f"Length should be {expected_length}, got {linked_list.fonk5()}"
def fonk11(linked_list, expected):
    assert linked_list.fonk7() == expected, f"Wrong maximum, should be {expected}"
def fonk12(b11, expected, b10 = ""):
    assert b11 = = expected, f"{b10}, should be {expected}, got {b11}"
def fonk13(numbers):
    b12 = class2()
    for b9 in numbers:
        b12.fonk4(b9)
    return b12
if b13 = = "__main__":
    b14 = class1(4)
    b14.b2 = class1(1)
    b14.b2.b2 = class1(7)
    fonk9(b14, [4, 1, 7])
    print("Test 1: class1 class class3")
    b15 = class2()
    b15.fonk3(6)
    b15.fonk3(4)
    b15.fonk3(2)
    fonk9(b15.b3, [2, 4, 6])
    print("Test 2: Add b14 & class2 class class4")
    b16 = class2()
    b16.fonk4(6)
    b16.fonk4(4)
    b16.fonk4(2)
    fonk9(b16.b3, [6, 4, 2])
    print("Test 3: Add last class4")
    b15 = class2()
    fonk10(b15, 0)
    b15.fonk3(6)
    fonk9(b15.b3, [6])
    fonk10(b15, 1)
    b15.fonk3(4)
    fonk9(b15.b3, [4, 6])
    fonk10(b15, 2)
    b15.fonk4(8)
    fonk9(b15.b3, [4, 6, 8])
    fonk10(b15, 3)
    print("Test 4: Length class4")
    b15 = fonk13([2, 4, 6, 8])
    b7 = b15.fonk8(3)
    fonk12(b7, None)
    b7 = b15.fonk8(4)
    fonk12(b7.b1, 4)
    fonk9(b15.b3, [2, 6, 8])
    fonk10(b15, 3)
    b7 = b15.fonk8(2)
    fonk12(b7.b1, 2)
    fonk9(b15.b3, [6, 8])
    fonk10(b15, 2)
    b7 = b15.fonk8(8)
    fonk12(b7.b1, 8)
    fonk9(b15.b3, [6])
    fonk10(b15, 1)
    b7 = b15.fonk8(6)
    fonk12(b7.b1, 6)
    fonk10(b15, 0)
    assert b15.fonk6() == True, "List should be empty"
    print("Test 5: Remove class4")
    fonk9(fonk13([1, 4, 3, 2]).b3, [1, 4, 3, 2])
    fonk11(fonk13([1, 4, 3, 2]), 4)
    fonk11(fonk13([9, 4, 3, 2]), 9)
    fonk11(fonk13([1, 4, 3, 8]), 8)
    fonk11(fonk13([1]), 1)
    print("Test 6: Find max class4")