import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class ReadWriteTest(unittest.TestCase):
    def test_mixed(self):
        w = WriteBitFile("data.bin")
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
        w.close()
        r = ReadBitFile("data.bin")
        b = r.read_bit()
        self.assertEqual(b, 1)
        b = r.read_bit()
        self.assertEqual(b, 0)
        b = r.read_bit()
        self.assertEqual(b, 1)
        b = r.read_bit()
        self.assertEqual(b, 1)
        value = r.read_uint()
        self.assertEqual(value, 10000042)
        b = r.read_bit()
        self.assertEqual(b, 1)
        b = r.read_bit()
        self.assertEqual(b, 0)
        value = r.read_ushort()
        self.assertEqual(value, 50000)
        b = r.read_bit()
        self.assertEqual(b, 1)
        value = r.read_ubyte()
        self.assertEqual(value, 42)
        r.close()
        os.remove("data.bin")
    def test_b(self):
        w = WriteBitFile("data2.bin")
        for _ in range(4):
            w.write_bit(1)
            w.write_bit(0)
        w.close()
def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if __name__ == '__main__':
    main(sys.argv)