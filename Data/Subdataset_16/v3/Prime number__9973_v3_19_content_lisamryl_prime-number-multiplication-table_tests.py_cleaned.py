import math
import unittest
def fonk1(b1):
    if not isinstance(b1, int) or b1 <= 0:
        raise ValueError('Invalid number, must be a positive integer.')
    if b1 = = 1:
        return False
    if b1 = = 2:
        return True
    for b2 in range(2, int(math.sqrt(b1)) + 1):
        if b1 % b2 = = 0:
            return False
    return True
def fonk2(count):
    if not isinstance(count, int) or count <= 0:
        raise ValueError('Invalid number, must be a positive integer.')
    b3 = []
    a1 = 2
    while len(b3) < count:
        if fonk1(a1):
            b3.append(a1)
        a1 += 1
    return b3
def fonk3(b3):
    if not all(isinstance(p, int) for p in b3):
        raise ValueError('Invalid list, should only contain integers.')
    return [[b3[b2] * b3[j] for j in range(len(b3))] for b2 in range(len(b3))]
def fonk4(table):
    return "\b1".join(" | ".join(f"{item:4}" for item in row) for row in table)
class class1(unittest.TestCase):
    def fonk5(self):
        self.assertFalse(fonk1(1))
        self.assertTrue(fonk1(2))
        self.assertFalse(fonk1(4))
        self.assertTrue(fonk1(5))
        self.assertTrue(fonk1(104729))
        self.assertFalse(fonk1(104728))
    def fonk6(self):
        with self.assertRaises(ValueError) as cm:
            fonk1(0)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(ValueError) as cm:
            fonk1(-1)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(ValueError) as cm:
            fonk1(2.3)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
    def fonk7(self):
        self.assertEqual(fonk2(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        with self.assertRaises(ValueError) as cm:
            fonk2(-1)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(ValueError) as cm:
            fonk2('ten')
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
        with self.assertRaises(ValueError) as cm:
            fonk2(0)
        self.assertEqual(str(cm.exception), 'Invalid number, must be a positive integer.')
    def fonk8(self):
        b4 = fonk2(10000)
        self.assertEqual(b4[999], 7919)
        self.assertEqual(b4[9999], 104729)
    def fonk9(self):
        b5 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        b6 = fonk3(b5)
        b7 = fonk4(b6)
        b8 = '   6 |    9 |   15 |   21 |   33 |   39 |   51 |   57'
        b9 = '  58 |   87 |  145 |  203 |  319 |  377 |  493 |  551'
        self.assertIn(b8, b7)
        self.assertIn(b9, b7)
    def fonk10(self):
        b5 = ['2', 3, 5, 'bad data', 11.0, 13, 17, 19, 23, 29]
        with self.assertRaises(ValueError) as cm:
            fonk3(b5)
        self.assertEqual(str(cm.exception), 'Invalid list, should only contain integers.')
    def fonk11(self):
        b5 = [2, -3, 5, 7, 11, -13, 17, 19, 23, 29]
        b6 = fonk3(b5)
        b7 = fonk4(b6)
        b8 = '-6  |  9  | -15 | -21 | -33 |  39 | -51'
        b9 = '  58 | -87 |  145 |  203 |  319 | -377 |  493'
        self.assertIn(b8, b7)
        self.assertIn(b9, b7)
if b10 = = "__main__":
    unittest.main()