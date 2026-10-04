import unittest
def fonk1(pesel_nr):
    if len(pesel_nr) != 11 or not pesel_nr.isdigit():
        return False
    b1 = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    b2 = sum(int(pesel_nr[i]) * b1[i] for i in range(10))
    b3 = (10 - (b2 % 10)) % 10
    return b3 = = int(pesel_nr[-1])
class class1(unittest.TestCase):
    def fonk2(self):
        self.assertTrue(fonk1("92121510595"))
        self.assertTrue(fonk1("99810235403"))
    def fonk3(self):
        self.assertFalse(fonk1("44051401358"))
        self.assertFalse(fonk1("51401358"))
        self.assertFalse(fonk1("12345678901"))
if b4 = = "__main__":
    unittest.main()