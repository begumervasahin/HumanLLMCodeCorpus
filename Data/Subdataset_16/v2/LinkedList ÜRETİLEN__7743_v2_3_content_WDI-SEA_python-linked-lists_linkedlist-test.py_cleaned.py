class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self):
        return self.b3 is None
    def fonk4(self):
        b4 = self.b3
        a1 = 0
        while b4:
            a1 += 1
            b4 = b4.b2
        return a1
    def fonk5(self):
        b5 = []
        b4 = self.b3
        while b4:
            b5.append(str(b4.b1))
            b4 = b4.b2
        return "[" + " -> ".join(b5) + "]"
    def fonk6(self, b1):
        b6 = class1(b1)
        b6.b2 = self.b3
        self.b3 = b6
    def fonk7(self):
        if self.fonk3():
            return False
        b7 = self.b3
        self.b3 = self.b3.b2
        return b7
    def fonk8(self, b1):
        b6 = class1(b1)
        if self.fonk3():
            self.b3 = b6
            return b6
        b4 = self.b3
        while b4.b2:
            b4 = b4.b2
        b4.b2 = b6
        return b6
    def fonk9(self):
        if self.fonk3():
            return False
        b4 = self.b3
        if b4.b2 is None:
            self.b3 = None
            return b4
        while b4.b2.b2:
            b4 = b4.b2
        b7 = b4.b2
        b4.b2 = None
        return b7
    def fonk10(self, b1, b8 = 0):
        if b8 < 0:
            return False
        b6 = class1(b1)
        if b8 = = 0:
            b6.b2 = self.b3
            self.b3 = b6
            return b6
        b4 = self.b3
        for _ in range(b8 - 1):
            if b4 is None:
                return False
            b4 = b4.b2
        if b4 is None:
            return False
        b6.b2 = b4.b2
        b4.b2 = b6
        return b6
    def fonk11(self, b8 = 0):
        if b8 < 0 or self.fonk3():
            return False
        if b8 = = 0:
            return self.fonk7()
        b4 = self.b3
        for _ in range(b8 - 1):
            if b4.b2 is None:
                return False
            b4 = b4.b2
        if b4.b2 is None:
            return False
        b7 = b4.b2
        b4.b2 = b4.b2.b2
        return b7
    def fonk12(self):
        if self.fonk3():
            return "List is empty, nothing to reverse"
        b9 = None
        b4 = self.b3
        while b4:
            b10 = b4.b2
            b4.b2 = b9
            b9 = b4
            b4 = b10
        self.b3 = b9
        return self.b3
    def fonk13(self, node):
        if self.fonk3():
            return "List is empty, nothing to reverse"
        if node.b2 is None:
            self.b3 = node
            return node
        b11 = self.fonk13(node.b2)
        node.b2.b2 = node
        node.b2 = None
        return b11
    def fonk14(self):
        b4 = self.b3
        while b4:
            yield b4
            b4 = b4.b2
import unittest
class class3(unittest.TestCase):
    def fonk15(self):
        self.b12 = class1(0)
        self.b13 = class2()
        self.b14 = class2()
        self.b14.fonk6(1)
        self.b15 = class2()
        self.b15.fonk6(2)
        self.b15.fonk6(1)
        self.b16 = class2()
        self.b16.fonk6(3)
        self.b16.fonk6(2)
        self.b16.fonk6(1)
        self.b17 = class2()
        for i in range(99, 0, -1):
            self.b17.fonk6(i)
    def fonk16(self):
        self.assertEqual(self.b12.b1, 0)
    def fonk17(self):
        self.assertTrue(self.b13.fonk3())
        self.assertEqual(len(self.b13), 0)
    def fonk18(self):
        self.assertFalse(self.b14.fonk3())
        self.assertEqual(len(self.b14), 1)
        self.assertFalse(self.b15.fonk3())
        self.assertEqual(len(self.b15), 2)
        self.assertFalse(self.b16.fonk3())
        self.assertEqual(len(self.b16), 3)
        self.assertFalse(self.b17.fonk3())
        self.assertEqual(len(self.b17), 99)
    def fonk19(self):
        self.assertEqual(str(self.b13), "[]")
        self.assertEqual(len(self.b13), 0)
    def fonk20(self):
        self.assertEqual(str(self.b14), "[1]")
        self.assertEqual(len(self.b14), 1)
    def fonk21(self):
        self.assertEqual(str(self.b15), "[1 -> 2]")
        self.assertEqual(len(self.b15), 2)
    def fonk22(self):
        self.assertEqual(str(self.b16), "[1 -> 2 -> 3]")
        self.assertEqual(len(self.b16), 3)
    def fonk23(self):
        b18 = "[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 -> 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 -> 48 -> 49 -> 50 -> 51 -> 52 -> 53 -> 54 -> 55 -> 56 -> 57 -> 58 -> 59 -> 60 -> 61 -> 62 -> 63 -> 64 -> 65 -> 66 -> 67 -> 68 -> 69 -> 70 -> 71 -> 72 -> 73 -> 74 -> 75 -> 76 -> 77 -> 78 -> 79 -> 80 -> 81 -> 82 -> 83 -> 84 -> 85 -> 86 -> 87 -> 88 -> 89 -> 90 -> 91 -> 92 -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99]"
        self.assertEqual(str(self.b17), b18)
        self.assertEqual(len(self.b17), 99)
    def fonk24(self):
        self.b13.fonk6(1)
        self.b14.fonk6(0)
        self.b14.fonk6(0)
        self.b14.fonk6(0)
        self.b14.fonk6(0)
        self.assertEqual(str(self.b13), '[1]')
        self.assertEqual(str(self.b14), '[0 -> 0 -> 0 -> 0 -> 1]')
        self.assertEqual(len(self.b14), 5)
    def fonk25(self):
        self.assertFalse(self.b13.fonk7())
        self.b14.fonk7()
        self.assertEqual(str(self.b14), '[]')
        self.assertEqual(len(self.b14), 0)
        self.b15.fonk7()
        self.assertEqual(str(self.b15), '[2]')
        self.assertEqual(len(self.b15), 1)
        self.b16.fonk7()
        self.assertEqual(str(self.b16), '[2 -> 3]')
        self.assertEqual(len(self.b16), 2)
    def fonk26(self):
        self.b13.fonk8(98)
        self.assertEqual(str(self.b13), '[98]')
        self.assertEqual(len(self.b13), 1)
        self.b14.fonk8(98)
        self.assertEqual(str(self.b14), '[1 -> 98]')
        self.assertEqual(len(self.b14), 2)
        self.b15.fonk8(98)
        self.assertEqual(str(self.b15), '[1 -> 2 -> 98]')
        self.assertEqual(len(self.b15), 3)
        self.b16.fonk8(98)
        self.assertEqual(str(self.b16), '[1 -> 2 -> 3 -> 98]')
        self.assertEqual(len(self.b16), 4)
    def fonk27(self):
        b19 = self.b13.fonk9()
        self.assertFalse(b19)
        self.assertEqual(len(self.b13), 0)
    def fonk28(self):
        self.b14.fonk9()
        self.assertEqual(str(self.b14), '[]')
        self.assertEqual(len(self.b14), 0)
    def fonk29(self):
        self.b15.fonk9()
        self.assertEqual(str(self.b15), '[1]')
        self.assertEqual(len(self.b15), 1)
    def fonk30(self):
        self.b16.fonk9()
        self.assertEqual(str(self.b16), '[1 -> 2]')
        self.assertEqual(len(self.b16), 2)
    def fonk31(self):
        self.b13.fonk10(22)
        self.assertEqual(str(self.b13), '[22]')
        self.assertEqual(len(self.b13), 1)
    def fonk32(self):
        self.b13.fonk10(22, 0)
        self.assertEqual(str(self.b13), '[22]')
        self.assertEqual(len(self.b13), 1)
    def fonk33(self):
        self.b14.fonk10(22, 0)
        self.assertEqual(str(self.b14), '[22 -> 1]')
        self.assertEqual(len(self.b14), 2)
    def fonk34(self):
        self.b14.fonk10(22, 1)
        self.assertEqual(str(self.b14), '[1 -> 22]')
        self.assertEqual(len(self.b14), 2)
    def fonk35(self):
        self.b16.fonk10(22, 0)
        self.assertEqual(str(self.b16), '[22 -> 1 -> 2 -> 3]')
        self.assertEqual(len(self.b16), 4)
    def fonk36(self):
        self.b16.fonk10(22, 1)
        self.assertEqual(str(self.b16), '[1 -> 22 -> 2 -> 3]')
        self.assertEqual(len(self.b16), 4)
    def fonk37(self):
        self.b16.fonk10(22, 2)
        self.assertEqual(str(self.b16), '[1 -> 2 -> 22 -> 3]')
        self.assertEqual(len(self.b16), 4)
    def fonk38(self):
        self.b16.fonk10(22, 3)
        self.assertEqual(str(self.b16), '[1 -> 2 -> 3 -> 22]')
        self.assertEqual(len(self.b16), 4)
    def fonk39(self):
        b19 = self.b13.fonk11()
        self.assertFalse(b19)
    def fonk40(self):
        self.b14.fonk11(0)
        self.assertEqual(str(self.b14), '[]')
        self.assertEqual(len(self.b14), 0)
    def fonk41(self):
        self.b16.fonk11(0)
        self.assertEqual(str(self.b16), '[2 -> 3]')
        self.assertEqual(len(self.b16), 2)
    def fonk42(self):
        self.b16.fonk11(1)
        self.assertEqual(str(self.b16), '[1 -> 3]')
        self.assertEqual(len(self.b16), 2)
    def fonk43(self):
        self.b16.fonk11(2)
        self.assertEqual(str(self.b16), '[1 -> 2]')
        self.assertEqual(len(self.b16), 2)
    def fonk44(self):
        for i, node in enumerate(self.b16):
            self.assertEqual(node.b1, i + 1)
if b20 = = '__main__':
    unittest.main()