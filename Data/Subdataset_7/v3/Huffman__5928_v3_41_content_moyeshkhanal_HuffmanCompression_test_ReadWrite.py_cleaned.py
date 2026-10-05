import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = "data.bin"
        self.b2 = "data2.bin"
    def fonk2(self):
        if os.path.exists(self.b1):
            os.remove(self.b1)
        if os.path.exists(self.b2):
            os.remove(self.b2)
    def fonk3(self):
        with WriteBitFile(self.b1) as w:
            w.write_bit(1)
            w.write_bit(0)
            w.write_bit(1)
            w.write_bit(1)
            w.write_uint(10000042)
            w.write_bit(1)
            w.write_bit(0)
            w.write_ushort(50000)
            w.write_bit(1)
            w.write_ubyte(42)
        with ReadBitFile(self.b1) as r:
            self.assertEqual(r.read_bit(), 1)
            self.assertEqual(r.read_bit(), 0)
            self.assertEqual(r.read_bit(), 1)
            self.assertEqual(r.read_bit(), 1)
            self.assertEqual(r.read_uint(), 10000042)
            self.assertEqual(r.read_bit(), 1)
            self.assertEqual(r.read_bit(), 0)
            self.assertEqual(r.read_ushort(), 50000)
            self.assertEqual(r.read_bit(), 1)
            self.assertEqual(r.read_ubyte(), 42)
    def fonk4(self):
        with WriteBitFile(self.b2) as w:
            for _ in range(4):
                w.write_bit(1)
                w.write_bit(0)
def fonk5(argv):
    try:
        unittest.fonk5()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if b3 = = '__main__':
    fonk5(sys.argv)