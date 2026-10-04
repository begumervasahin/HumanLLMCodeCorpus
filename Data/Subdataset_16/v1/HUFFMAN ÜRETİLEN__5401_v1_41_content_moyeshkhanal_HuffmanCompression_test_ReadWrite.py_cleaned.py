import sys
import unittest
import os
class class1:
    def fonk1(self, filename):
        self.b1 = open(filename, 'wb')
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, b2):
        if b2 not in [0, 1]:
            raise ValueError("Bit must be 0 or 1")
        if self.a2 = = 8:
            self.fonk6()
        if b2 = = 1:
            self.a1 |= (1 << (7 - self.a2))
        self.a2 += 1
    def fonk3(self, value):
        self.b1.write(value.to_bytes(4, b3 = 'big'))
    def fonk4(self, value):
        self.b1.write(value.to_bytes(2, b3 = 'big'))
    def fonk5(self, value):
        self.b1.write(value.to_bytes(1, b3 = 'big'))
    def fonk6(self):
        if self.a2 > 0:
            self.b1.write(bytes([self.a1]))
            self.a1 = 0
            self.a2 = 0
    def fonk7(self):
        self.fonk6()
        self.b1.fonk13()
class class2:
    def fonk8(self, filename):
        self.b1 = open(filename, 'rb')
        self.a1 = None
        self.a2 = 8
    def fonk9(self):
        if self.a2 = = 8:
            b4 = self.b1.read(1)
            if len(b4) == 0:
                raise EOFError("End of b1 reached")
            self.a1 = b4[0]
            self.a2 = 0
        b2 = (self.a1 >> (7 - self.a2)) & 1
        self.a2 += 1
        return b2
    def fonk10(self):
        return int.from_bytes(self.b1.read(4), b3 = 'big')
    def fonk11(self):
        return int.from_bytes(self.b1.read(2), b3 = 'big')
    def fonk12(self):
        return int.from_bytes(self.b1.read(1), b3 = 'big')
    def fonk13(self):
        self.b1.fonk13()
class class3(unittest.TestCase):
    def fonk14(self):
        b5 = class1("data.bin")
        b5.fonk2(1)
        b5.fonk2(0)
        b5.fonk2(1)
        b5.fonk2(1)
        b5.fonk3(10000042)
        b5.fonk2(1)
        b5.fonk2(0)
        b5.fonk4(50000)
        b5.fonk2(1)
        b5.fonk5(42)
        b5.fonk13()
        b6 = class2("data.bin")
        self.assertEqual(b6.fonk9(), 1)
        self.assertEqual(b6.fonk9(), 0)
        self.assertEqual(b6.fonk9(), 1)
        self.assertEqual(b6.fonk9(), 1)
        self.assertEqual(b6.fonk10(), 10000042)
        self.assertEqual(b6.fonk9(), 1)
        self.assertEqual(b6.fonk9(), 0)
        self.assertEqual(b6.fonk11(), 50000)
        self.assertEqual(b6.fonk9(), 1)
        self.assertEqual(b6.fonk12(), 42)
        b6.fonk13()
        os.remove("data.bin")
    def fonk15(self):
        b5 = class1("data2.bin")
        for _ in range(4):
            b5.fonk2(1)
            b5.fonk2(0)
        b5.fonk13()
def fonk16(b7):
    try:
        unittest.fonk16(b7 = b7, exit=False)
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if b8 = = '__main__':
    fonk16(sys.b7)