import struct
import os
def long_to_bytes(n, blocksize=0):
    s = b''
    n = int(n)
    while n > 0:
        s = struct.pack('>I', n & 0xffffffff) + s
        n >>= 32
    for i, byte in enumerate(s):
        if byte != 0:
            break
    else:
        s = b'\x00'
        i = 0
    s = s[i:]
    if blocksize > 0 and len(s) % blocksize:
        s = (blocksize - len(s) % blocksize) * b'\x00' + s
    return s
def strxor(var1, var2):
    return bytes(a ^ b for a, b in zip(var1, var2))
def get_random_bytes(n):
    return os.urandom(n)
def is_writeable_buffer(data):
    return True