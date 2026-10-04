def fonk1(s):
    b1 = {}
    for char in s:
        if char in b1:
            b1[char] += 1
        else:
            b1[char] = 1
    return b1
def fonk2(b1):
    b2 = list(b1.keys())
    b3 = list(b1.values())
    b4 = []
    b5 = {char: "" for char in b2}
    while len(b3) > 1:
        b6 = sorted(zip(b3, b2))
        b3, b2 = zip(*b6)
        b7 = b3[0]
        b8 = b3[1]
        b3 = b3[2:]
        b2 = b2[2:]
        b9 = b7 + b8
        b10 = "".join(sorted(b2[:2]))
        for char in b10:
            if char in b5:
                b5[char] = ("0" if char in b2[0] else "1") + b5[char]
        b3 = [b9] + list(b3)
        b2 = [b10] + list(b2)
    return b5
def fonk3(b12, b5):
    b11 = ''.join(b5[char] for char in b12)
    return b11
def fonk4(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
def fonk5():
    with open("input.txt", "r") as f:
        b12 = f.readline().strip().lower()
    print("The String:", b12)
    b1 = fonk1(b12)
    print("Frequency Table before sorting:", b1)
    b5 = fonk2(b1)
    print("Huffman Codes:", b5)
    b11 = fonk3(b12, b5)
    print("Encoded Text:", b11)
    fonk4("output.txt", b11)
    b13 = "\n".join(f"{char}={code}" for char, code in b5.items())
    fonk4("dictionary.txt", b13)
    print("Huffman Encoding Complete.")
if b14 = = "__main__":
    fonk5()