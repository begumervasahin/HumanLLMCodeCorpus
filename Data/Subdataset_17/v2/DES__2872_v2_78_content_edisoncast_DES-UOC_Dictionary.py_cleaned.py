import crypt
def generate_hash(input_filename, output_filename, salt):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line:
                hashed_line = crypt.crypt(line, salt)
                result = f"{hashed_line} {line}"
                print(result)
                outfile.write(result + "\n")
def filter_lines_of_length(input_filename, output_filename, length=8):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if len(line) == length:
                print(line)
                outfile.write(line + "\n")
if __name__ == "__main__":
    input_file = 'rockyou.txt'
    intermediate_file = 'pec1.txt'
    hashed_file1 = 'hashed1.txt'
    hashed_file2 = 'hashed2.txt'
    salt1 = 'tl'
    salt2 = 'as'
    filter_lines_of_length(input_file, intermediate_file)
    generate_hash(intermediate_file, hashed_file1, salt1)
    generate_hash(intermediate_file, hashed_file2, salt2)