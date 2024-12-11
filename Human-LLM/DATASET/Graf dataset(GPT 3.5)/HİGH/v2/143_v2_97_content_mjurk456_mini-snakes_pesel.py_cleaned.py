
def fonk1(pesel_nr):
    if len(pesel_nr) < 11:
        return False
    if not pesel_nr.isdigit():
        return False
    b1 = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    b2 = sum(int(pesel_nr[i]) * b1[i] for i in range(10))
    return (10 - int(str(b2)[-1])) == int(pesel_nr[-1])
import unittest
class class1(unittest.TestCase):
    def fonk2(self):
        self.assertTrue(fonk1("92121510595"))
        self.assertTrue(fonk1("99810235403"))
    def fonk3(self):
        self.assertFalse(fonk1("44051401358"))
        self.assertFalse(fonk1("51401358"))
if b3 = = "__main__":
    unittest.main()