import random
b1 = "encryption-cypher.txt"
b2 = "component-II-decrypt.txt"
a1 = 2048
a2 = 6
b3 = random.sample(range(0, a1), a1)
b4 = []
b5 = {}
with open("english.txt", "r") as myfile:
    for line in myfile:
        b4.append(line.strip())
print(f"Generating {b1} ...")
with open(b1, 'w') as f_enc:
    f_enc.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    b6 = ""
    for i, word in enumerate(b4):
        b6 += f"{word:<9}={b3[i]:05d} "
        b5[b3[i]] = word
        if (i + 1) % a2 = = 0:
            f_enc.write(b6.strip() + "\n")
            b6 = ""
    if b6:
        f_enc.write(b6.strip() + "\n")
    f_enc.write(f"==== END OF {i + 1} b7 = ===\n")
print(f"Generating {b2} ...")
with open(b2, 'w') as f_dec:
    f_dec.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
    b6 = ""
    for i, (nr, word) in enumerate(b5.items()):
        b6 += f"{nr:04d}={word:<9} "
        if (i + 1) % a2 = = 0:
            f_dec.write(b6.strip() + "\n")
            b6 = ""
    if b6:
        f_dec.write(b6.strip() + "\n")
    f_dec.write(f"==== END OF {i + 1} b7 = ===\n")
print("Done.")