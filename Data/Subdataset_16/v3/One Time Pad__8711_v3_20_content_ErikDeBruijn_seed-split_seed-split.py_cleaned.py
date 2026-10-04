import random
b1 = "encryption-cypher.txt"
b2 = "component-II-decrypt.txt"
a1 = 2048
a2 = 6
def fonk1(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]
def fonk2(count, max_value):
    return random.sample(range(max_value), count)
def fonk3(filename, b6, b7, b4):
    with open(filename, 'w') as file:
        print(f"Generating {filename} ...")
        file.write("==== Encryption sheet to make component 1 of 2 (DESTROY after use) ====\n")
        b3 = ""
        for i, word in enumerate(b6):
            b3 += f"{word:<9}={b7[i]:05d}  "
            if (i + 1) % b4 = = 0:
                file.write(b3 + "\n")
                b3 = ""
        if b3:
            file.write(b3 + "\n")
        file.write(f"==== END OF {len(b6)} b5 = ===\n")
def fonk4(filename, b8, b4):
    with open(filename, 'w') as file:
        print(f"Generating {filename} ...")
        file.write("==== DO NOT DISCARD - STORE SAFELY - component 2 of 2 (decryption cypher) ====\n")
        b3 = ""
        for i, (number, word) in enumerate(b8.items()):
            b3 += f"{number:04d}={word:<9}  "
            if (i + 1) % b4 = = 0:
                file.write(b3 + "\n")
                b3 = ""
        if b3:
            file.write(b3 + "\n")
        file.write(f"==== END OF {len(b8)} b5 = ===\n")
def fonk5():
    b6 = fonk1("english.txt")
    b7 = fonk2(a1, a1)
    b8 = dict(zip(b7, b6))
    fonk3(b1, b6, b7, a2)
    fonk4(b2, b8, a2)
    print("Done.")
if b9 = = "__main__":
    fonk5()