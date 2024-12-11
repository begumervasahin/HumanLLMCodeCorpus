class class1(object):
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        return None
class class2(object):
    def fonk2(self):
        self.b3 = None
        return None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
        return None
    def fonk4(self, b1):
        b5 = self.b3
        if b5 is None:
            self.b3 = class1(b1)
            return None
        while b5.b2 != None:
            b5 = b5.b2
        b5.b2 = class1(b1)
        return None
    def fonk5(self):
        return None
    def fonk6(self):
        return None
    def fonk7(self, b6 = None):
        return None
    def fonk8(self, b1):
        return None
def fonk9(b12, expected):
    a1 = 1
    b7 = b12
    for b6 in expected:
        b8 = b7.b1 if b7 is not None else None
        b9 = "element b1 {} should have the value of {}, got {}".format(
            a1, b6, b8)
        assert b7 is not None and b6 = = b7.b1, b9
        b7 = b7.b2
def fonk10(linked_list, expected_length):
    b9 = "Length should be {}, got {}".format(expected_length, linked_list.b10)
    assert linked_list.b10 = = expected_length, b9
def fonk11(b12, expected, b11 = ""):
    b9 = b11 + " should be {}, got {}".format(expected, b12)
    assert b12 = = expected, b9
def fonk12(linked_list, expected):
    b13 = linked_list.fonk7()
    fonk11(b13, expected, "Wrong maximum")
def fonk13(numbers):
    b14 = class2()
    for b6 in numbers:
        b14.fonk4(b6)
    return b14
if b15 = = "__main__":
    b16 = class1(4)
    b16.b2 = class1(1)
    b16.b2.b2 = class1(7)
    fonk9(b16, [4, 1, 7])
    print("test 1: class1 class class3")
    b17 = class2()
    b17.fonk3(6)
    b17.fonk3(4)
    b17.fonk3(2)
    fonk9(b17.b3, [2, 4, 6])
    print("test 2: add b16 & class2 class class4")
    b18 = class2()
    b18.fonk4(6)
    b18.fonk4(4)
    b18.fonk4(2)
    fonk9(b18.b3, [6, 4, 2])
    print("test 3: add last class4")
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
    print("test 4: b10 class4")
    b17 = fonk13([2, 4, 6, 8])
    b19 = b17.fonk8(3)
    fonk11(b19, None)
    b19 = b17.fonk8(4)
    fonk11(b19.b1, 4)
    fonk9(b17.b3, [2, 6, 8])
    fonk10(b17, 3)
    b19 = b17.fonk8(2)
    fonk11(b19.b1, 2)
    fonk9(b17.b3, [6, 8])
    fonk10(b17, 2)
    b19 = b17.fonk8(8)
    fonk11(b19.b1, 8)
    fonk9(b17.b3, [6])
    fonk10(b17, 1)
    b19 = b17.fonk8(6)
    fonk11(b19.b1, 6)
    fonk10(b17, 0)
    assert b17.fonk6() == True, "List should be empty"
    print("test 5: remove class4")
    fonk9(fonk13([1,4,3,2]).b3, [1,4,3,2])
    fonk12(fonk13([1,4,3,2]), 4)
    fonk12(fonk13([9,4,3,2]), 9)
    fonk12(fonk13([1,4,3,8]), 8)
    fonk12(fonk13([1]), 1)
    print("test 6: find b13 class4")
    fonk9(class2([1,4,3,2]).b3, [1,4,3,2])
    fonk9(class2([1,4,3,2]).b3, [1,4,3,2])
    fonk9(class2([9,4,3,2]).b3, [9,4,3,2])
    fonk9(class2([1,4,3,8]).b3, [1,4,3,8])
    fonk9(class2([1]).b3, [1])
    print("test 7: Ninja - create linked b14 from b14 class4")