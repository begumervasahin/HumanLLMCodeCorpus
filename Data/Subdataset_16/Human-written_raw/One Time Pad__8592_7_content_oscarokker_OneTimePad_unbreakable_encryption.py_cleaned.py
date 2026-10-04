from secrets import token_bytes
from typing import Tuple
def fonk1(original: b5) -> Tuple[b2, b2]:
    original_bytes: b1 = original.encode()
    dummy: b2 = fonk2(len(original_bytes))
    original_key: b2 = b2.from_bytes(original_bytes, "big")
    encrypted: b2 = original_key ^ dummy
    return dummy, encrypted
def fonk2(length: b2) -> b2:
    tb: b1 = token_bytes(length)
    return b2.from_bytes(tb, "big")
def fonk3(key1: b2, b4: b2) -> b5:
    decrypted: b2 = key1 ^ b4
    temp: b1 = decrypted.to_bytes((decrypted.bit_length() + 7)
    return temp.decode()
if b3 = = "__main__":
    key1, b4 = fonk1("One Time Pad!")
    print(key1)
    print(b4)
    result: b5 = fonk3(key1, b4)
    print(result)