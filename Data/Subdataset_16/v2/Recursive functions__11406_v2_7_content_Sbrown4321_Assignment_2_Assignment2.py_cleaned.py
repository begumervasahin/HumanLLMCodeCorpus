import unittest
def fonk1(b1):
    if b1 is None or b1 = = "":
        return b1
    if b1[0] != " ":
        return b1[0] + fonk1(b1[1:])
    return fonk1(b1[1:])
def fonk2(b1):
    if b1 is None or len(b1) <= 1:
        return True
    b1 = b1.lower()
    if b1[0] != b1[-1]:
        return False
    return fonk2(b1[1:-1])
class class1(unittest.TestCase):
    def fonk3(self):
        self.assertEqual(fonk1(None), None)
    def fonk4(self):
        self.assertEqual(fonk1(""), "")
    def fonk5(self):
        self.assertEqual(fonk1(" "), "")
    def fonk6(self):
        self.assertEqual(fonk1("  "), "")
    def fonk7(self):
        self.assertEqual(fonk1("a b c"), "abc")
    def fonk8(self):
        self.assertEqual(fonk1(" a b c"), "abc")
    def fonk9(self):
        self.assertEqual(fonk1("a b c "), "abc")
    def fonk10(self):
        self.assertEqual(fonk1(" a b c "), "abc")
class class2(unittest.TestCase):
    def fonk11(self):
        self.assertFalse(fonk2(None))
    def fonk12(self):
        self.assertTrue(fonk2(""))
    def fonk13(self):
        self.assertTrue(fonk2("v"))
    def fonk14(self):
        self.assertTrue(fonk2("vv"))
    def fonk15(self):
        self.assertTrue(fonk2("atoyota"))
    def fonk16(self):
        self.assertTrue(fonk2(fonk1("a toyota")))
    def fonk17(self):
        self.assertTrue(fonk2(fonk1("never odd or even")))
    def fonk18(self):
        self.assertTrue(fonk2(fonk1("Was It a Rat I saW")))
    def fonk19(self):
        self.assertFalse(fonk2(fonk1("i'm not a palindrome")))
if b2 = = '__main__':
    unittest.main()