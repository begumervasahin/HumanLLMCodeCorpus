def fonk1():
    b1 = {}
    b2 = {}
    b1[' '] = 0
    b2[0] = ' '
    for i in range(65, 65 + 26):
        b1[chr(i)] = i - 64
        b2[i - 64] = chr(i)
    b3 = {',': 27, '.': 28, '?': 29}
    for char, code in b3.items():
        b1[char] = code
        b2[code] = char
    for i in range(48, 48 + 10):
        b1[chr(i)] = i - 18
        b2[i - 18] = chr(i)
    for i in range(97, 97 + 26):
        b1[chr(i)] = i - 57
        b2[i - 57] = chr(i)
    b1['!'] = 66
    b2[66] = '!'
    return b1, b2
def fonk2(text, a1):
    b1, b2 = fonk1()
    b4 = ""
    for char in text:
        if char not in b1:
            return -1
        else:
            b5 = b1[char]
            b6 = (b5 + a1) % 67
            b4 += b2[b6]
    return b4
def fonk3(text, a1):
    b1, b2 = fonk1()
    b7 = ""
    for char in text:
        if char not in b1:
            return -1
        else:
            b5 = b1[char]
            b8 = (b5 - a1) % 67
            b7 += b2[b8]
    return b7
if b9 = = '__main__':
    b10 = "Hello, World!"
    a1 = 5
    b11 = fonk2(b10, a1)
    if b11 != -1:
        print(f"Encrypted: {b11}")
    else:
        print("Error: Invalid character in input string for encryption.")
    b12 = fonk3(b11, a1)
    if b12 != -1:
        print(f"Decrypted: {b12}")
    else:
        print("Error: Invalid character in input string for decryption.")