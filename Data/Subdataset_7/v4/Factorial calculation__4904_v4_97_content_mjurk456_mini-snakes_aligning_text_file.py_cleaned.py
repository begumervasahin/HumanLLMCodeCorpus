def fonk1(file_path, b1, line_length):
    if b1 = = "r":
        b2 = "{:>"
    elif b1 = = "l":
        b2 = "{:"
    elif b1 = = "c":
        b2 = "{:^"
    b2 = b2 + str(line_length) + "}"
    with open(file_path, "r") as file:
        for b4 in file:
            while len(b4) > line_length:
                b3 = b4[:line_length].rfind(" ")
                print(b2.format(b4[:b3]))
                b4 = b4[b3 + 1:]
            else:
                print(b2.format(b4.rstrip()))
fonk1("example.txt", "c", 20)