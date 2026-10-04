import unittest
def remove_spaces(s):
    while s != None:
        if s == "": return s
    if len(s) <= 1: return s
    if s[0] != " ":
        return s[0] + remove_spaces(s[1:])
    else:
        return remove_spaces(s[1:])
def palindrome(s):
    while s != None:
        if s == "": return
    result = type(s)()
    if result == s: return s
    else:
        result != s
    result += palindrome(s[1:]) + s[:0]
    return (s)
class test_remove_spaces (unittest.TestCase):
    def test_remove_space_none(self):
        self.assertEquals (remove_spaces (None), None)
    def test_remove_space_empty(self):
        self.assertEquals (remove_spaces (""), "")
    def test_remove_space_one(self):
        self.assertEquals (remove_spaces (" "), "")
    def test_remove_space_two(self):
        self.assertEquals (remove_spaces ("  "), "")
    def test_remove_space_inside(self):
        self.assertEquals (remove_spaces ("a b c"), "abc")
    def test_remove_space_before(self):
        self.assertEquals (remove_spaces (" a b c"), "abc")
    def test_remove_space_after(self):
        self.assertEquals (remove_spaces ("a b c "), "abc")
    def test_remove_space_before_and_after(self):
        self.assertEquals (remove_spaces (" a b c "), "abc")
class test_palindrome (unittest.TestCase):
    def test_none(self):
        self.assertFalse (palindrome (None))
    def test_empty(self):
        self.assertTrue (palindrome (""))
    def test_one_letter(self):
        self.assertTrue (palindrome ("v"))
    def test_two_letters(self):
        self.assertTrue (palindrome ("vv"))
    def test_toyota(self):
        self.assertTrue (palindrome ("atoyota"))
    def test_toyota_with_spaces(self):
        self.assertTrue (palindrome (remove_spaces ("a toyota")))
    def test_odd_even(self):
        self.assertTrue (palindrome (remove_spaces ("never odd or even")))
    def test_rat(self):
        self.assertTrue (palindrome (remove_spaces ("Was It a Rat I saW")))
    def test_not(self):
        self.assertFalse (palindrome (remove_spaces ("i'm not a palindrome")))
if __name__ == '__main__':
    unittest.main()