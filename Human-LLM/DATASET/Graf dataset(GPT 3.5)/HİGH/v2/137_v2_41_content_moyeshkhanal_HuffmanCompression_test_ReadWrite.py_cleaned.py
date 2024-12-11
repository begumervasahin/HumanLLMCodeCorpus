import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = WriteBitFile("data.bin")
        b1.write_bit(1)
        b1.write_bit(0)
        b1.write_bit(1)
        b1.write_bit(1)
        b1.write_uint(10000042)
        b1.write_bit(1)
        b1.write_bit(0)
        b1.write_ushort(50000)
        b1.write_bit(1)
        b1.write_ubyte(42)
        b1.close()
        b2 = ReadBitFile("data.bin")
        b3 = b2.read_bit()
        self.assertEqual(b3, 1)
        b3 = b2.read_bit()
        self.assertEqual(b3, 0)
        b3 = b2.read_bit()
        self.assertEqual(b3, 1)
        b3 = b2.read_bit()
        self.assertEqual(b3, 1)
        b4 = b2.read_uint()
        self.assertEqual(b4, 10000042)
        b3 = b2.read_bit()
        self.assertEqual(b3, 1)
        b3 = b2.read_bit()
        self.assertEqual(b3, 0)
        b4 = b2.read_ushort()
        self.assertEqual(b4, 50000)
        b3 = b2.read_bit()
        self.assertEqual(b3, 1)
        b4 = b2.read_ubyte()
        self.assertEqual(b4, 42)
        b2.close()
        os.remove("data.bin")
    def fonk2(self):
        b1 = WriteBitFile("data2.bin")
        for _ in range(4):
            b1.write_bit(1)
            b1.write_bit(0)
        b1.close()
def fonk3(argv):
    try:
        unittest.fonk3()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if b5 = = '__main__':
    fonk3(sys.argv)