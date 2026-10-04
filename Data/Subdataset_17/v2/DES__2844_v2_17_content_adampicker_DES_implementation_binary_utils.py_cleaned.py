def read_binary_file(file_path):
    binary_string = ''
    with open(file_path, 'rb') as file:
        file_bytes = file.read()
    for byte in file_bytes:
        binary_string += bin(byte)[2:].zfill(8)
    return binary_string
def write_binary_file(binary_str):
    byte_array = bytearray()
    for i in range(0, len(binary_str), 8):
        byte_segment = binary_str[i:i+8]
        byte_array.append(int(byte_segment, 2))
    return byte_array
def hex_key_to_binary(hex_key):
    binary_key = ''.join("{:04b}".format(int(char, 16)) for char in hex_key)
    return binary_key
def main():
    file_path = 'example.bin'
    binary_content = read_binary_file(file_path)
    print("Binary content of file:", binary_content)
    byte_array = write_binary_file(binary_content)
    print("Bytearray:", byte_array)
    hex_key = '1a2b3c'
    binary_key = hex_key_to_binary(hex_key)
    print("Binary key:", binary_key)
if __name__ == "__main__":
    main()