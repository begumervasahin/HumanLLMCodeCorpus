import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class ReadWriteTest(unittest.TestCase):
    def setUp(self):
        self.data_file = "data.bin"
        self.data_file2 = "data2.bin"
    def tearDown(self):
        if os.path.exists(self.data_file):
            os.remove(self.data_file)
        if os.path.exists(self.data_file2):
            os.remove(self.data_file2)
    def test_write_and_read(self):
        with WriteBitFile(self.data_file) as w:
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
        with ReadBitFile(self.data_file) as r:
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
    def test_write_bits(self):
        with WriteBitFile(self.data_file2) as w:
            for _ in range(4):
                w.write_bit(1)
                w.write_bit(0)
def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if __name__ == '__main__':
    main(sys.argv)