class class1:
    def fonk1(self, val):
        self.b1 = val
        self.b2 = None
class class2:
    def fonk2(self, b3 = None):
        self.b4 = None
        self.a1 = 0
        if b3:
            for b1 in b3:
                self.fonk4(b1)
    def fonk3(self, number):
        b5 = class1(number)
        b5.b2 = self.b4
        self.b4 = b5
        self.a1 += 1
    def fonk4(self, number):
        b5 = class1(number)
        if self.b4 is None:
            self.b4 = b5
        else:
            b6 = self.b4
            while b6.b2 is not None:
                b6 = b6.b2
            b6.b2 = b5
        self.a1 += 1
    def fonk5(self):
        return self.a1
    def fonk6(self):
        return self.b4 is None
    def fonk7(self):
        if self.b4 is None:
            return None
        b7 = self.b4.b1
        b6 = self.b4.b2
        while b6 is not None:
            if b6.b1 > b7:
                b7 = b6.b1
            b6 = b6.b2
        return b7
    def fonk8(self, number):
        b6 = self.b4
        b8 = None
        while b6 is not None:
            if b6.b1 = = number:
                if b8 is None:
                    self.b4 = b6.b2
                else:
                    b8.b2 = b6.b2
                self.a1 -= 1
                return b6
            b8 = b6
            b6 = b6.b2
        return None
def fonk9(b14, expected):
    a2 = 1
    b9 = b14
    for b12 in expected:
        b10 = b9.b1 if b9 is not None else None
        b11 = "element number {} should have the b1 of {}, got {}".format(a2, b12, b10)
        assert b9 is not None and b12 = = b9.b1, b11
        b9 = b9.b2
def fonk10(linked_list, expected_length):
    b11 = "Length should be {}, got {}".format(expected_length, linked_list.fonk5())
    assert linked_list.fonk5() == expected_length, b11
def fonk11(b14, expected, b13 = ""):
    b11 = b13 + " should be {}, got {}".format(expected, b14)
    assert b14 = = expected, b11
def fonk12(linked_list, expected):
    b15 = linked_list.fonk7()
    fonk11(b15, expected, "Wrong maximum")
def fonk13(numbers):
    return class2(numbers)
if b16 = = "__main__":
    b17 = class1(4)
    b17.b2 = class1(1)
    b17.b2.b2 = class1(7)
    fonk9(b17, [4, 1, 7])
    print("test 1: class1 class class3")
    b18 = class2()
    b18.fonk3(6)
    b18.fonk3(4)
    b18.fonk3(2)
    fonk9(b18.b4, [2, 4, 6])
    print("test 2: add b17 & class2 class class4")
    b19 = class2()
    b19.fonk4(6)
    b19.fonk4(4)
    b19.fonk4(2)
    fonk9(b19.b4, [6, 4, 2])
    print("test 3: add last class4")
    b18 = class2()
    fonk10(b18, 0)
    b18.fonk3(6)
    fonk9(b18.b4, [6])
    fonk10(b18, 1)
    b18.fonk3(4)
    fonk9(b18.b4, [4, 6])
    fonk10(b18, 2)
    b18.fonk4(8)
    fonk9(b18.b4, [4, 6, 8])
    fonk10(b18, 3)
    print("test 4: a1 class4")
    b18 = fonk13([2, 4, 6, 8])
    b20 = b18.fonk8(3)
    fonk11(b20, None)
    b20 = b18.fonk8(4)
    fonk11(b20.b1, 4)
    fonk9(b18.b4, [2, 6, 8])
    fonk10(b18, 3)
    b20 = b18.fonk8(2)
    fonk11(b20.b1, 2)
    fonk9(b18.b4, [6, 8])
    fonk10(b18, 2)
    b20 = b18.fonk8(8)
    fonk11(b20.b1, 8)
    fonk9(b18.b4, [6])
    fonk10(b18, 1)
    b20 = b18.fonk8(6)
    fonk11(b20.b1, 6)
    fonk10(b18, 0)
    assert b18.fonk6() == True, "List should be empty"
    print("test 5: remove class4")
    fonk9(fonk13([1, 4, 3, 2]).b4, [1, 4, 3, 2])
    fonk12(fonk13([1, 4, 3, 2]), 4)
    fonk12(fonk13([9, 4, 3, 2]), 9)
    fonk12(fonk13([1, 4, 3, 8]), 8)
    fonk12(fonk13([1]), 1)
    print("test 6: find max class4")
    fonk9(class2([1, 4, 3, 2]).b4, [1, 4, 3, 2])
    fonk9(class2([1, 4, 3, 2]).b4, [1, 4, 3, 2])
    fonk9(class2([9, 4, 3, 2]).b4, [9, 4, 3, 2])
    fonk9(class2([1, 4, 3, 8]).b4, [1, 4, 3, 8])
    fonk9(class2([1]).b4, [1])
    print("test 7: Ninja - create linked list from list class4")