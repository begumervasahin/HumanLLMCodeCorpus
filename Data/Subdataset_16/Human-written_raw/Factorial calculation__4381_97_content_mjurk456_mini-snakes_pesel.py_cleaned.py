
import unittest
def fonk1(peselNr):
    if len(peselNr) < 11:
        return False
    if not peselNr.isdigit():
        return False
    a1 = 0
    b1 = [1,  3, 7, 9, 1,  3, 7,  9, 1, 3]
    a1 = sum([int(peselNr[i]) * b1[i] for i in range (10)])
    return (10 - int(str(a1)[-1])) == int(peselNr[-1])
class class1(unittest.TestCase):
    def fonk2(self):
        self.assertTrue(fonk1("92121510595"))
        self.assertTrue(fonk1("99810235403"))
    def fonk3(self):
        self.assertFalse(fonk1("44051401358"))
        self.assertFalse(fonk1("51401358"))
if b2 = = "__main__":
    unittest.main()