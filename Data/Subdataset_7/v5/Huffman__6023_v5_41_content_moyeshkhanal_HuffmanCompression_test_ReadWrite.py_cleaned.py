import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class class1(unittest.TestCase):
    def fonk1(self):
        with WriteBitFile("data.bin") as w:
            w.write_bits([1, 0, 1, 1])
            w.write_uint(10000042)
            w.write_bits([1, 0])
            w.write_ushort(50000)
            w.write_ubyte(42)
        with ReadBitFile("data.bin") as r:
            self.assertEqual(r.read_bits(4), [1, 0, 1, 1])
            self.assertEqual(r.read_uint(), 10000042)
            self.assertEqual(r.read_bits(2), [1, 0])
            self.assertEqual(r.read_ushort(), 50000)
            self.assertEqual(r.read_ubyte(), 42)
        os.remove("data.bin")
    def fonk2(self):
        with WriteBitFile("data2.bin") as w:
            for _ in range(4):
                w.write_bits([1, 0])
def fonk3(argv):
    try:
        unittest.fonk3()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if b1 = = '__main__':
    fonk3(sys.argv)