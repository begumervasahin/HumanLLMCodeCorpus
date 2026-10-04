import random
from gmpy2 import mpz, mpz_random, powmod, random_state
from Crypto.Cipher import AES
import hashlib
class User:
    def __init__(self, name, a, q):
        self.name = name
        self.a = a
        self.q = q
        temp = sum([ord(i) for i in name])
        self.__X = mpz_random(random_state(temp), q)
        self.Y = powmod(self.a, self.__X, self.q)
        self.__key = {}
        print(f"{self.name}'s master key: {self.__X}")
    def common_key(self, other_user, Yb):
        key = powmod(Yb, self.__X, self.q)
        key = int(key).to_bytes((key.bit_length() + 7)
        key = hashlib.sha256(key).digest()
        print(f"\nCommon key for {self.name} and {other_user.name}: \n{key.hex()}")
        self.__key[other_user.name] = key
    def aes_encrypt(self, other_user, data):
        data = data.encode('utf-8')
        padding = 16 - len(data) % 16
        data += bytes([padding] * padding)
        cryptor = AES.new(self.__key[other_user.name], AES.MODE_CBC, b'\x00' * 16)
        ciphertext = cryptor.encrypt(data)
        print(f"\ncipher: \n{ciphertext.hex()}")
        return [ciphertext, self.name]
    def aes_decrypt(self, ciphertext):
        data, name = ciphertext
        cryptor = AES.new(self.__key[name], AES.MODE_CBC, b'\x00' * 16)
        plaintext = cryptor.decrypt(data)
        plaintext = plaintext[:-plaintext[-1]]
        plaintext = plaintext.decode('utf-8')
        print(f"\nplain from {name}: \n{plaintext}")
        return plaintext
def main():
    a = mpz(11)
    q = mpz(1040699159)
    print(f'a: {a}, q: {q}')
    data = 'I love ncyucsie åå»~~(â§êªâ¦)'
    print(f'Plain: {data}\n')
    alice = User('Alice', a, q)
    bob = User('Bob', a, q)
    alice.common_key(bob, bob.Y)
    bob.common_key(alice, alice.Y)
    encrypted_data = alice.aes_encrypt(bob, data)
    decrypted_data = bob.aes_decrypt(encrypted_data)
if __name__ == "__main__":
    main()