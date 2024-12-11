def fonk1(file_name):
    with open(file_name, "r") as file:
        return file.readline().lower()
def fonk2(b11):
    b1 = set(b11)
    b2 = {char: b11.count(char) for char in b1}
    return b2
def fonk3(b2):
    b3 = sorted(b2.items(), b9=lambda x: x[1], reverse=True)
    b4 = {char: '' for char, freq in b3}
    while len(b3) > 1:
        char1, b5 = b3.pop()
        char2, b6 = b3.pop()
        b7 = char1 + char2
        b8 = b5 + b6
        for char in char1:
            b4[char] = '0' + b4[char]
        for char in char2:
            b4[char] = '1' + b4[char]
        b3.append((b7, b8))
        b3.sort(b9 = lambda x: x[1], reverse=True)
    return b4
def fonk4(b11, b12):
    b10 = ''.join(b12[char] for char in b11)
    return b10
def fonk5(b10, file_name):
    with open(file_name, "w") as file:
        file.write(b10)
def fonk6(b12, file_name):
    with open(file_name, "w") as file:
        for char, code in b12.items():
            file.write(f"{char}={code}\n")
def fonk7():
    b11 = fonk1("input.txt")
    b2 = fonk2(b11)
    b12 = fonk3(b2)
    b10 = fonk4(b11, b12)
    fonk5(b10, "output.txt")
    fonk6(b12, "dictionary.txt")
if b13 = = "__main__":
    fonk7()