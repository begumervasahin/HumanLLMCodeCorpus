import sys
def fonk1(argv):
    if len(argv) < 2:
        print("Error: No input provided")
        return 0, 0, 0
    b1 = argv[1].lower()
    if b1 not in ["encrypt", "decrypt"]:
        print("Error: Invalid b1. Choose 'encrypt' or 'decrypt'.")
        return 0, 0, 0
    if len(argv) > 2 and argv[2].startswith("file:"):
        b2 = argv[2][5:]
    else:
        b2 = input("Enter File Directory: ").strip()
    if len(argv) > 3 and argv[3].startswith("key:"):
        b3 = argv[3][4:]
    else:
        b3 = input("Enter Key Directory: ").strip()
    return b1, b2, b3
if b4 = = "__main__":
    b1, file_dir, b5 = fonk1(sys.argv)
    if b1:
        print(f"Operation: {b1}")
        print(f"File Directory: {file_dir}")
        print(f"Key Directory: {b5}")