def text_file_aligning(file_path, align, line_length):
    if align == "r":
        pattern = "{:>"
    elif align == "l":
        pattern = "{:"
    elif align == "c":
        pattern = "{:^"
    pattern = pattern + str(line_length) + "}"
    with open(file_path, "r") as f:
        for line in f:
            while len(line) > line_length:
                last_space = line[:line_length].rfind(" ")
                print(pattern.format(line[:last_space]))
                line = line[last_space + 1:]
            else:
                print(pattern.format(line.rstrip()))
text_file_aligning("example.txt", "c", 20)