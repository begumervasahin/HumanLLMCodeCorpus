def take_input(argv):
    if len(argv) < 2:
        print("Error: found no input")
        return 0, 0, 0
    action = argv[1]
    file_directory = ""
    key_directory = ""
    if action in ["encrypt", "decrypt"]:
        if len(argv) > 2 and argv[2].startswith("file"):
            file_directory = argv[2][5:]
        else:
            file_directory = input("Enter File-Directory: ").strip()
        if len(argv) > 3 and argv[3].startswith("key"):
            key_directory = argv[3][4:]
        else:
            key_directory = input("Enter Key-Directory: ").strip()
        return action, file_directory, key_directory
    print("Error: invalid action specified")
    return 0, 0, 0