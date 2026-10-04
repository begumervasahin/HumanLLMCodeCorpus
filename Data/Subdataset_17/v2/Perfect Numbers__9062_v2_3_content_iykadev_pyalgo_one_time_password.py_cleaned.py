import hmac
import base64
import struct
import hashlib
import time
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    hmac_hash = hmac.new(key, msg, hashlib.sha1).digest()
    offset = hmac_hash[19] & 15
    binary_code = struct.unpack(">I", hmac_hash[offset:offset+4])[0] & 0x7fffffff
    hotp_token = binary_code % 1000000
    return hotp_token
def get_totp_token(secret):
    time_step = int(time.time())
    return get_hotp_token(secret, intervals_no=time_step)
secret = 'MZXW633PN5XW6MZX'
print("HOTP Tokens:")
for interval in range(1, 30):
    print(f"Interval {interval}: {get_hotp_token(secret, intervals_no=interval)}")
current_totp_token = get_totp_token(secret)
print(f"Current TOTP token: {current_totp_token}")