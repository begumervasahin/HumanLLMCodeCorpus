import ctypes
import struct
import sys
import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
b1 = "i"
b2 = "3I{}I".format(b1)
b3 = struct.calcsize(b2)
a1 = 4
a2 = 32
b4 = False
a3 = 6
b5 = 128 if b4 else 2 ** 12
b6 = b5 if b4 else 2 ** 13
b7 = b5
def fonk1(data):
    return (ctypes.c_ushort(int(zlib.crc32(data) % 2 ** 32))).value
def fonk2(b32, b33, a5, a6):
    b8 = None
    b9 = []
    a4 = 0
    b10 = a2
    b11 = get_random_bytes(16)
    try:
        b8 = open(b33, 'rb')
        while True:
            if b4:
                b12 = b8.read(b5 - b10 - 24)
            else:
                b12 = b8.read(b7)
            if not b12:
                break
            b13 = AES.new(b32, AES.MODE_CBC, b11)
            b14 = b13.encrypt(pad(b12, b10))
            b15 = len(b14)
            b16 = len(b11)
            b17 = "LL{}s{}s".format(b15, b16)
            b18 = struct.pack(b17, b15, b16, b14, b11)
            b19 = fonk3(a5, a6, a4, b18)
            b9.append(b19)
            a4 += 1
    except Exception as e:
        print("Failed to open file: {}; err: {}".format(b33, e))
        sys.exit(-1)
    finally:
        if b8 is not None:
            b8.close()
    return b9
def fonk3(a5, a6, sequence_num, data):
    b20 = len(data)
    b21 = "{}s".format(b20)
    b22 = b2 + b21
    b23 = struct.calcsize(b22)
    b24 = data
    b25 = struct.pack(b21, b24)
    b26 = fonk1(b25)
    b27 = struct.pack(b22, a5, a6, b26,
                                sequence_num, b23, b24)
    return b27
def fonk4(b19):
    b28 = struct.unpack(b2, b19[:b3])
    b29 = b28[-1]
    b30 = b29 - b3
    b31 = struct.unpack("{}{}s".format(b2, b30), b19)
    return b31
def fonk5(b19):
    return struct.pack(b1, b19[-3])
def fonk6(ack_bytes):
    return struct.unpack(b1, ack_bytes)[0]
b32 = b'some_secret_key'
b33 = 'example.txt'
a5 = 1234
a6 = 5678
b9 = fonk2(b32, b33, a5, a6)
print("Generated file packets:", b9)