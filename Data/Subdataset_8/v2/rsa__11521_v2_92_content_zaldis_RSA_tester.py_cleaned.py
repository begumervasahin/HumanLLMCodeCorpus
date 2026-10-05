
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
from rsa.key_generator.key_generator import KeyGenerator
def read_file_bytes(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def encrypt_decrypt_demo(data_bytes):
    key_generator = KeyGenerator()
    private_key, public_key = key_generator.generate()
    crypter = Crypt(public_key)
    encrypted_bytes = crypter.crypt(list(data_bytes))
    decrypter = Decrypt(private_key)
    decrypted_bytes = decrypter.decrypt(encrypted_bytes)
    print("Encrypted Bytes:", encrypted_bytes)
    print("Decrypted Bytes:", bytes(decrypted_bytes))
def find_two_large_primes():
    import math
    primes = []
    for num in range(10_000, 2, -1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        if len(primes) == 2:
            break
    print("Two Large Prime Numbers:", primes)
if __name__ == "__main__":
    input_bytes = read_file_bytes("files/input.txt")
    print("Input Bytes:", input_bytes)
    encrypt_decrypt_demo(input_bytes)
    find_two_large_primes()