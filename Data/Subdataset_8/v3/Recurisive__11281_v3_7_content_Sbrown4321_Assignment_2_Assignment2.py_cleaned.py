import unittest
def remove_spaces(s):
    if s is None:
        return None
    elif s == "":
        return ""
    elif s[0] == " ":
        return remove_spaces(s[1:])
    else:
        return s[0] + remove_spaces(s[1:])
def is_palindrome(s):
    if s is None:
        return False
    elif s == "":
        return True
    elif len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
class TestRemoveSpaces(unittest.TestCase):
    def test_remove_space_none(self):
        self.assertIsNone(remove_spaces(None))
    def test_remove_space_empty(self):
        self.assertEqual(remove_spaces(""), "")
    def test_remove_space_one(self):
        self.assertEqual(remove_spaces(" "), "")
class TestIsPalindrome(unittest.TestCase):
    def test_none(self):
        self.assertFalse(is_palindrome(None))
    def test_empty(self):
        self.assertTrue(is_palindrome(""))
if __name__ == '__main__':
    unittest.main()