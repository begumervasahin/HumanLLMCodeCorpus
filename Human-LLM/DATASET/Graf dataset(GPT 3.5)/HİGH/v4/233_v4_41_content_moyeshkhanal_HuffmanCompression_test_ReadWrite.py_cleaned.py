import sys
import unittest
import os
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = WriteBitFile("data.bin")
        b1.writeBit(1)
        b1.writeBit(0)
        b1.writeBit(1)
        b1.writeBit(1)
        b1.writeUInt(10000042)
        b1.writeBit(1)
        b1.writeBit(0)
        b1.writeUShort(50000)
        b1.writeBit(1)
        b1.writeUByte(42)
        b1.close()
        b2 = ReadBitFile("data.bin")
        self.assertEqual(b2.readBit(), 1)
        self.assertEqual(b2.readBit(), 0)
        self.assertEqual(b2.readBit(), 1)
        self.assertEqual(b2.readBit(), 1)
        self.assertEqual(b2.readUInt(), 10000042)
        self.assertEqual(b2.readBit(), 1)
        self.assertEqual(b2.readBit(), 0)
        self.assertEqual(b2.readUShort(), 50000)
        self.assertEqual(b2.readBit(), 1)
        self.assertEqual(b2.readUByte(), 42)
        b2.close()
        os.remove("data.bin")
    def fonk2(self):
        b1 = WriteBitFile("data2.bin")
        for _ in range(4):
            b1.writeBit(1)
            b1.writeBit(0)
        b1.close()
def fonk3(argv):
    try:
        unittest.fonk3()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if b3 = = '__main__':
    fonk3(sys.argv)