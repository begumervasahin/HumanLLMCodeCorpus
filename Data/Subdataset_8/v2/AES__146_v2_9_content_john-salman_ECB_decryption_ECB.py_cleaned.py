import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    flags = []
    outputs = []
    for line in lines:
        i = 5
        end = len(line)
        flag = ""
        output = ""
        while line[i] != ":":
            i += 1
        flags.append(line[:i])
        i += 1
        outputs.append(line[i:end])
    print(outputs)
if __name__ == "__main__":
    main()