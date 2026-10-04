def text_file_aligning(file_path, align, line_length):
    if align == 'r':
        pattern = '{:>'
    elif align == 'l':
        pattern = '{:'
    elif align == 'c':
        pattern = '{:^'
    else:
        raise ValueError("Invalid alignment option. Use 'r', 'l', or 'c'.")
    pattern += str(line_length) + '}'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                while len(line) > line_length:
                    split_pos = line[:line_length].rfind(' ')
                    if split_pos == -1:
                        split_pos = line_length
                    print(pattern.format(line[:split_pos]))
                    line = line[split_pos:].lstrip()
                print(pattern.format(line))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python script.py <file_path> <alignment> <line_length>")
        sys.exit(1)
    file_path = sys.argv[1]
    align = sys.argv[2]
    try:
        line_length = int(sys.argv[3])
    except ValueError:
        print("Error: Line length must be an integer.")
        sys.exit(1)
    text_file_aligning(file_path, align, line_length)