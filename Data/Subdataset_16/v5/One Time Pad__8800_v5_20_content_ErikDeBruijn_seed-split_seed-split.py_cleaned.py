import random
b1 = "encryption-cypher.txt"
b2 = "component-II-decrypt.txt"
a1 = 2048
a2 = 6
b3 = random.sample(range(a1), a1)
b4 = []
b5 = {}
with open("english.txt", "r") as file:
    for line in file:
        b4.append(line.strip())
print(f"Generating {b1} ...")
with open(b1, 'w') as enc_file:
    enc_file.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    b6 = ""
    for index, word in enumerate(b4):
        b6 += f"{word:<9}={b3[index]:05d} "
        b5[b3[index]] = word
        if (index + 1) % a2 = = 0:
            enc_file.write(b6.strip() + "\n")
            b6 = ""
    if b6:
        enc_file.write(b6.strip() + "\n")
    enc_file.write(f"==== END OF {index + 1} b7 = ===\n")
print(f"Generating {b2} ...")
with open(b2, 'w') as dec_file:
    dec_file.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cipher) ====\n")
    b6 = ""
    for index, (number, word) in enumerate(b5.items()):
        b6 += f"{number:04d}={word:<9} "
        if (index + 1) % a2 = = 0:
            dec_file.write(b6.strip() + "\n")
            b6 = ""
    if b6:
        dec_file.write(b6.strip() + "\n")
    dec_file.write(f"==== END OF {index + 1} b7 = ===\n")
print("Done.")
import random
b1 = "encryption-cypher.txt"
b2 = "component-II-decrypt.txt"
a1 = 2048
a2 = 6
b3 = random.sample(range(a1), a1)
b4 = []
b5 = {}
with open("english.txt", "r") as file:
    for line in file:
        b4.append(line.strip())
print(f"Generating {b1} ...")
with open(b1, 'w') as enc_file:
    enc_file.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    b6 = ""
    for index, word in enumerate(b4):
        b6 += f"{word:<9}={b3[index]:05d} "
        b5[b3[index]] = word
        if (index + 1) % a2 = = 0:
            enc_file.write(b6.strip() + "\n")
            b6 = ""
    if b6:
        enc_file.write(b6.strip() + "\n")
    enc_file.write(f"==== END OF {index + 1} b7 = ===\n")
print(f"Generating {b2} ...")
with open(b2, 'w') as dec_file:
    dec_file.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cipher) ====\n")
    b6 = ""
    for index, (number, word) in enumerate(b5.items()):
        b6 += f"{number:04d}={word:<9} "
        if (index + 1) % a2 = = 0:
            dec_file.write(b6.strip() + "\n")
            b6 = ""
    if b6:
        dec_file.write(b6.strip() + "\n")
    dec_file.write(f"==== END OF {index + 1} b7 = ===\n")
print("Done.")