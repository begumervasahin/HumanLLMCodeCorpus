import random
import sys
def encrypt(byte):
    byte = ord(byte)
    key = random.randint(0, 255)
    encrypted_byte = byte ^ key
    return [key, encrypted_byte]
def decrypt(key_byte, encrypted_byte):
    key = ord(key_byte)
    encrypted = ord(encrypted_byte)
    return key ^ encrypted
def encrypt_file(input_file, key_file, encrypted_file):
    with open(input_file, "rb") as infile, open(key_file, 'wb') as key_out, open(encrypted_file, 'wb') as encrypted_out:
        byte = infile.read(1)
        while byte:
            key, encrypted = encrypt(byte)
            key_out.write(key.to_bytes(1, byteorder="big", signed=False))
            encrypted_out.write(encrypted.to_bytes(1, byteorder="big", signed=False))
            byte = infile.read(1)
def decrypt_file(key_file, encrypted_file, output_file):
    with open(key_file, "rb") as key_in, open(encrypted_file, "rb") as encrypted_in, open(output_file, 'wb') as outfile:
        key_byte = key_in.read(1)
        encrypted_byte = encrypted_in.read(1)
        while key_byte and encrypted_byte:
            decrypted_byte = decrypt(key_byte, encrypted_byte)
            outfile.write(decrypted_byte.to_bytes(1, byteorder="big", signed=False))
            key_byte = key_in.read(1)
            encrypted_byte = encrypted_in.read(1)
if __name__ == "__main__":
    print("Starting script...")
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        encrypt_file(input_file, input_file + ".0", input_file + ".1")
    elif len(sys.argv) == 3:
        key_file = sys.argv[1]
        encrypted_file = sys.argv[2]
        output_file = key_file[:-2]
        decrypt_file(key_file, encrypted_file, output_file)
    else:
        print("Argument parsing error.")
    print("Script finished.")