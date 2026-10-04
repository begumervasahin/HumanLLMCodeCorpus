def read_binary_file(filename_path):
    string_binary = ''
    with open(filename_path, mode='rb') as file:
        file_bytes = file.read()
    for byte in file_bytes:
        binary_str = bin(byte)[2:].zfill(8)
        string_binary += binary_str
    return string_binary
def write_binary_file(binary):
    byte_array = bytearray()
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        byte_array.append(int(byte, 2))
    return byte_array
def hex_key_to_binary(hex_key):
    binary_key = ''.join("{:04b}".format(int(char, 16)) for char in hex_key)
    return binary_key
if __name__ == "__main__":
    filename_path = 'example.bin'
    binary_content = read_binary_file(filename_path)
    print("Binary content of file:", binary_content)
    byte_array = write_binary_file(binary_content)
    print("Bytearray:", byte_array)
    hex_key = '1a2b3c'
    binary_key = hex_key_to_binary(hex_key)
    print("Binary key:", binary_key)