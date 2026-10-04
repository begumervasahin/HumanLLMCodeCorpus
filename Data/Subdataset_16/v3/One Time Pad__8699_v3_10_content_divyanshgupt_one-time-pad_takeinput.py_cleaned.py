import sys
def fonk1(argv):
    if len(argv) < 2:
        print("Error: No input provided.")
        return None, None, None
    b1 = argv[1].lower()
    if b1 not in ["encrypt", "decrypt"]:
        print("Error: Invalid b1. Choose 'encrypt' or 'decrypt'.")
        return None, None, None
    b2 = fonk2(argv, 2, "file:")
    if not b2:
        b2 = input("Enter File Directory: ").strip()
    b3 = fonk2(argv, 3, "key:")
    if not b3:
        b3 = input("Enter Key Directory: ").strip()
    return b1, b2, b3
def fonk2(argv, index, prefix):
    if len(argv) > index and argv[index].startswith(prefix):
        return argv[index][len(prefix):]
    return None
if b4 = = "__main__":
    b1, file_dir, b5 = fonk1(sys.argv)
    if b1:
        print(f"Operation: {b1}")
        print(f"File Directory: {file_dir}")
        print(f"Key Directory: {b5}")