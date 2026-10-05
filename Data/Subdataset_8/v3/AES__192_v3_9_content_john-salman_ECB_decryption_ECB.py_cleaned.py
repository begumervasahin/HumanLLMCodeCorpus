import sys
def read_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
def extract_flags_and_outputs(lines):
    flags = []
    outputs = []
    for line in lines:
        flag_index = line.find(":")
        if flag_index == -1:
            print(f"Warning: ':' not found in line '{line}'. Skipping...")
            continue
        flags.append(line[:flag_index].strip())
        outputs.append(line[flag_index + 1:].strip())
    return flags, outputs
def print_outputs(outputs):
    print(outputs)
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return
    filename = sys.argv[1]
    lines = read_file_contents(filename)
    if lines is None:
        return
    flags, outputs = extract_flags_and_outputs(lines)
    print_outputs(outputs)
if __name__ == "__main__":
    main()