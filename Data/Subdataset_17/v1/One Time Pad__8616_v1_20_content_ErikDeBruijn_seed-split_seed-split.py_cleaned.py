import random
f_name = "encryption-cypher.txt"
word_count = 2048
i = 0
cols = 6
s = ""
nrs = random.sample(range(0, word_count), word_count)
words = []
nr_words = {}
with open(f_name, 'w') as f:
    print("Generating %s ..." % f_name)
    f.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    with open("english.txt", "r") as myfile:
        for line in myfile:
            words.append(line.strip())
    for word in words:
        s = "%s %-9s=%-05d" % (s, word, nrs[i])
        nr_words[nrs[i]] = word
        i += 1
        if i % cols == 0:
            f.write(s + "\n")
            s = ""
    f.write("==== END OF %d CODES ==== \n" % i)
f_name = "component-II-decrypt.txt"
i = 0
cols = 6
s = ""
with open(f_name, 'w') as f:
    print("Generating %s ..." % f_name)
    f.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
    for nr, word in nr_words.items():
        s = "%s %-04d=%-9s" % (s, nr, word)
        i += 1
        if i % cols == 0:
            f.write(s + "\n")
            s = ""
    f.write("==== END OF %d CODES ==== \n" % i)
print("Done.")