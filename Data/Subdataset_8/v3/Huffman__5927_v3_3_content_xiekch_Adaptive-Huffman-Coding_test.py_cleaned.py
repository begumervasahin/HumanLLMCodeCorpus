def write_file(file_name, data):
    with open(file_name, 'wb') as file:
        for char in data:
            byte_representation = ord(char).to_bytes(1, byteorder='little')
            file.write(byte_representation)
def read_file(file_name):
    with open(file_name, 'rb') as file:
        while True:
            byte = file.read(1)
            if not byte:
                break
            character = chr(int.from_bytes(byte, byteorder='little'))
            print(character, end='')
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_file(file_name, data)
    read_file(file_name)