def fonk1(filename):
    with open(filename, "r") as file:
        return file.readline().lower()
def fonk2(string):
    return {char: string.count(char) for char in set(string)}
def fonk3(b8):
    return dict(sorted(b8.items(), b1 = lambda item: item[1], reverse=True))
def fonk4(b8):
    b2 = {}
    b3 = list(b8.keys())
    while len(b8) > 1:
        char1, b4 = b8.popitem()
        char2, b5 = b8.popitem()
        b6 = b4 + b5
        b7 = char1 + char2
        for char in char1:
            b2[char] = '0' + b2.get(char, '')
        for char in char2:
            b2[char] = '1' + b2.get(char, '')
        b8[b7] = b6
        b8 = fonk3(b8)
    return b2
def fonk5(string, b2):
    return ''.join(b2[char] for char in string)
def fonk6(filename, b14):
    with open(filename, "w") as file:
        file.write(b14)
def fonk7(filename, b2):
    with open(filename, "w") as file:
        for char, code in b2.items():
            file.write(f"{char}={code}\n")
def fonk8():
    b9 = "input.txt"
    b10 = "output.txt"
    b11 = "dictionary.txt"
    b12 = fonk1(b9)
    print("Original String:", b12)
    b13 = fonk2(b12)
    print("Frequency Table:", b13)
    b2 = fonk4(b13)
    print("Encoder:", b2)
    b14 = fonk5(b12, b2)
    print("Encoded String:", b14)
    fonk6(b10, b14)
    fonk7(b11, b2)
if b15 = = "__main__":
    fonk8()