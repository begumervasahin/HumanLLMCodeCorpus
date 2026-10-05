def text_file_aligning(file, align, lineLength):
    if align == "r":
        pattern = "{:>"
    elif align == "l":
        pattern = "{:"
    elif align == "c":
        pattern = "{:^"
    pattern = pattern + str(lineLength) + "}"
    f = open(file, "r")
    for line in f:
        mappingSpaces = []
        start = 0
        while len(line) > lineLength:
            p = line[:lineLength].rfind(" ")
            print(pattern.format(line[:p]))
            line = line[p + 1:]
        else:
            print(pattern.format(line))
    f.close()