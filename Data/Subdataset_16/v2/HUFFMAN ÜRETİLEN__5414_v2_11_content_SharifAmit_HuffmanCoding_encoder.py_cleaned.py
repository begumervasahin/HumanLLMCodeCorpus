def fonk1(b1):
    b1 = b1.lower()
    b2 = list(set(b1))
    b3 = [b1.count(char) for char in b2]
    return b2, b3
def fonk2(chars, b16):
    b4 = sorted(zip(b16, chars), reverse=True)
    b17, b5 = zip(*b4)
    return list(b5), list(b17)
def fonk3(chars, b16):
    b6 = [""] * len(chars)
    b7 = list(b16)
    b8 = list(chars)
    while len(b7) > 1:
        b9 = b7.index(min(b7))
        b10 = b7.pop(b9)
        b11 = b8.pop(b9)
        b12 = b7.index(min(b7))
        b13 = b7.pop(b12)
        b14 = b8.pop(b12)
        for char in b11:
            b6[chars.index(char)] = "0" + b6[chars.index(char)]
        for char in b14:
            b6[chars.index(char)] = "1" + b6[chars.index(char)]
        b7.insert(0, b13 + b10)
        b8.insert(0, b14 + b11)
    return b6
def fonk4(b1, chars, b6):
    return ''.join(b6[chars.index(char)] for char in b1)
def fonk5(filename, content):
    with open(filename, "w") as file:
        file.write(content)
def fonk6():
    with open("input.txt", "r") as file:
        b15 = file.readline().strip()
    chars, b16 = fonk1(b15)
    print("Original String:", b15)
    print("Character List:", chars)
    print("Frequency Table (Unsorted):", b16)
    b5, b17 = fonk2(chars, b16)
    print("Frequency Table (Sorted):", b17)
    print("Sorted Character List:", b5)
    b6 = fonk3(b5, b17)
    print("Huffman Encoder:", b6)
    b18 = fonk4(b15, b5, b6)
    print("Encoded String:", b18)
    fonk5("output.txt", b18)
    b19 = "\n".join(f"{char}={b6[i]}" for i, char in enumerate(b5))
    fonk5("dictionary.txt", b19)
    print("Huffman encoding dictionary saved to dictionary.txt")
if b20 = = "__main__":
    fonk6()