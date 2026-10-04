import sys
import encrypt
def main(decrypt_or_encrypt, passphrase, path, output_type, save_location):
    result = encrypt.enc(decrypt_or_encrypt, passphrase, path, output_type, save_location)
    print(result)
def parse_args(args):
    if len(args) != 6:
        print("Usage: python script.py <encrypt|decrypt> <passphrase> <path> <outputType> <saveLocation>")
        sys.exit(1)
    decrypt_or_encrypt = args[1]
    passphrase = args[2]
    path = args[3]
    output_type = args[4]
    save_location = args[5]
    return decrypt_or_encrypt, passphrase, path, output_type, save_location
if __name__ == "__main__":
    args = sys.argv
    decrypt_or_encrypt, passphrase, path, output_type, save_location = parse_args(args)
    main(decrypt_or_encrypt, passphrase, path, output_type, save_location)