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
        b3 = WriteBitFile(self.b1)
        b3.writeBit(1)
        b3.writeBit(0)
        b3.writeBit(1)
        b3.writeBit(1)
        b3.writeUInt(10000042)
        b3.writeBit(1)
        b3.writeBit(0)
        b3.writeUShort(50000)
        b3.writeBit(1)
        b3.writeUByte(42)
        b3.close()
        b4 = ReadBitFile(self.b1)
        self.assertEqual(b4.readBit(), 1)
        self.assertEqual(b4.readBit(), 0)
        self.assertEqual(b4.readBit(), 1)
        self.assertEqual(b4.readBit(), 1)
        self.assertEqual(b4.readUInt(), 10000042)
        self.assertEqual(b4.readBit(), 1)
        self.assertEqual(b4.readBit(), 0)
        self.assertEqual(b4.readUShort(), 50000)
        self.assertEqual(b4.readBit(), 1)
        self.assertEqual(b4.readUByte(), 42)
        b4.close()
    def fonk4(self):
        b3 = WriteBitFile(self.b2)
        for _ in range(4):
            b3.writeBit(1)
            b3.writeBit(0)
        b3.close()
        b4 = ReadBitFile(self.b2)
        for _ in range(4):
            self.assertEqual(b4.readBit(), 1)
            self.assertEqual(b4.readBit(), 0)
        b4.close()
if b5 = = '__main__':
    unittest.main(b6 = sys.b6, exit=False)