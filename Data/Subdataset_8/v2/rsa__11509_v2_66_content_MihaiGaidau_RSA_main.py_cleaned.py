import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
MAX_RANDOM_NUMBER = 500
FILE_TO_READ = 'in.txt'
OUT_FILE = 'crypted.txt'
OUT_FILE2 = 'decrypted.txt'
def read_from_file(file_path):
    with io.open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
    return data
def main():
    with io.open(OUT_FILE, "w", encoding="utf-8") as out_file, \
         io.open(OUT_FILE2, "w", encoding="utf-8") as out_file2:
        random1 = generateRandomNumber(MAX_RANDOM_NUMBER)
        random2 = generateRandomNumber(MAX_RANDOM_NUMBER)
        prime1 = findNearPrime(random1)
        prime2 = findNearPrime(random2)
        private_key, public_key = generateKeys(prime1, prime2)
        print("Private Key:", private_key)
        print("Public Key:", public_key)
        text_to_encrypt = read_from_file(FILE_TO_READ)
        encrypted_data = encrypt(text_to_encrypt, private_key)
        print("Encrypted Data:", encrypted_data)
        out_file.write(encrypted_data)
        decrypted_data = decrypt(encrypted_data, public_key)
        out_file2.write(decrypted_data)
if __name__ == "__main__":
    main()