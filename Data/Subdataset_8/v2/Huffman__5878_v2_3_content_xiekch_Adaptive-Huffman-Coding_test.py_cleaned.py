def write_file(file_name, data):
    with open(file_name, 'wb') as file:
        for char in data:
            file.write((ord(char)).to_bytes(1, byteorder='little'))
def read_file(file_name):
    with open(file_name, 'rb') as file:
        byte = file.read(1)
        while byte:
            print(chr(int.from_bytes(byte, byteorder='little')), end='')
            byte = file.read(1)
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_file(file_name, data)
    read_file(file_name)