def write_file(file_name: str, data: str) -> None:
    with open(file_name, 'wb') as file:
        file.write(data.encode('utf-8'))
def read_file(file_name: str) -> None:
    with open(file_name, 'rb') as file:
        for byte in iter(lambda: file.read(1), b''):
            print(byte)
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_file(file_name, data)
    read_file(file_name)