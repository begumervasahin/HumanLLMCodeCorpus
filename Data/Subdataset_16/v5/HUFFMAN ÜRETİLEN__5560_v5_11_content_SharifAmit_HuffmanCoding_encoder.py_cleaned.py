def fonk1(b10):
    b1 = {}
    for char in b10:
        b1[char] = b1.get(char, 0) + 1
    return b1
def fonk2(b1):
    b2 = list(b1.keys())
    b3 = list(b1.values())
    b4 = {char: "" for char in b2}
    while len(b3) > 1:
        b5 = sorted(zip(b3, b2))
        b3, b2 = zip(*b5)
        left, b6 = b3[:2], b2[:2]
        b3 = b3[2:]
        b2 = b2[2:]
        b7 = sum(left)
        b8 = "".join(sorted(b6))
        for b9, char in enumerate(b6):
            b4[char] = ("0" if b9 = = 0 else "1") + b4[char]
        b3 = [b7] + list(b3)
        b2 = [b8] + list(b2)
    return b4
def fonk3(b10, b4):
    return ''.join(b4[char] for char in b10)
def fonk4(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
def fonk5():
    with open("input.txt", "r") as file:
        b10 = file.readline().strip().lower()
    print("Input Text:", b10)
    b1 = fonk1(b10)
    print("Frequency Table:", b1)
    b4 = fonk2(b1)
    print("Huffman Codes:", b4)
    b11 = fonk3(b10, b4)
    print("Encoded Text:", b11)
    fonk4("output.txt", b11)
    b12 = "\n".join(f"{char}={code}" for char, code in b4.items())
    fonk4("dictionary.txt", b12)
    print("Huffman Encoding Complete.")
if b13 = = "__main__":
    fonk5()