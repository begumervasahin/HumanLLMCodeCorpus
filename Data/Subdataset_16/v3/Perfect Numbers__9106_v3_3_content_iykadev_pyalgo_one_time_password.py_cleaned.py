import hmac
import base64
import struct
import hashlib
import time
def fonk1(b9, b8):
    b1 = base64.b32decode(b9, True)
    b2 = struct.pack(">Q", b8)
    b3 = hmac.new(b1, b2, hashlib.sha1).digest()
    b4 = b3[19] & 15
    b5 = struct.unpack(">I", b3[b4:b4+4])[0] & 0x7fffffff
    b6 = b5 % 1000000
    return b6
def fonk2(b9):
    b7 = int(time.time())
    return fonk1(b9, b8 = b7)
def fonk3():
    b9 = 'MZXW633PN5XW6MZX'
    print("HOTP Tokens:")
    for interval in range(1, 30):
        b6 = fonk1(b9, b8=interval)
        print(f"Interval {interval}: {b6}")
    b10 = fonk2(b9)
    print(f"Current TOTP token: {b10}")
if b11 = = "__main__":
    fonk3()