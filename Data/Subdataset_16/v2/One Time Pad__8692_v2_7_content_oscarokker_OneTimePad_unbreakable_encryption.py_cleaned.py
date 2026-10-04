import random
from secrets import token_bytes
from typing import Tuple
def fonk1(length: b2) -> b2:
    tb: b1 = token_bytes(length)
    return b2.from_bytes(tb, "big")
def fonk2(original: b5) -> Tuple[b2, b2]:
    original_bytes: b1 = original.encode()
    dummy: b2 = fonk1(len(original_bytes))
    original_key: b2 = b2.from_bytes(original_bytes, "big")
    encrypted: b2 = original_key ^ dummy
    return dummy, encrypted
def fonk3(key1: b2, b4: b2) -> b5:
    decrypted: b2 = key1 ^ b4
    temp: b1 = decrypted.to_bytes((decrypted.bit_length() + 7)
    return temp.decode()
def fonk4():
    b3 = "One Time Pad!"
    key1, b4 = fonk2(b3)
    print(f"Key 1: {key1}")
    print(f"Key 2: {b4}")
    decrypted_message: b5 = fonk3(key1, b4)
    print(f"Decrypted result: {decrypted_message}")
if b6 = = "__main__":
    fonk4()