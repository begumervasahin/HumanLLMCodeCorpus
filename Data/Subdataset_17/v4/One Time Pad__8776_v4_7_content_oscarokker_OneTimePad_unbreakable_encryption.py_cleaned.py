from secrets import token_bytes
from typing import Tuple
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = generate_random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted
def generate_random_key(length: int) -> int:
    random_bytes: bytes = token_bytes(length)
    return int.from_bytes(random_bytes, "big")
def decrypt(dummy_key: int, encrypted_message: int) -> str:
    decrypted: int = dummy_key ^ encrypted_message
    decrypted_bytes: bytes = decrypted.to_bytes((decrypted.bit_length() + 7)
    return decrypted_bytes.decode()
if __name__ == "__main__":
    dummy_key, encrypted_message = encrypt("One Time Pad!")
    print(f"Dummy Key: {dummy_key}")
    print(f"Encrypted Message: {encrypted_message}")
    decrypted_message: str = decrypt(dummy_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")