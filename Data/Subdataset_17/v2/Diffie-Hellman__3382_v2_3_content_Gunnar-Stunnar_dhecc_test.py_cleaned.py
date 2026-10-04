import os
import Encryption
def generate_random_key():
    random_key = os.urandom(32)
    return int.from_bytes(random_key, byteorder='big')
def display_keys(key1, key2):
    print(" -=keys=- ")
    print(key1)
    print(key2)
def display_public_keys(part1, part2):
    print("\n-=public keys=-")
    print(part1.getPubKey())
    print(part2.getPubKey())
def perform_diffie_hellman_exchange(part1, part2):
    part1.DHEC(part2.getPubKey())
    part2.DHEC(part1.getPubKey())
def test_encryption_decryption(part1, part2):
    print("\n-=TEST ROUNDS=-")
    encrypted_message1 = part1.encrypt("howdy" + " " + 128 * ",")
    decrypted_message1 = part2.decrypt(encrypted_message1)
    print(decrypted_message1)
    encrypted_message2 = part2.encrypt("howdy2")
    decrypted_message2 = part1.decrypt(encrypted_message2)
    print(decrypted_message2)
def main():
    random_key1 = generate_random_key()
    random_key2 = generate_random_key()
    display_keys(random_key1, random_key2)
    part1 = Encryption.AESCipher(random_key1)
    part2 = Encryption.AESCipher(random_key2)
    display_public_keys(part1, part2)
    perform_diffie_hellman_exchange(part1, part2)
    test_encryption_decryption(part1, part2)
if __name__ == "__main__":
    main()