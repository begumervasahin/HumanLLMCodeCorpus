from secrets import token_bytes
from typing import Tuple
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes = original.encode()
    dummy_key = generate_random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted_message = original_key ^ dummy_key
    return dummy_key, encrypted_message
def generate_random_key(length: int) -> int:
    random_bytes = token_bytes(length)
    return int.from_bytes(random_bytes, "big")
def decrypt(dummy_key: int, encrypted_message: int) -> str:
    decrypted_key = dummy_key ^ encrypted_message
    decrypted_bytes = decrypted_key.to_bytes((decrypted_key.bit_length() + 7)
    return decrypted_bytes.decode()
def main():
    message = "One Time Pad!"
    dummy_key, encrypted_message = encrypt(message)
    print(f"Dummy Key: {dummy_key}")
    print(f"Encrypted Message: {encrypted_message}")
    decrypted_message = decrypt(dummy_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
if __name__ == "__main__":
    main()