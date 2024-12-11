import ctypes
import struct
import sys
import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
b1 = "i"
b2 = f"3I{b1}I"
b3 = struct.calcsize(b2)
a1 = 4
a2 = 32
b4 = False
a3 = 6
b5 = 128 if b4 else 2 ** 12
b6 = b5
b7 = b5
def fonk1(data):
    return ctypes.c_ushort(zlib.crc32(data) % (2 ** 32)).value
def fonk2(session_key, file_path, source_port, destination_port):
    b8 = []
    b9 = a2
    b10 = get_random_bytes(16)
    try:
        with open(file_path, 'rb') as input_file:
            a4 = 0
            while True:
                if b4:
                    b11 = input_file.read(b5 - b9 - 24)
                else:
                    b11 = input_file.read(b7)
                if not b11:
                    break
                b12 = AES.new(session_key, AES.MODE_CBC, b10)
                b13 = b12.encrypt(pad(b11, b9))
                b14 = len(b13)
                b15 = len(b10)
                b16 = f"LL{b14}s{b15}s"
                b17 = struct.pack(b16, b14, b15, b13, b10)
                b18 = fonk3(source_port, destination_port, a4, b17)
                b8.append(b18)
                a4 += 1
    except Exception as e:
        print(f"Failed to open file: {file_path}; err: {e}")
        sys.exit(-1)
    return b8
def fonk3(source_port, destination_port, sequence_num, data):
    b19 = len(data)
    b20 = f"{b19}s"
    b21 = f"{b2}{b20}"
    b22 = struct.calcsize(b21)
    b23 = data
    b24 = struct.pack(b20, b23)
    b25 = fonk1(b24)
    b26 = struct.pack(
        b21,
        source_port,
        destination_port,
        b25,
        sequence_num,
        b22,
        b23
    )
    return b26
def fonk4(b18):
    b27 = struct.unpack(b2, b18[:b3])
    b28 = b27[-1]
    b29 = b28 - b3
    b30 = struct.unpack(f"{b2}{b29}s", b18)
    return b30
def fonk5(b18):
    return struct.pack(b1, b18[-3])
def fonk6(ack_bytes):
    return struct.unpack(b1, ack_bytes)[0]