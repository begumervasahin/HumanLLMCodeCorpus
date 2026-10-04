import random
import sys
def encrypt(byte):
    byte = ord(byte)
    keys = []
    keys.append(random.randint(0, 255))
    keys.append(byte ^ keys[0])
    return keys
def decrypt(byte0, byte1):
    keys = []
    keys.append(ord(byte0))
    keys.append(ord(byte1))
    aux = keys[0] ^ keys[1]
    return aux
def encryptFile(input_file, output1, output2):
    with open(input_file, "rb") as f, open(output1, 'wb') as key1File, open(output2, 'wb') as key2File:
        byte = f.read(1)
        while byte:
            aux = encrypt(byte)
            key1File.write(aux[0].to_bytes(1, byteorder="big", signed=False))
            key2File.write(aux[1].to_bytes(1, byteorder="big", signed=False))
            byte = f.read(1)
def decryptFile(input1, input2, output_file):
    with open(input1, "rb") as f1, open(input2, "rb") as f2, open(output_file, 'wb') as output:
        byte1 = f1.read(1)
        byte2 = f2.read(1)
        while byte1 and byte2:
            output.write(decrypt(byte1, byte2).to_bytes(1, byteorder="big", signed=False))
            byte1 = f1.read(1)
            byte2 = f2.read(1)
if __name__ == "__main__":
    print("Starting script...")
    if len(sys.argv) == 2:
        encryptFile(sys.argv[1], sys.argv[1] + ".0", sys.argv[1] + ".1")
    elif len(sys.argv) == 3:
        decryptFile(sys.argv[1], sys.argv[2], sys.argv[1][:-2])
    else:
        print("Argument parsing error.")
    print("Script finished.")