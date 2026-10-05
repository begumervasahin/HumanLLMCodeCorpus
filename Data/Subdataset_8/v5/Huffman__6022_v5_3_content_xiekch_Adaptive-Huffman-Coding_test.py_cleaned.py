def write_bytes_to_file(file_name, data):
    with open(file_name, 'wb') as file:
        for ch in data:
            file.write((ord(ch)).to_bytes(1, byteorder='little'))
def read_bytes_from_file(file_name):
    with open(file_name, 'rb') as file:
        while True:
            byte = file.read(1)
            if not byte:
                break
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_bytes_to_file(file_name, data)
    read_bytes_from_file(file_name)