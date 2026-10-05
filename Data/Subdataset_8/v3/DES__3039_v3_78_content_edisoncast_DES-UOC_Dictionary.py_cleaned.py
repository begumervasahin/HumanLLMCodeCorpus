import crypt
def generate_hash(input_filename, output_filename, salt):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                hashed = crypt.crypt(line, salt)
                result = f"{hashed} {line}\n"
                print(result)
                output_file.write(result)
def filter_plaintexts(input_filename, output_filename):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if len(line) == 8:
                    print(line)
                    output_file.write(line + '\n')
def main():
    input_filename = 'rockyou.txt'
    intermediate_filename = 'pec1.txt'
    output_filename1 = 'hashed1.txt'
    output_filename2 = 'hashed2.txt'
    filter_plaintexts(input_filename, intermediate_filename)
    salt1 = 'tl'
    salt2 = 'as'
    generate_hash(intermediate_filename, output_filename1, salt1)
    generate_hash(intermediate_filename, output_filename2, salt2)
if __name__ == "__main__":
    main()