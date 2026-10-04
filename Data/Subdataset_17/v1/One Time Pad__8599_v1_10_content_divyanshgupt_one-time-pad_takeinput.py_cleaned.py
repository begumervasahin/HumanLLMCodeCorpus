import sys
def take_input(argv):
    if len(argv) < 2:
        print("Error: found no input")
        return 0, 0, 0
    operation = argv[1]
    if operation not in ["encrypt", "decrypt"]:
        return 0, 0, 0
    if len(argv) > 2 and argv[2].startswith("file"):
        file_directory = argv[2][5:]
    else:
        file_directory = input("Enter File-Directory: ").strip()
    if len(argv) > 3 and argv[3].startswith("key"):
        key_directory = argv[3][4:]
    else:
        key_directory = input("Enter Key-Directory: ").strip()
    return operation, file_directory, key_directory
if __name__ == "__main__":
    operation, file_dir, key_dir = take_input(sys.argv)
    if operation:
        print(f"Operation: {operation}")
        print(f"File Directory: {file_dir}")
        print(f"Key Directory: {key_dir}")