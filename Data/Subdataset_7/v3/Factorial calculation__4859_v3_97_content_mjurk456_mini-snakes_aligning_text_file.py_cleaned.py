def fonk1(file_path, align, line_length):
    b1 = {'r': '{:>', 'l': '{:', 'c': '{:^'}
    b2 = b1.get(align, '{:>') + str(line_length) + "}"
    with open(file_path, "r") as file:
        for b4 in file:
            while len(b4) > line_length:
                b3 = b4[:line_length].rfind(" ")
                print(b2.format(b4[:b3]))
                b4 = b4[b3 + 1:]
            else:
                print(b2.format(b4.rstrip()))
fonk1("example.txt", "c", 20)