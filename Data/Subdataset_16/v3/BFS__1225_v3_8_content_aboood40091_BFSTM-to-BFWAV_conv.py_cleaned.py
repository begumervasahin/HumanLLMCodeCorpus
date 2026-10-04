import os
import struct
import sys
import time
b1 = bytearray.fromhex(
    "46574156FEFF00400001010000000000000200007000000000000040000000C07001000000000100000000000000000000000000000000000000000000000000"
)
b2 = bytearray.fromhex(
    "494E464F000000C0000000000000000000000000000000000000000000000000710000000000001471000000000000281F000000000000180300000000000028000000001F000000000000000300000000000042000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
)
def fonk1():
    if not sys.argv[1].endswith(".bfstm"):
        print("Invalid file format. Please provide a .bfstm file.")
        print("Exiting in 5 seconds...")
        time.sleep(5)
        sys.exit(1)
    with open(sys.argv[1], "rb") as infile:
        b3 = infile.read()
    b4 = struct.unpack(">I", b3[0x30:0x34])[0]
    b5 = struct.unpack(">I", b3[0x34:0x38])[0]
    fonk2(b3, b5)
    b6 = struct.unpack(">I", b3[0x74:0x78])[0]
    b7 = struct.unpack(">I", b3[0x84:0x88])[0]
    b8 = fonk3(
        b6, b7
    )
    b2[0x48:0x4C] = (0x18 + b8).to_bytes(4, 'big')
    b2[0x58:0xB2] = b3[0xDC:0x136]
    b9 = b3[b4:b4 + b5]
    b10 = b1 + b2 + b9
    b11 = os.path.splitext(sys.argv[1])[0] + ".bfwav"
    with open(b11, "wb") as output_file:
        output_file.write(b10)
    print(f"Conversion complete: {b11}")
def fonk2(b3, b5):
    b1[0x0C:0x10] = (0x100 + b5).to_bytes(4, 'big')
    b1[0x28:0x2C] = b5.to_bytes(4, 'big')
    b2[0x08:0x09] = b3[0x60:0x61]
    b2[0x09:0x0A] = b3[0x61:0x62]
    b2[0x1F:0x20] = b3[0x62:0x63]
    b2[0x14:0x18] = b3[0x6C:0x70]
    b2[0x0E:0x10] = struct.unpack(">H", b3[0x64:0x66])[0].to_bytes(2, 'big')
    b2[0x10:0x14] = b3[0x68:0x6C]
def fonk3(b6, b7):
    b8 = b6 - ((b7 & 0xFF)
    b8 -= (((b7 & 0xFF)
    b8 += b7
    return b8
if b12 = = "__main__":
    fonk1()