def write_file(file_name: str, data: str) -> None:
    with open(file_name, 'wb') as file:
        file.write(data.encode('utf-8'))
def read_file(file_name: str) -> None:
    with open(file_name, 'rb') as file:
        content = file.read()
        print(content.decode('utf-8', errors='replace'))
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_file(file_name, data)
    read_file(file_name)