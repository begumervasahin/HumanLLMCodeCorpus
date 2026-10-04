def read_file_as_bytes(file_path):
    with open(file_path, 'rb') as file:
        file_in_bytes = list(file.read())
    return file_in_bytes
def main():
    file_path = 'path/to/your/file'
    file_bytes = read_file_as_bytes(file_path)
    print(file_bytes)
if __name__ == "__main__":
    main()