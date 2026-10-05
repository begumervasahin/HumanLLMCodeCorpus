import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class ReadWriteTest(unittest.TestCase):
    def test_mixed_data(self):
        w = WriteBitFile("data.bin")
        w.writeBit(1)
        w.writeBit(0)
        w.writeBit(1)
        w.writeBit(1)
        w.writeUInt(10000042)
        w.writeBit(1)
        w.writeBit(0)
        w.writeUShort(50000)
        w.writeBit(1)
        w.writeUByte(42)
        w.close()
        r = ReadBitFile("data.bin")
        self.assertEqual(r.readBit(), 1)
        self.assertEqual(r.readBit(), 0)
        self.assertEqual(r.readBit(), 1)
        self.assertEqual(r.readBit(), 1)
        self.assertEqual(r.readUInt(), 10000042)
        self.assertEqual(r.readBit(), 1)
        self.assertEqual(r.readBit(), 0)
        self.assertEqual(r.readUShort(), 50000)
        self.assertEqual(r.readBit(), 1)
        self.assertEqual(r.readUByte(), 42)
        r.close()
        os.remove("data.bin")
    def test_single_bit_write(self):
        w = WriteBitFile("data2.bin")
        for _ in range(4):
            w.writeBit(1)
            w.writeBit(0)
        w.close()
def main(argv):
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if __name__ == '__main__':
    main(sys.argv)