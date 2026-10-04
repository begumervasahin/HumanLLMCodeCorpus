def write_file(file_name, data):
    with open(file_name, 'wb') as file:
        for ch in data:
            file.write(ord(ch).to_bytes(1, byteorder='little'))
def read_file(file_name):
    with open(file_name, 'rb') as file:
        while (c := file.read(1)):
            print(c)
if __name__ == '__main__':
    file_name = 'test.txt'
    data = 'ä¸­æ'
    write_file(file_name, data)
    read_file(file_name)