import crypt
def generate_hash(input_filename, output_filename, salt):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                hashed = crypt.crypt(line.strip(), salt)
                result = f"{hashed} {line}"
                print(result)
                output_file.write(result + "\n")
def filter_plaintexts(input_filename, output_filename):
    with open(output_filename, "w") as output_file:
        with open(input_filename, 'r') as input_file:
            for line in input_file:
                if len(line.strip()) == 8:
                    print(line)
                    output_file.write(line)
def main():
    plaintexts_file = 'rockyou.txt'
    filtered_plaintexts_file = 'pec1.txt'
    DESDictionary(plaintexts_file, filtered_plaintexts_file)
    salt1 = 'tl'
    salt2 = 'as'
    generateHash(filtered_plaintexts_file, 'hashed1.txt', salt1)
    generateHash(filtered_plaintexts_file, 'hashed2.txt', salt2)
if __name__ == "__main__":
    main()