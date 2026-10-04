import unittest
from sorters import QS, BCIS, IS
import random
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = list(range(10))
        self.b2 = self.b1.copy()
        random.shuffle(self.b2)
        print(f"Setup complete. Expected: {self.b1}, Non-Sorted: {self.b2}")
    def fonk2(self):
        b3 = BCIS()
        b3.sort(self.b2, 0, len(self.b2) - 1)
        self.assertEqual(self.b1, self.b2, "BCIS failed to sort correctly.")
    def fonk3(self):
        b3 = IS()
        b3.sort(self.b2)
        self.assertEqual(self.b1, self.b2, "IS failed to sort correctly.")
    def fonk4(self):
        b3 = QS()
        b3.sort(self.b2, 0, len(self.b2) - 1)
        self.assertEqual(self.b1, self.b2, "QS failed to sort correctly.")
    def fonk5(self):
        print("Running a test designed to fail.")
        self.assertEqual("foo", 1, "This test is b1 to fail.")
if b4 = = '__main__':
    unittest.main()