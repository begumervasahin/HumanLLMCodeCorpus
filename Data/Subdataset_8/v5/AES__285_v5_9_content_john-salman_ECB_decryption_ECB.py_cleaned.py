import sys
def read_input(filename):
    flags = []
    outputs = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        delimiter_index = line.find(":")
        flag = line[:delimiter_index]
        output = line[delimiter_index + 1:]
        flags.append(flag)
        outputs.append(output)
    return flags, outputs
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return
    filename = sys.argv[1]
    flags, outputs = read_input(filename)
    print(outputs)
if __name__ == "__main__":
    main()