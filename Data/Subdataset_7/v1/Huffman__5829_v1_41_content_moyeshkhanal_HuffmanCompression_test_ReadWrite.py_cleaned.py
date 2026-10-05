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
        b3 = b2.readBit()
        self.assertEqual(b3, 1)
        b3 = b2.readBit()
        self.assertEqual(b3, 0)
        b3 = b2.readBit()
        self.assertEqual(b3, 1)
        b3 = b2.readBit()
        self.assertEqual(b3, 1)
        b4 = b2.readUInt()
        self.assertEqual(b4, 10000042)
        b3 = b2.readBit()
        self.assertEqual(b3, 1)
        b3 = b2.readBit()
        self.assertEqual(b3, 0)
        b4 = b2.readUShort()
        self.assertEqual(b4, 50000)
        b3 = b2.readBit()
        self.assertEqual(b3, 1)
        b4 = b2.readUByte()
        self.assertEqual(b4, 42)
        b2.close()
        os.remove("data.bin")
    def fonk2(self):
        b1 = WriteBitFile("data2.bin")
        for i in range(4):
            b1.writeBit(1)
            b1.writeBit(0)
        b1.close()
def fonk3(argv):
    try:
        unittest.fonk3()
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
if b5 = = '__main__':
    fonk3(sys.argv)