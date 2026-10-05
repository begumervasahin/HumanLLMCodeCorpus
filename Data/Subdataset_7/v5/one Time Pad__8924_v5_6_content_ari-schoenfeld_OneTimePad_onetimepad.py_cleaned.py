import sys
def fonk1(b6):
    return [ord(char) for char in b6]
def fonk2(num):
    b1 = []
    while num > 0:
        b1.insert(0, num % 10)
        num
    return b1
def fonk3(b10):
    b2 = []
    for num in b10:
        b2.extend(fonk2(num))
    return b2
def fonk4(plain_array, b8):
    return [(plain + pad) % 10 for plain, pad in zip(plain_array, b8)]
def fonk5(encrypted_array, b8):
    b3 = []
    for i in range(0, len(encrypted_array), 3):
        b4 = sum((encrypted_array[i + j] - b8[i + j] + 10) % 10 * 10**(2-j) for j in range(3))
        b3.append(b4)
    return b3
def fonk6():
    if len(sys.argv) != 4:
        sys.exit("Error: Incorrect number of arguments")
    b9, input_file, b5 = sys.argv[1:]
    try:
        with open(input_file) as message_file:
            b6 = message_file.read()
    except IOError:
        sys.exit("Error: Cannot open message file")
    try:
        with open(b5) as b5:
            b7 = b5.read()
    except IOError:
        sys.exit("Error: Cannot open pad file")
    b8 = [int(char) for char in b7 if char.isdigit()]
    if b9 = = "encrypt":
        b10 = fonk1(b6)
        if len(b8) < len(b10):
            sys.exit("Error: Pad is shorter than numeric version of message")
        b11 = fonk4(b10, b8)
        b12 = f"encrypted_{input_file}"
        b13 = "".join(map(str, b11)) + "\n"
    elif b9 = = "decrypt":
        b11 = [int(char) for char in b6 if char.isdigit()]
        if len(b8) < len(b11):
            sys.exit("Error: Pad is shorter than numeric version of message")
        b3 = fonk5(b11, b8)
        b12 = f"decrypted_{input_file}"
        b13 = "".join(map(chr, b3))
    else:
        sys.exit("Error: Incorrect command, must be 'encrypt' or 'decrypt'")
    with open(b12, "w+") as outfile:
        outfile.write(b13)
if b14 = = "__main__":
    fonk6()