import sys
import encrypt
def main(decrypt_or_encrypt, passphrase, path, output_type, save_location):
    result = encrypt.enc(decrypt_or_encrypt, passphrase, path, output_type, save_location)
    print(result)
if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python script.py <encrypt|decrypt> <passphrase> <path> <outputType> <saveLocation>")
        sys.exit(1)
    decrypt_or_encrypt = sys.argv[1]
    passphrase = sys.argv[2][1:]
    path = sys.argv[3][1:]
    output_type = sys.argv[4]
    save_location = sys.argv[5][1:]
    main(decrypt_or_encrypt, passphrase, path, output_type, save_location)