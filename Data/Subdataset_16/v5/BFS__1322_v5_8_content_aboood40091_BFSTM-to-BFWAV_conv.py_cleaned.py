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
def fonk1(b7):
    with open(b7, "rb") as infile:
        return infile.read()
def fonk2(b8):
    b3 = struct.unpack(">I", b8[0x30:0x34])[0]
    b4 = struct.unpack(">I", b8[0x34:0x38])[0]
    return b3, b4
def fonk3(b9, b4):
    b9[0x0C:0x10] = (0x100 + b4).to_bytes(4, 'big')
    b9[0x28:0x2C] = b4.to_bytes(4, 'big')
def fonk4(b10, b8):
    b10[0x08:0x09] = b8[0x60:0x61]
    b10[0x09:0x0A] = b8[0x61:0x62]
    b10[0x1F:0x20] = b8[0x62:0x63]
    b10[0x14:0x18] = b8[0x6C:0x70]
    b10[0x0E:0x10] = (struct.unpack(">H", b8[0x64:0x68])[0]).to_bytes(2, 'big')
    b10[0x10:0x14] = b8[0x68:0x6C]
def fonk5(b8):
    b5 = struct.unpack(">I", b8[0x74:0x78])[0]
    b6 = struct.unpack(">I", b8[0x84:0x88])[0]
    return (
        b5
        - ((b6 & 0xFF)
        - (((b6 & 0xFF)
        + b6
    )
def fonk6():
    if len(sys.argv) < 2 or not sys.argv[1].endswith(".bfstm"):
        print("Invalid input file. Please provide a .bfstm file.")
        print("\nExiting in 5 seconds...")
        time.sleep(5)
        sys.exit(1)
    b7 = sys.argv[1]
    b8 = fonk1(b7)
    b3, b4 = fonk2(b8)
    b9 = deepcopy(b1)
    fonk3(b9, b4)
    b10 = deepcopy(b2)
    fonk4(b10, b8)
    b11 = fonk5(b8)
    b10[0x48:0x4C] = (0x18 + b11).to_bytes(4, 'big')
    b10[0x58:0xB2] = b8[0xDC:0x136]
    b12 = b8[b3:b3 + b4]
    b13 = b9 + b10 + b12
    b14 = os.path.splitext(b7)[0] + ".bfwav"
    with open(b14, "wb") as outfile:
        outfile.write(b13)
if b15 = = "__main__":
    fonk6()