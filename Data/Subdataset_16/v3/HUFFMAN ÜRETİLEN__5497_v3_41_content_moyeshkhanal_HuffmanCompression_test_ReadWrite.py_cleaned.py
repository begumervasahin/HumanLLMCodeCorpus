import sys
import unittest
import os
class class1:
    def fonk1(self, filename):
        self.b1 = open(filename, 'wb')
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, b2):
        if b2 not in (0, 1):
            raise ValueError("Bit must be 0 or 1")
        if self.a2 = = 8:
            self.fonk7()
        if b2 = = 1:
            self.a1 |= (1 << (7 - self.a2))
        self.a2 += 1
    def fonk3(self, value):
        self.fonk6(value, 4)
    def fonk4(self, value):
        self.fonk6(value, 2)
    def fonk5(self, value):
        self.fonk6(value, 1)
    def fonk6(self, value, num_bytes):
        self.b1.write(value.to_bytes(num_bytes, b3 = 'big'))
    def fonk7(self):
        if self.a2 > 0:
            self.b1.write(bytes([self.a1]))
            self.a1 = 0
            self.a2 = 0
    def fonk8(self):
        self.fonk7()
        self.b1.fonk16()
class class2:
    def fonk9(self, filename):
        self.b1 = open(filename, 'rb')
        self.a1 = None
        self.a2 = 8
    def fonk10(self):
        if self.a2 = = 8:
            self.fonk15()
        b2 = (self.a1 >> (7 - self.a2)) & 1
        self.a2 += 1
        return b2
    def fonk11(self):
        return self.fonk14(4)
    def fonk12(self):
        return self.fonk14(2)
    def fonk13(self):
        return self.fonk14(1)
    def fonk14(self, num_bytes):
        return int.from_bytes(self.b1.read(num_bytes), b3 = 'big')
    def fonk15(self):
        b4 = self.b1.read(1)
        if not b4:
            raise EOFError("End of b1 reached")
        self.a1 = b4[0]
        self.a2 = 0
    def fonk16(self):
        self.b1.fonk16()
class class3(unittest.TestCase):
    def fonk17(self):
        self.b5 = "test_data.bin"
    def fonk18(self):
        if os.path.exists(self.b5):
            os.remove(self.b5)
    def fonk19(self):
        b6 = class1(self.b5)
        b6.fonk2(1)
        b6.fonk2(0)
        b6.fonk2(1)
        b6.fonk2(1)
        b6.fonk3(10000042)
        b6.fonk2(1)
        b6.fonk2(0)
        b6.fonk4(50000)
        b6.fonk2(1)
        b6.fonk5(42)
        b6.fonk16()
        b7 = class2(self.b5)
        self.assertEqual(b7.fonk10(), 1)
        self.assertEqual(b7.fonk10(), 0)
        self.assertEqual(b7.fonk10(), 1)
        self.assertEqual(b7.fonk10(), 1)
        self.assertEqual(b7.fonk11(), 10000042)
        self.assertEqual(b7.fonk10(), 1)
        self.assertEqual(b7.fonk10(), 0)
        self.assertEqual(b7.fonk12(), 50000)
        self.assertEqual(b7.fonk10(), 1)
        self.assertEqual(b7.fonk13(), 42)
        b7.fonk16()
    def fonk20(self):
        b6 = class1(self.b5)
        for _ in range(4):
            b6.fonk2(1)
            b6.fonk2(0)
        b6.fonk16()
        b7 = class2(self.b5)
        for _ in range(4):
            self.assertEqual(b7.fonk10(), 1)
            self.assertEqual(b7.fonk10(), 0)
        b7.fonk16()
def fonk21(b8):
    unittest.fonk21(b8 = b8, exit=False)
if b9 = = '__main__':
    fonk21(sys.b8)