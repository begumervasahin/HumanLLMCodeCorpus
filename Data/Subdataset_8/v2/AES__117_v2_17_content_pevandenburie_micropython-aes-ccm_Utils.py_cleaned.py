import struct
import os
def long_to_bytes(n, blocksize=0):
    result_bytes = b''
    n = int(n)
    while n > 0:
        result_bytes = struct.pack('>I', n & 0xffffffff) + result_bytes
        n >>= 32
    for i in range(len(result_bytes)):
        if result_bytes[i] != 0:
            break
    else:
        result_bytes = b'\x00'
        i = 0
    result_bytes = result_bytes[i:]
    if blocksize > 0 and len(result_bytes) % blocksize:
        result_bytes = (blocksize - len(result_bytes) % blocksize) * b'\x00' + result_bytes
    return result_bytes
def strxor(var1, var2):
    return bytes([a ^ b for (a, b) in zip(var1, var2)])
def get_random_bytes(n):
    return os.urandom(n)
def is_writeable_buffer(data):
    return True