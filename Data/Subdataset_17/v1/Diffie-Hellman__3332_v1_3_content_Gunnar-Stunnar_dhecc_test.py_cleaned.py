import os
import Encryption
def generate_random_key():
    random_key = os.urandom(32)
    random_key_int = int.from_bytes(random_key, byteorder='big')
    return random_key_int
def main():
    random_key1 = generate_random_key()
    random_key2 = generate_random_key()
    print(" -=keys=- ")
    print(random_key1)
    print(random_key2)
    part1 = Encryption.AESCipher(random_key1)
    part2 = Encryption.AESCipher(random_key2)
    print("\n-=public keys=-")
    print(part1.getPubKey())
    print(part2.getPubKey())
    part1.DHEC(part2.getPubKey())
    part2.DHEC(part1.getPubKey())
    print("\n-=TEST ROUNDS=-")
    encrypted_message1 = part1.encrypt("howdy" + " " + 128 * ",")
    decrypted_message1 = part2.decrypt(encrypted_message1)
    print(decrypted_message1)
    encrypted_message2 = part2.encrypt("howdy2")
    decrypted_message2 = part1.decrypt(encrypted_message2)
    print(decrypted_message2)
if __name__ == "__main__":
    main()