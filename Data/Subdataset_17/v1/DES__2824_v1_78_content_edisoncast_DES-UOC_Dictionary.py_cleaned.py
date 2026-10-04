import crypt
def generate_hash(input_filename, output_filename, salt):
    with open(output_filename, "w") as out_file:
        with open(input_filename, 'r') as in_file:
            for line in in_file:
                line = line.strip()
                if line:
                    hashed_line = crypt.crypt(line, salt)
                    result = f"{hashed_line} {line}"
                    print(result)
                    out_file.write(result + "\n")
def des_dictionary(input_filename, output_filename):
    with open(output_filename, "w") as out_file:
        with open(input_filename, 'r') as in_file:
            for line in in_file:
                line = line.strip()
                if len(line) == 8:
                    print(line)
                    out_file.write(line + "\n")
if __name__ == "__main__":
    input_file = 'rockyou.txt'
    intermediate_file = 'pec1.txt'
    hashed_file1 = 'hashed1.txt'
    hashed_file2 = 'hashed2.txt'
    salt1 = 'tl'
    salt2 = 'as'
    des_dictionary(input_file, intermediate_file)
    generate_hash(intermediate_file, hashed_file1, salt1)
    generate_hash(intermediate_file, hashed_file2, salt2)