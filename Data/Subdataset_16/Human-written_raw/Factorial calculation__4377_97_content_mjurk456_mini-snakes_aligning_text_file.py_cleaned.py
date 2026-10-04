def fonk1(file, b1, lineLength):
    if b1 = = "r":
        b2 = "{:>"
    elif b1 = = "l":
        b2 = "{:"
    elif b1 = = "c":
        b2 = "{:^"
    b2 = b2 + str(lineLength) + "}"
    b3 = open(file, "r")
    for b6 in b3:
        b4 = []
        a1 = 0
        while len(b6) > lineLength:
            b5 = b6[:lineLength].rfind(" ")
            print(b2.format(b6[:b5]))
            b6 = b6[b5 + 1:]
        else:
            print(b2.format(b6))
    b3.close()