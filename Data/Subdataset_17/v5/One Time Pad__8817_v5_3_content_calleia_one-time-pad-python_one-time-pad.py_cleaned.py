import random
import sys
def encrypt(byte):
    byte = byte[0]
    key = random.randint(0, 255)
    encrypted_byte = byte ^ key
    return key, encrypted_byte
def decrypt(key, encrypted_byte):
    key = key[0]
    encrypted_byte = encrypted_byte[0]
    return key ^ encrypted_byte
def encrypt_file(input_filename, key1_filename, key2_filename):
    with open(input_filename, "rb") as infile, \
         open(key1_filename, 'wb') as key1_file, \
         open(key2_filename, 'wb') as key2_file:
        byte = infile.read(1)
        while byte:
            key, encrypted_byte = encrypt(byte)
            key1_file.write(key.to_bytes(1, byteorder="big", signed=False))
            key2_file.write(encrypted_byte.to_bytes(1, byteorder="big", signed=False))
            byte = infile.read(1)
def decrypt_file(key1_filename, key2_filename, output_filename):
    with open(key1_filename, "rb") as key1_file, \
         open(key2_filename, "rb") as key2_file, \
         open(output_filename, 'wb') as outfile:
        byte1 = key1_file.read(1)
        byte2 = key2_file.read(1)
        while byte1 and byte2:
            decrypted_byte = decrypt(byte1, byte2)
            outfile.write(decrypted_byte.to_bytes(1, byteorder="big", signed=False))
            byte1 = key1_file.read(1)
            byte2 = key2_file.read(1)
if __name__ == "__main__":
    print("Starting script...")
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        encrypt_file(input_file, input_file + ".0", input_file + ".1")
    elif len(sys.argv) == 3:
        key1_file = sys.argv[1]
        key2_file = sys.argv[2]
        output_file = key1_file[:-2]
        decrypt_file(key1_file, key2_file, output_file)
    else:
        print("Argument parsing error. Usage:")
        print("  To encrypt: python script.py <input_file>")
        print("  To decrypt: python script.py <key1_file> <key2_file>")
    print("Script finished.")