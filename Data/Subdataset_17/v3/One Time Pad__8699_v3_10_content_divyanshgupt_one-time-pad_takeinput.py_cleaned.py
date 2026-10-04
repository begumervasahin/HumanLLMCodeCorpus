import sys
def take_input(argv):
    if len(argv) < 2:
        print("Error: No input provided.")
        return None, None, None
    operation = argv[1].lower()
    if operation not in ["encrypt", "decrypt"]:
        print("Error: Invalid operation. Choose 'encrypt' or 'decrypt'.")
        return None, None, None
    file_directory = get_directory(argv, 2, "file:")
    if not file_directory:
        file_directory = input("Enter File Directory: ").strip()
    key_directory = get_directory(argv, 3, "key:")
    if not key_directory:
        key_directory = input("Enter Key Directory: ").strip()
    return operation, file_directory, key_directory
def get_directory(argv, index, prefix):
    if len(argv) > index and argv[index].startswith(prefix):
        return argv[index][len(prefix):]
    return None
if __name__ == "__main__":
    operation, file_dir, key_dir = take_input(sys.argv)
    if operation:
        print(f"Operation: {operation}")
        print(f"File Directory: {file_dir}")
        print(f"Key Directory: {key_dir}")