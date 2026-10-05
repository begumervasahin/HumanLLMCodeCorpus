def text_file_aligning(file_path, align, line_length):
    alignment_patterns = {'r': '{:>', 'l': '{:', 'c': '{:^'}
    pattern = alignment_patterns.get(align, '{:>') + str(line_length) + "}"
    with open(file_path, "r") as file:
        for line in file:
            while len(line) > line_length:
                last_space = line[:line_length].rfind(" ")
                print(pattern.format(line[:last_space]))
                line = line[last_space + 1:]
            else:
                print(pattern.format(line.rstrip()))
text_file_aligning("example.txt", "c", 20)