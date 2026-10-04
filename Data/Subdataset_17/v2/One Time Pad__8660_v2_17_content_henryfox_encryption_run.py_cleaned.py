import sys
import encrypt
def main() -> None:
    if len(sys.argv) != 6:
        print("Usage: python script.py <encrypt/decrypt> <passphrase> <path> <outputType> <saveLocation>")
        return
    operation = sys.argv[1]
    passphrase = sys.argv[2][1:]
    path = sys.argv[3][1:]
    output_type = sys.argv[4]
    save_location = sys.argv[5][1:]
    result = encrypt.enc(operation, passphrase, path, output_type, save_location)
    print(result)
if __name__ == "__main__":
    main()