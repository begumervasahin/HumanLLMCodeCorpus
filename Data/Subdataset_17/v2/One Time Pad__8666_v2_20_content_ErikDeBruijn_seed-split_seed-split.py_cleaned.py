import random
ENCRYPTION_FILE = "encryption-cypher.txt"
DECRYPTION_FILE = "component-II-decrypt.txt"
WORD_COUNT = 2048
COLUMNS = 6
random_numbers = random.sample(range(0, WORD_COUNT), WORD_COUNT)
words = []
number_to_word = {}
with open("english.txt", "r") as myfile:
    words = [line.strip() for line in myfile]
with open(ENCRYPTION_FILE, 'w') as f:
    print(f"Generating {ENCRYPTION_FILE} ...")
    f.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    row = ""
    for i, word in enumerate(words):
        row += f"{word:<9}={random_numbers[i]:05d}  "
        number_to_word[random_numbers[i]] = word
        if (i + 1) % COLUMNS == 0:
            f.write(row + "\n")
            row = ""
    if row:
        f.write(row + "\n")
    f.write(f"==== END OF {len(words)} CODES ==== \n")
with open(DECRYPTION_FILE, 'w') as f:
    print(f"Generating {DECRYPTION_FILE} ...")
    f.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
    row = ""
    for i, (number, word) in enumerate(number_to_word.items()):
        row += f"{number:04d}={word:<9}  "
        if (i + 1) % COLUMNS == 0:
            f.write(row + "\n")
            row = ""
    if row:
        f.write(row + "\n")
    f.write(f"==== END OF {len(number_to_word)} CODES ==== \n")
print("Done.")