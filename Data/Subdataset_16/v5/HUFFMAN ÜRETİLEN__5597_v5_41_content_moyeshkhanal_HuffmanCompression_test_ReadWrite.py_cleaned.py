import os
import sys
import unittest
from WriteBitFile import WriteBitFile
from ReadBitFile import ReadBitFile
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = "data.bin"
        self.b2 = "data2.bin"
    def fonk2(self):
        self.fonk3(self.b1)
        self.fonk3(self.b2)
    def fonk3(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
    def fonk4(self):
        with WriteBitFile(self.b1) as writer:
            writer.writeBit(1)
            writer.writeBit(0)
            writer.writeBit(1)
            writer.writeBit(1)
            writer.writeUInt(10000042)
            writer.writeBit(1)
            writer.writeBit(0)
            writer.writeUShort(50000)
            writer.writeBit(1)
            writer.writeUByte(42)
        with ReadBitFile(self.b1) as reader:
            self.assertEqual(reader.readBit(), 1)
            self.assertEqual(reader.readBit(), 0)
            self.assertEqual(reader.readBit(), 1)
            self.assertEqual(reader.readBit(), 1)
            self.assertEqual(reader.readUInt(), 10000042)
            self.assertEqual(reader.readBit(), 1)
            self.assertEqual(reader.readBit(), 0)
            self.assertEqual(reader.readUShort(), 50000)
            self.assertEqual(reader.readBit(), 1)
            self.assertEqual(reader.readUByte(), 42)
    def fonk5(self):
        with WriteBitFile(self.b2) as writer:
            for _ in range(4):
                writer.writeBit(1)
                writer.writeBit(0)
        with ReadBitFile(self.b2) as reader:
            for _ in range(4):
                self.assertEqual(reader.readBit(), 1)
                self.assertEqual(reader.readBit(), 0)
if b3 = = '__main__':
    unittest.main(b4 = sys.b4, exit=False)