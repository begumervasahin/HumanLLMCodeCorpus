def fonk1(argv):
    if len(argv) < 2:
        print("Error: found no input")
        return 0, 0, 0
    b1 = argv[1]
    b2 = ""
    b3 = ""
    if b1 = = "encrypt" or b1 == "decrypt":
        if len(argv) > 2 and argv[2].startswith("file"):
            b2 = argv[2][5:]
        else:
            b2 = input("Enter File-Directory: ").strip()
        if len(argv) > 3 and argv[3].startswith("key"):
            b3 = argv[3][4:]
        else:
            b3 = input("Enter Key-Directory: ").strip()
        return b1, b2, b3
    print("Error: invalid b1 specified")
    return 0, 0, 0