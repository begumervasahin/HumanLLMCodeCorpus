def takeinput(argv):
    if len(argv)<2:
        print("error: found no input")
        return 0,0,0
    else:
        if argv[1]=="encrypt":
            if len(argv)>2:
                if argv[2][:4]=="file":
                    directory = argv[2][5:]
            else:
                directory = input("Enter File-Directory: ").strip()
            if len(argv)>3:
                if argv[3][:3]=="key":
                    key_directory = argv[3][4:]
            else:
                key_directory = input("Enter Key-Directory: ").strip()
            return "encrypt",directory,key_directory
        elif argv[1]=="decrypt":
            if len(argv)>2:
                if argv[2][:4]=="file":
                    directory = argv[2][5:]
            else:
                directory = input("Enter File-Directory: ").strip()
            if len(argv)>3:
                if argv[3][:3]=="key":
                    key_directory = argv[3][4:]
            else:
                key_directory = input("Enter Key-Directory: ").strip()
            return "decrypt",directory,key_directory
        else:
            return 0,0,0