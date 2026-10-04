import random
b1 = "encryption-cypher.txt"
b2 = "component-II-decrypt.txt"
a1 = 2048
a2 = 6
b3 = random.sample(range(0, a1), a1)
b4 = []
b5 = {}
with open("english.txt", "r") as myfile:
    b4 = [line.strip() for line in myfile]
with open(b1, 'w') as f:
    print(f"Generating {b1} ...")
    f.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    b6 = ""
    for i, word in enumerate(b4):
        b6 += f"{word:<9}={b3[i]:05d}  "
        b5[b3[i]] = word
        if (i + 1) % a2 = = 0:
            f.write(b6 + "\n")
            b6 = ""
    if b6:
        f.write(b6 + "\n")
    f.write(f"==== END OF {len(b4)} b7 = === \n")
with open(b2, 'w') as f:
    print(f"Generating {b2} ...")
    f.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
    b6 = ""
    for i, (number, word) in enumerate(b5.items()):
        b6 += f"{number:04d}={word:<9}  "
        if (i + 1) % a2 = = 0:
            f.write(b6 + "\n")
            b6 = ""
    if b6:
        f.write(b6 + "\n")
    f.write(f"==== END OF {len(b5)} b7 = === \n")
print("Done.")