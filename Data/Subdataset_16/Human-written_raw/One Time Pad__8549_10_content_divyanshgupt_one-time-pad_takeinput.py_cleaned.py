def fonk1(argv):
    if len(argv)<2:
        print("error: found no input")
        return 0,0,0
    else:
        if argv[1]=="encrypt":
            if len(argv)>2:
                if argv[2][:4]=="file":
                    b1 = argv[2][5:]
            else:
                b1 = input("Enter File-Directory: ").strip()
            if len(argv)>3:
                if argv[3][:3]=="key":
                    b2 = argv[3][4:]
            else:
                b2 = input("Enter Key-Directory: ").strip()
            return "encrypt",b1,b2
        elif argv[1]=="decrypt":
            if len(argv)>2:
                if argv[2][:4]=="file":
                    b1 = argv[2][5:]
            else:
                b1 = input("Enter File-Directory: ").strip()
            if len(argv)>3:
                if argv[3][:3]=="key":
                    b2 = argv[3][4:]
            else:
                b2 = input("Enter Key-Directory: ").strip()
            return "decrypt",b1,b2
        else:
            return 0,0,0