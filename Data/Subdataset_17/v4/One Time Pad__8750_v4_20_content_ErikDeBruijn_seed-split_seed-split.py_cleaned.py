import random
f_name_enc = "encryption-cypher.txt"
f_name_dec = "component-II-decrypt.txt"
word_count = 2048
cols = 6
nrs = random.sample(range(0, word_count), word_count)
words = []
nr_words = {}
with open("english.txt", "r") as myfile:
    for line in myfile:
        words.append(line.strip())
print(f"Generating {f_name_enc} ...")
with open(f_name_enc, 'w') as f_enc:
    f_enc.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    s = ""
    for i, word in enumerate(words):
        s += f"{word:<9}={nrs[i]:05d} "
        nr_words[nrs[i]] = word
        if (i + 1) % cols == 0:
            f_enc.write(s.strip() + "\n")
            s = ""
    if s:
        f_enc.write(s.strip() + "\n")
    f_enc.write(f"==== END OF {i + 1} CODES ====\n")
print(f"Generating {f_name_dec} ...")
with open(f_name_dec, 'w') as f_dec:
    f_dec.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
    s = ""
    for i, (nr, word) in enumerate(nr_words.items()):
        s += f"{nr:04d}={word:<9} "
        if (i + 1) % cols == 0:
            f_dec.write(s.strip() + "\n")
            s = ""
    if s:
        f_dec.write(s.strip() + "\n")
    f_dec.write(f"==== END OF {i + 1} CODES ====\n")
print("Done.")