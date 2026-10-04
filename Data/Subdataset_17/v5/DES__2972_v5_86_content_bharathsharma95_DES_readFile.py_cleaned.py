def read_file_as_bytes(file_path):
    with open(file_path, 'rb') as file:
        return list(file.read())
def main():
    file_path = 'path/to/your/file'
    try:
        file_bytes = read_file_as_bytes(file_path)
        print(file_bytes)
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()