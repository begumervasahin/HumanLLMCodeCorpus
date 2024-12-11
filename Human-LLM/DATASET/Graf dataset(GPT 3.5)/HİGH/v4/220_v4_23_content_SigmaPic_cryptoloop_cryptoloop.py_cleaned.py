from Crypto.Cipher import AES
import binascii
import struct
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
class class1:
    a1 = 512
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b13, b14):
        self.fonk4(b13, b14, self._decrypt_sector)
    def fonk3(self, b13, b14):
        self.fonk4(b13, b14, self._encrypt_sector)
    def fonk4(self, b13, b14, transfer_func):
        a2 = 0
        with open(b13, "rb") as file_in:
            with open(b14, "wb") as file_out:
                while True:
                    b2 = file_in.read(class1.a1)
                    if len(b2) == 0:
                        break
                    b2 = b2.ljust(class1.a1, b'\0')
                    file_out.write(transfer_func(b2, a2))
                    a2 += 1
    def fonk5(self, b2, a2):
        b3 = struct.pack("<I", a2) + b'\0' * 12
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        return b4.b12(b2)
    def fonk6(self, b2, a2):
        b3 = struct.pack("<I", a2) + b'\0' * 12
        b4 = AES.new(self.b1, AES.MODE_CBC, b3)
        return b4.b11(b2)
def fonk7(b5 = None):
    if b5 is None:
        b5 = sys.b5[1:]
    b6 = 'A Python implementation of cryptoloop using AES CBC'
    try:
        b7 = ArgumentParser(description=b6, formatter_class=RawDescriptionHelpFormatter)
        b7.add_argument("-e", "--b11", b8 = "b11", action="store_true",
                            b9 = "Encrypt file")
        b7.add_argument("-d", "--b12", b8 = "b12", action="store_true",
                            b9 = "Decrypt file")
        b7.add_argument(b8 = "b1", b9="AES 128-bits b1 as hex string", metavar="b1", nargs=1)
        b7.add_argument(b8 = "b13", b9="Path to input file", metavar="input", nargs=1)
        b7.add_argument(b8 = "b14", b9="Path to output file", metavar="output", nargs=1)
        b10 = b7.parse_args()
        b11 = b10.b11
        b12 = b10.b12
        b1 = b10.b1[0]
        b13 = b10.b13[0]
        b14 = b10.b14[0]
        if b11 and b12:
            raise Exception('Choose either b11 or b12 but not both')
        b15 = class1(binascii.unhexlify(b1))
        if b12:
            b15.fonk2(b13, b14)
        elif b11:
            b15.fonk3(b13, b14)
        return 0
    except KeyboardInterrupt:
        return 0
    except Exception as e:
        b16 = len('cryptoloop') * " "
        sys.stderr.write('cryptoloop' + ": " + str(e) + "\n")
        sys.stderr.write(b16 + "  For b9, use --b9")
        return 2
if b17 = = "__main__":
    sys.exit(fonk7())