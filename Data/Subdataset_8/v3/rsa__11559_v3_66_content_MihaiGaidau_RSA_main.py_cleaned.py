import io
from keyGenerator import generateRandomNumber, findNearPrime, generateKeys
from encrypt import encrypt
from decrypt import decrypt
MAX_RANDOM_NUMBER = 500
FILE_TO_READ = 'in.txt'
OUT_FILE_ENCRYPTED = 'crypted.txt'
OUT_FILE_DECRYPTED = 'decrypted.txt'
def read_from_file(file_path):
    with io.open(file_path, "r", encoding="utf-8") as file:
        data = file.read()
    return data
def main():
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
    with io.open(OUT_FILE_ENCRYPTED, "w", encoding="utf-8") as out_file_encrypted:
        out_file_encrypted.write(encrypted_data)
    decrypted_data = decrypt(encrypted_data, public_key)
    with io.open(OUT_FILE_DECRYPTED, "w", encoding="utf-8") as out_file_decrypted:
        out_file_decrypted.write(decrypted_data)
if __name__ == "__main__":
    main()