def write_file(file_name, data):
    with open(file_name, 'wb') as file:
        for ch in data:
            file.write(ch.encode('utf-8'))
def read_file(file_name):
    with open(file_name, 'rb') as file:
        while (byte := file.read(1)):
            print(byte.decode('utf-8', errors='replace'), end='')
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_file(file_name, data)
    read_file(file_name)