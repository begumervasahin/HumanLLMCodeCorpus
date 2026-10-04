import sys
def parse_line(line):
    line = line.strip()
    key_part, value_part = line.split(',')
    word_part, word = key_part.split('=')
    word = word.strip()
    _, count_str = value_part.split("&")[3].split("=")
    count = int(count_str.strip())
    return word, count
def process_lines(input_lines):
    file_count = {}
    current_word = None
    current_count = 0
    for line in input_lines:
        try:
            word, count = parse_line(line)
        except ValueError:
            continue
        if current_word == word:
            current_count += count
        else:
            if current_word is not None:
                file_count[current_word] = current_count
            current_word = word
            current_count = count
    if current_word == word:
        file_count[current_word] = current_count
    return file_count
def format_output(input_lines, file_count):
    for line in input_lines:
        line = line.strip()
        key_part, value_part = line.split(',')
        word_part, word = key_part.split('=')
        word = word.strip()
        value_parts = value_part.split("=")[1].split("&")
        file_name, n, total = value_parts[0], value_parts[1], value_parts[2]
        total_file_count = str(file_count[word])
        print(f"key={word}&{file_name}, value={n}&{total}&{total_file_count}")
def main():
    input_lines = [line.strip() for line in sys.stdin]
    file_count = process_lines(input_lines)
    format_output(input_lines, file_count)
if __name__ == "__main__":
    main()