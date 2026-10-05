import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
MAX_RANDOM_NUMBER = 500
INPUT_FILE = 'in.txt'
ENCRYPTED_FILE = 'crypted.txt'
DECRYPTED_FILE = 'decrypted.txt'
def read_from_file(file):
    with io.open(file, "r+", encoding="utf-8") as file_handle:
        data = file_handle.read()
    return data
def main():
    with io.open(ENCRYPTED_FILE, "w", encoding="utf-8") as encrypted_out, io.open(DECRYPTED_FILE, "w", encoding="utf-8") as decrypted_out:
        random1 = generateRandomNumber(MAX_RANDOM_NUMBER)
        random2 = generateRandomNumber(MAX_RANDOM_NUMBER)
        prime1 = findNearPrime(random1)
        prime2 = findNearPrime(random2)
        private_key, public_key = generateKeys(prime1, prime2)
        print("Private Key:", private_key)
        print("Public Key:", public_key)
        text_to_encrypt = read_from_file(INPUT_FILE)
        encrypted_data = encrypt(text_to_encrypt, private_key)
        print("Encrypted data:", encrypted_data)
        encrypted_out.write(encrypted_data)
        decrypted_data = decrypt(encrypted_data, public_key)
        decrypted_out.write(decrypted_data)
if __name__ == "__main__":
    main()