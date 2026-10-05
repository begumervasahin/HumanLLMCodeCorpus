def fonk1(b8, b9):
    b1 = []
    a1 = 101
    a2 = 128
    b2 = len(b8)
    b3 = len(b9)
    b4 = pow(a2, b3 - 1) % a1
    b5 = fonk2(b9, a1, a2)
    b6 = fonk2(b8[:b3], a1, a2)
    for i in range(b2 - b3 + 1):
        if b5 = = b6:
            if b8[i:i + b3] == b9:
                b1.append(i)
                print("Substring found at index:", i)
        if i < b2 - b3:
            b6 = fonk3(b6, b8[i], b8[i + b3], b4, a1, a2)
    return b1
def fonk2(string, a1, a2):
    a3 = 0
    for char in string:
        a3 = (a3 * a2 + ord(char)) % a1
    return a3
def fonk3(old_hash, old_char, new_char, b4, a1, a2):
    b7 = (old_hash - ord(old_char) * b4) % a1
    b7 = (b7 * a2 + ord(new_char)) % a1
    return b7 if b7 >= 0 else b7 + a1
b8 = 'Get bit; set bit; clear bit; update bit'
b9 = 'bit'
print("Indices of b9 found using Rabin-Karp algorithm:", fonk1(b8, b9))