import hmac
import base64
import struct
import hashlib
import time
def fonk1(b8, b6):
    b1 = base64.b32decode(b8, True)
    b2 = struct.pack(">Q", b6)
    b3 = hmac.new(b1, b2, hashlib.sha1).digest()
    b4 = b3[19] & 0x0F
    b5 = (struct.unpack(">I", b3[b4:b4 + 4])[0] & 0x7FFFFFFF) % 1000000
    return b5
def fonk2(b8):
    b6 = int(time.time())
    return fonk1(b8, b6)
if b7 = = "__main__":
    b8 = 'MZXW633PN5XW6MZX'
    print("HOTP tokens:")
    for i in range(1, 30):
        print(f"Interval {i}: {fonk1(b8, b6 = i)}")
    print("\nCurrent TOTP token:")
    print(fonk2(b8))