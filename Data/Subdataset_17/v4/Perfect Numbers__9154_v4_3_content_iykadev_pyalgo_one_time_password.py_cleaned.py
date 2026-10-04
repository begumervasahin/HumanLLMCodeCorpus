import hmac
import base64
import struct
import hashlib
import time
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    hmac_hash = hmac.new(key, msg, hashlib.sha1).digest()
    offset = hmac_hash[19] & 0x0F
    code = (struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF) % 1000000
    return code
def get_totp_token(secret):
    intervals_no = int(time.time())
    return get_hotp_token(secret, intervals_no)
if __name__ == "__main__":
    secret = 'MZXW633PN5XW6MZX'
    print("HOTP tokens:")
    for i in range(1, 30):
        print(f"Interval {i}: {get_hotp_token(secret, intervals_no=i)}")
    print("\nCurrent TOTP token:")
    print(get_totp_token(secret))