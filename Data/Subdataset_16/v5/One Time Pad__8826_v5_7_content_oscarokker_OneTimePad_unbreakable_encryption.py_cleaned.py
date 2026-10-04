from secrets import token_bytes
from typing import Tuple
def fonk1(original: str) -> Tuple[int, int]:
    b1 = original.encode()
    b2 = fonk2(len(b1))
    b3 = int.from_bytes(b1, "big")
    b4 = b3 ^ b2
    return b2, b4
def fonk2(length: int) -> int:
    b5 = token_bytes(length)
    return int.from_bytes(b5, "big")
def fonk3(b2: int, b4: int) -> str:
    b6 = b2 ^ b4
    b7 = b6.to_bytes((b6.bit_length() + 7)
    return b7.decode()
def fonk4():
    b8 = "One Time Pad!"
    b2, b4 = fonk1(b8)
    print(f"Dummy Key: {b2}")
    print(f"Encrypted Message: {b4}")
    b9 = fonk3(b2, b4)
    print(f"Decrypted Message: {b9}")
if b10 = = "__main__":
    fonk4()