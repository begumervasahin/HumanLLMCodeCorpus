def read_file_as_bytes(file_path):
    file_in_bytes = []
    with open(file_path, 'rb') as file:
        while byte := file.read(1):
            file_in_bytes.append(byte)
    return file_in_bytes
def main(file_path):
    file_bytes = read_file_as_bytes(file_path)
    print(file_bytes)
if __name__ == "__main__":
    file_path = 'path/to/your/file'
    main(file_path)