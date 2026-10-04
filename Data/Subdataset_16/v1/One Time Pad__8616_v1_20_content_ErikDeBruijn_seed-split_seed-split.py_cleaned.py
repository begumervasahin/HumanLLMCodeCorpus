import random
b1 = "encryption-cypher.txt"
a1 = 2048
a2 = 0
a3 = 6
b2 = ""
b3 = random.sample(range(0, a1), a1)
b4 = []
b5 = {}
with open(b1, 'w') as f:
    print("Generating %b2 ..." % b1)
    f.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
    with open("english.txt", "r") as myfile:
        for line in myfile:
            b4.append(line.strip())
    for word in b4:
        b2 = "%b2 %-9s=%-05d" % (b2, word, b3[a2])
        b5[b3[a2]] = word
        a2 += 1
        if a2 % a3 = = 0:
            f.write(b2 + "\n")
            b2 = ""
    f.write("==== END OF %d b6 = === \n" % a2)
b1 = "component-II-decrypt.txt"
a2 = 0
a3 = 6
b2 = ""
with open(b1, 'w') as f:
    print("Generating %b2 ..." % b1)
    f.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
    for nr, word in b5.items():
        b2 = "%b2 %-04d=%-9s" % (b2, nr, word)
        a2 += 1
        if a2 % a3 = = 0:
            f.write(b2 + "\n")
            b2 = ""
    f.write("==== END OF %d b6 = === \n" % a2)
print("Done.")