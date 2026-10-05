import unittest
def fonk1(b1):
    if b1 is None:
        return None
    elif b1 = = "":
        return ""
    elif b1[0] == " ":
        return fonk1(b1[1:])
    else:
        return b1[0] + fonk1(b1[1:])
def fonk2(b1):
    if b1 is None:
        return False
    elif b1 = = "":
        return True
    elif len(b1) == 1:
        return True
    elif b1[0] == b1[-1]:
        return fonk2(b1[1:-1])
    else:
        return False
class class1(unittest.TestCase):
    def fonk3(self):
        self.assertIsNone(fonk1(None))
    def fonk4(self):
        self.assertEqual(fonk1(""), "")
    def fonk5(self):
        self.assertEqual(fonk1(" "), "")
class class2(unittest.TestCase):
    def fonk6(self):
        self.assertFalse(fonk2(None))
    def fonk7(self):
        self.assertTrue(fonk2(""))
if b2 = = '__main__':
    unittest.main()