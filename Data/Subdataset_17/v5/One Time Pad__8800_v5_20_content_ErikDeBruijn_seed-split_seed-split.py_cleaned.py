import random
encryption_filename = "encryption-cypher.txt"
decryption_filename = "component-II-decrypt.txt"
word_count = 2048
columns = 6
random_numbers = random.sample(range(word_count), word_count)
words = []
number_to_word = {}
with open("english.txt", "r") as file:
    for line in file:
        words.append(line.strip())
print(f"Generating {encryption_filename} ...")
with open(encryption_filename, 'w') as enc_file:
    enc_file.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    line_buffer = ""
    for index, word in enumerate(words):
        line_buffer += f"{word:<9}={random_numbers[index]:05d} "
        number_to_word[random_numbers[index]] = word
        if (index + 1) % columns == 0:
            enc_file.write(line_buffer.strip() + "\n")
            line_buffer = ""
    if line_buffer:
        enc_file.write(line_buffer.strip() + "\n")
    enc_file.write(f"==== END OF {index + 1} CODES ====\n")
print(f"Generating {decryption_filename} ...")
with open(decryption_filename, 'w') as dec_file:
    dec_file.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cipher) ====\n")
    line_buffer = ""
    for index, (number, word) in enumerate(number_to_word.items()):
        line_buffer += f"{number:04d}={word:<9} "
        if (index + 1) % columns == 0:
            dec_file.write(line_buffer.strip() + "\n")
            line_buffer = ""
    if line_buffer:
        dec_file.write(line_buffer.strip() + "\n")
    dec_file.write(f"==== END OF {index + 1} CODES ====\n")
print("Done.")
import random
encryption_filename = "encryption-cypher.txt"
decryption_filename = "component-II-decrypt.txt"
word_count = 2048
columns = 6
random_numbers = random.sample(range(word_count), word_count)
words = []
number_to_word = {}
with open("english.txt", "r") as file:
    for line in file:
        words.append(line.strip())
print(f"Generating {encryption_filename} ...")
with open(encryption_filename, 'w') as enc_file:
    enc_file.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    line_buffer = ""
    for index, word in enumerate(words):
        line_buffer += f"{word:<9}={random_numbers[index]:05d} "
        number_to_word[random_numbers[index]] = word
        if (index + 1) % columns == 0:
            enc_file.write(line_buffer.strip() + "\n")
            line_buffer = ""
    if line_buffer:
        enc_file.write(line_buffer.strip() + "\n")
    enc_file.write(f"==== END OF {index + 1} CODES ====\n")
print(f"Generating {decryption_filename} ...")
with open(decryption_filename, 'w') as dec_file:
    dec_file.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cipher) ====\n")
    line_buffer = ""
    for index, (number, word) in enumerate(number_to_word.items()):
        line_buffer += f"{number:04d}={word:<9} "
        if (index + 1) % columns == 0:
            dec_file.write(line_buffer.strip() + "\n")
            line_buffer = ""
    if line_buffer:
        dec_file.write(line_buffer.strip() + "\n")
    dec_file.write(f"==== END OF {index + 1} CODES ====\n")
print("Done.")