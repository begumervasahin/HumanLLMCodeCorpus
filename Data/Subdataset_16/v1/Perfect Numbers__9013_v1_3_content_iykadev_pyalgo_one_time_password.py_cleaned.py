import hmac
import base64
import struct
import hashlib
import time
def fonk1(b6, b5):
    b1 = base64.b32decode(b6, True)
    b2 = struct.pack(">Q", b5)
    b3 = hmac.new(b1, b2, hashlib.sha1).digest()
    b4 = b3[19] & 15
    b3 = (struct.unpack(">I", b3[b4:b4+4])[0] & 0x7fffffff) % 1000000
    return b3
def fonk2(b6):
    return fonk1(b6, b5 = int(time.time())
b6 = 'MZXW633PN5XW6MZX'
for i in range(1, 30):
    print(i, fonk1(b6, b5 = i))
print("Current TOTP token:", fonk2(b6))