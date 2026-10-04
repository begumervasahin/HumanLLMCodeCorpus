import os
import struct
import sys
import time
b1 = bytearray.fromhex(
    "46574156FEFF00400001010000000000000200007000000000000040000000C07001000000000100000000000000000000000000000000000000000000000000"
)
b2 = bytearray.fromhex(
    "494E464F000000C0000000000000000000000000000000000000000000000000710000000000001471000000000000281F000000000000180300000000000028000000001F000000000000000300000000000042000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
)
def fonk1():
    if len(sys.argv) < 2 or not sys.argv[1].endswith(".bfstm"):
        print("Invalid input file. Please provide a .bfstm file.")
        print("\nExiting in 5 seconds...")
        time.sleep(5)
        sys.exit(1)
    b3 = sys.argv[1]
    with open(b3, "rb") as infile:
        b4 = infile.read()
    b5 = struct.unpack(">I", b4[0x30:0x34])[0]
    b6 = struct.unpack(">I", b4[0x34:0x38])[0]
    b1[0x0C:0x10] = (0x100 + b6).to_bytes(4, 'big')
    b1[0x28:0x2C] = b6.to_bytes(4, 'big')
    b2[0x08:0x09] = b4[0x60:0x61]
    b2[0x09:0x0A] = b4[0x61:0x62]
    b2[0x1F:0x20] = b4[0x62:0x63]
    b2[0x14:0x18] = b4[0x6C:0x70]
    b2[0x0E:0x10] = (struct.unpack(">H", b4[0x64:0x68])[0]).to_bytes(2, 'big')
    b2[0x10:0x14] = b4[0x68:0x6C]
    b7 = struct.unpack(">I", b4[0x74:0x78])[0]
    b8 = struct.unpack(">I", b4[0x84:0x88])[0]
    b9 = (
        b7
        - ((b8 & 0xFF)
        - (((b8 & 0xFF)
        + b8
    )
    b2[0x48:0x4C] = (0x18 + b9).to_bytes(4, 'big')
    b2[0x58:0xB2] = b4[0xDC:0x136]
    b10 = b4[b5:b5 + b6]
    b11 = b1 + b2 + b10
    b12 = os.path.splitext(b3)[0] + ".bfwav"
    with open(b12, "wb") as outfile:
        outfile.write(b11)
if b13 = = "__main__":
    fonk1()