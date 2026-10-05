import crypt
def generate_hash(input_filename, output_filename, salt):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                stripped_line = line.strip()
                hashed = crypt.crypt(stripped_line, salt)
                result = f"{hashed} {stripped_line}"
                print(result)
                output_file.write(result + "\n")
def filter_plaintexts(input_filename, output_filename):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                stripped_line = line.strip()
                if len(stripped_line) == 8:
                    print(stripped_line)
                    output_file.write(stripped_line + '\n')
def create_filtered_plaintexts(input_filename, output_filename):
    filter_plaintexts(input_filename, output_filename)
def main():
    plaintexts_file = 'rockyou.txt'
    filtered_plaintexts_file = 'pec1.txt'
    create_filtered_plaintexts(plaintexts_file, filtered_plaintexts_file)
    salt1 = 'tl'
    salt2 = 'as'
    generate_hash(filtered_plaintexts_file, 'hashed1.txt', salt1)
    generate_hash(filtered_plaintexts_file, 'hashed2.txt', salt2)
if __name__ == "__main__":
    main()