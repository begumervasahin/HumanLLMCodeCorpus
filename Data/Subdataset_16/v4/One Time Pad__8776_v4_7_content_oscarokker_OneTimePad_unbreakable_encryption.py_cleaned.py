from secrets import token_bytes
from typing import Tuple
def fonk1(original: b5) -> Tuple[b2, b2]:
    original_bytes: b1 = original.encode()
    dummy: b2 = fonk2(len(original_bytes))
    original_key: b2 = b2.from_bytes(original_bytes, "big")
    encrypted: b2 = original_key ^ dummy
    return dummy, encrypted
def fonk2(length: b2) -> b2:
    random_bytes: b1 = token_bytes(length)
    return b2.from_bytes(random_bytes, "big")
def fonk3(dummy_key: b2, b4: b2) -> b5:
    decrypted: b2 = dummy_key ^ b4
    decrypted_bytes: b1 = decrypted.to_bytes((decrypted.bit_length() + 7)
    return decrypted_bytes.decode()
if b3 = = "__main__":
    dummy_key, b4 = fonk1("One Time Pad!")
    print(f"Dummy Key: {dummy_key}")
    print(f"Encrypted Message: {b4}")
    decrypted_message: b5 = fonk3(dummy_key, b4)
    print(f"Decrypted Message: {decrypted_message}")