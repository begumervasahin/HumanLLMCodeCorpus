from rsa.key_generator.key_generator import KeyGenerator
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
import math
def read_bytes_from_file(file_path):
    with open(file_path, 'rb') as file_input:
        return file_input.read()
def bytes_to_integers(byte_data):
    return list(byte_data)
def generate_rsa_keys():
    key_generator = KeyGenerator()
    return key_generator.generate()
def encrypt_bytes(public_key, byte_data):
    crypter = Crypt(public_key)
    return crypter.crypt(byte_data)
def decrypt_bytes(private_key, encrypted_data):
    decrypter = Decrypt(private_key)
    return decrypter.decrypt(encrypted_data)
def find_prime_numbers_within_range():
    primes = []
    for num in range(10_000_000_000, 1_000_000_000, -1):
        if all(num % i != 0 for i in range(2, round(math.sqrt(num)) + 1)):
            primes.append(num)
        if len(primes) == 2:
            break
    return primes
def main():
    input_file_path = "files/input.txt"
    read_bytes = read_bytes_from_file(input_file_path)
    dec_bytes = bytes_to_integers(read_bytes)
    private_key, public_key = generate_rsa_keys()
    crypted_bytes = encrypt_bytes(public_key, dec_bytes)
    decrypted_bytes = decrypt_bytes(private_key, crypted_bytes)
    prime_numbers = find_prime_numbers_within_range()
    print("Original Bytes:", read_bytes)
    print("Encrypted Bytes:", crypted_bytes)
    print("Decrypted Bytes:", bytes(decrypted_bytes))
    print("Prime Numbers within Range:", prime_numbers)
if __name__ == "__main__":
    main()