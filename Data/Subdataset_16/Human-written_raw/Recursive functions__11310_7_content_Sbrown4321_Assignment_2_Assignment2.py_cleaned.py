import unittest
def fonk1(b1):
    while b1 != None:
        if b1 = = "": return b1
    if len(b1) <= 1: return b1
    if b1[0] != " ":
        return b1[0] + fonk1(b1[1:])
    else:
        return fonk1(b1[1:])
def fonk2(b1):
    while b1 != None:
        if b1 = = "": return
    b2 = type(b1)()
    if b2 = = b1: return b1
    else:
        b2 != b1
    b2 += fonk2(b1[1:]) + b1[:0]
    return (b1)
class class1 (unittest.TestCase):
    def fonk3(self):
        self.assertEquals (remove_spaces (None), None)
    def fonk4(self):
        self.assertEquals (remove_spaces (""), "")
    def fonk5(self):
        self.assertEquals (remove_spaces (" "), "")
    def fonk6(self):
        self.assertEquals (remove_spaces ("  "), "")
    def fonk7(self):
        self.assertEquals (remove_spaces ("a b c"), "abc")
    def fonk8(self):
        self.assertEquals (remove_spaces (" a b c"), "abc")
    def fonk9(self):
        self.assertEquals (remove_spaces ("a b c "), "abc")
    def fonk10(self):
        self.assertEquals (remove_spaces (" a b c "), "abc")
class class2 (unittest.TestCase):
    def fonk11(self):
        self.assertFalse (palindrome (None))
    def fonk12(self):
        self.assertTrue (palindrome (""))
    def fonk13(self):
        self.assertTrue (palindrome ("v"))
    def fonk14(self):
        self.assertTrue (palindrome ("vv"))
    def fonk15(self):
        self.assertTrue (palindrome ("atoyota"))
    def fonk16(self):
        self.assertTrue (palindrome (remove_spaces ("a toyota")))
    def fonk17(self):
        self.assertTrue (palindrome (remove_spaces ("never odd or even")))
    def fonk18(self):
        self.assertTrue (palindrome (remove_spaces ("Was It a Rat I saW")))
    def fonk19(self):
        self.assertFalse (palindrome (remove_spaces ("i'm not a palindrome")))
if b3 = = '__main__':
    unittest.main()