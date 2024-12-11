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
if b4:
    a4 = 128
    b5 = a4
else:
    a4 = 2**12
    b5 = 2**13
b6 = a4
def fonk1(data):
    return (ctypes.c_ushort(int(zlib.crc32(data) % 2**32))).value
def fonk2(b31, b32, a6, a7):
    b7 = None
    b8 = []
    a5 = 0
    b9 = a2
    b10 = get_random_bytes(16)
    try:
        b7 = open(b32, 'rb')
        while True:
            if b4:
                b11 = b7.read(a4 - b9 - 24)
            else:
                b11 = b7.read(b6)
            if not b11:
                break
            b12 = AES.new(b31, AES.MODE_CBC, b10)
            b13 = b12.encrypt(pad(b11, b9))
            b14 = len(b13)
            b15 = len(b10)
            b16 = "LL{}s{}s".format(b14, b15)
            b17 = struct.pack(b16, b14, b15, b13, b10)
            b18 = fonk3(a6, a7, a5, b17)
            b8.append(b18)
            a5 += 1
    except Exception as e:
        print("Failed to open file: {}; err: {}".format(b32, e))
        sys.exit(-1)
    finally:
        if b7 is not None:
            b7.close()
    return b8
def fonk3(a6, a7, sequence_num, data):
    b19 = len(data)
    b20 = "{}s".format(b19)
    b21 = b2 + b20
    b22 = struct.calcsize(b21)
    b23 = data
    b24 = struct.pack(b20, b23)
    b25 = fonk1(b24)
    b26 = struct.pack(b21, a6, a7, b25,
                                sequence_num, b22, b23)
    return b26
def fonk4(b18):
    b27 = struct.unpack(b2, b18[:b3])
    b28 = b27[-1]
    b29 = b28 - b3
    b30 = struct.unpack("{}{}s".format(b2, b29), b18)
    return b30
def fonk5(b18):
    return struct.pack(b1, b18[-3])
def fonk6(ack_bytes):
    return struct.unpack(b1, ack_bytes)[0]
b31 = b'some_secret_key'
b32 = 'example.txt'
a6 = 1234
a7 = 5678
b8 = fonk2(b31, b32, a6, a7)
print("Generated file packets:", b8)