
from rsa.key_generator.key_generator import KeyGenerator
from rsa.crypt.crypt import Crypt
from rsa.decrypt.decrypt import Decrypt
import math
with open("files/input.txt", 'rb') as file_input:
    read_bytes = file_input.read()
dec_bytes = list(read_bytes)
key_generator = KeyGenerator()
private_key, public_key = key_generator.generate()
crypter = Crypt(public_key)
crypted_bytes = crypter.crypt(dec_bytes)
decrypter = Decrypt(private_key)
decrypted_bytes = decrypter.decrypt(crypted_bytes)
def find_prime():
    primes = []
    for num in range(10_000_000_000, 1_000_000_000, -1):
        is_prime = True
        for i in range(2, round(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        if len(primes) == 2:
            break
    print(primes)
print("Original Bytes:", read_bytes)
print("Encrypted Bytes:", crypted_bytes)
print("Decrypted Bytes:", bytes(decrypted_bytes))