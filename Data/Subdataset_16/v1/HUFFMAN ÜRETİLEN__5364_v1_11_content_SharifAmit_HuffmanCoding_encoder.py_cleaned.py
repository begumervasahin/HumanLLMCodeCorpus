def fonk1(b1):
    b1 = b1.lower()
    b2 = list(set(b1))
    b3 = [0] * len(b2)
    for char in b1:
        b4 = b2.index(char)
        if b3[b4] == 0:
            b3[b4] = b1.count(char)
    return b2, b3
def fonk2(chars, b19):
    b5 = []
    b6 = []
    while b19:
        b7 = max(b19)
        b4 = b19.index(b7)
        b6.append(b7)
        b5.append(chars[b4])
        chars.pop(b4)
        b19.pop(b4)
    return b5, b6
def fonk3(chars, b19):
    b8 = ["null"] * len(chars)
    b9 = list(b19)
    b10 = list(chars)
    while len(b9) > 1:
        b11 = min(b9)
        b12 = b9.index(b11)
        b13 = b10[b12]
        for char in b13:
            b14 = chars.index(char)
            if b8[b14] == "null":
                b8[b14] = "0"
            else:
                b8[b14] = "0" + b8[b14]
        b9.pop(b12)
        b10.pop(b12)
        b15 = min(b9)
        b16 = b9.index(b15)
        b17 = b10[b16]
        for char in b17:
            b14 = chars.index(char)
            if b8[b14] == "null":
                b8[b14] = "1"
            else:
                b8[b14] = "1" + b8[b14]
        b9.pop(b16)
        b10.pop(b16)
        b9.insert(0, b15 + b11)
        b10.insert(0, b17 + b13)
    return b8
def fonk4(b1, chars, b8):
    b18 = ""
    for char in b1:
        b4 = chars.index(char)
        b18 += b8[b4]
    return b18
def fonk5(filename, content):
    with open(filename, "w") as file:
        file.write(content)
def fonk6():
    with open("input.txt", "r") as f:
        b1 = f.readline().strip()
    chars, b19 = fonk1(b1)
    print("The String:", b1)
    print("The char list:", chars)
    print("Frequency Table before sorting:", b19)
    b5, b6 = fonk2(chars, b19)
    print("Frequency Table after sorting:", b6)
    print("Sorted char list:", b5)
    b8 = fonk3(b5, b6)
    print("Huffman Encoder:", b8)
    b18 = fonk4(b1, b5, b8)
    print("Encoded string:", b18)
    fonk5("output.txt", b18)
    b20 = "\n".join(f"{char}={b8[i]}" for i, char in enumerate(b5))
    fonk5("dictionary.txt", b20)
    print("Encoding dictionary saved to dictionary.txt")
if b21 = = "__main__":
    fonk6()