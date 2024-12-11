import struct
import os
def fonk1(b3, b1 = 0):
    b2 = b''
    b3 = int(b3)
    while b3 > 0:
        b2 = struct.pack('>I', b3 & 0xffffffff) + b2
        b3 >>= 32
    for a1, byte in enumerate(b2):
        if byte != 0:
            break
    else:
        b2 = b'\x00'
        a1 = 0
    b2 = b2[a1:]
    if b1 > 0 and len(b2) % b1:
        b2 = (b1 - len(b2) % b1) * b'\x00' + b2
    return b2
def fonk2(var1, var2):
    return bytes(a ^ b for a, b in zip(var1, var2))
def fonk3(b3):
    return os.urandom(b3)
def fonk4(data):
    return True