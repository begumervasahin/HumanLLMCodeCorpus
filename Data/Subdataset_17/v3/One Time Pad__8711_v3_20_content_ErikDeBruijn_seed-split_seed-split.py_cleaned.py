import random
ENCRYPTION_FILE = "encryption-cypher.txt"
DECRYPTION_FILE = "component-II-decrypt.txt"
WORD_COUNT = 2048
COLUMNS = 6
def read_words(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]
def generate_random_numbers(count, max_value):
    return random.sample(range(max_value), count)
def write_encryption_sheet(filename, words, random_numbers, columns):
    with open(filename, 'w') as file:
        print(f"Generating {filename} ...")
        file.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
        row = ""
        for i, word in enumerate(words):
            row += f"{word:<9}={random_numbers[i]:05d}  "
            if (i + 1) % columns == 0:
                file.write(row + "\n")
                row = ""
        if row:
            file.write(row + "\n")
        file.write(f"==== END OF {len(words)} CODES ====\n")
def write_decryption_sheet(filename, number_to_word, columns):
    with open(filename, 'w') as file:
        print(f"Generating {filename} ...")
        file.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
        row = ""
        for i, (number, word) in enumerate(number_to_word.items()):
            row += f"{number:04d}={word:<9}  "
            if (i + 1) % columns == 0:
                file.write(row + "\n")
                row = ""
        if row:
            file.write(row + "\n")
        file.write(f"==== END OF {len(number_to_word)} CODES ====\n")
def main():
    words = read_words("english.txt")
    random_numbers = generate_random_numbers(WORD_COUNT, WORD_COUNT)
    number_to_word = dict(zip(random_numbers, words))
    write_encryption_sheet(ENCRYPTION_FILE, words, random_numbers, COLUMNS)
    write_decryption_sheet(DECRYPTION_FILE, number_to_word, COLUMNS)
    print("Done.")
if __name__ == "__main__":
    main()