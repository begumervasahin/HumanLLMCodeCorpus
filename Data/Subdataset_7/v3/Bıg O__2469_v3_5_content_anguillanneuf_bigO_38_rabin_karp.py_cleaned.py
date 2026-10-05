def fonk1(b7, b8):
    b1 = []
    b2 = len(b7)
    b3 = len(b8)
    a1 = 101
    a2 = 128
    b4 = pow(a2, b3 - 1, a1)
    def fonk2(s):
        a3 = 0
        for char in s:
            a3 = (a3 * a2 + ord(char)) % a1
        return a3
    b5 = fonk2(b8)
    b6 = fonk2(b7[:b3])
    for i in range(b2 - b3 + 1):
        if b5 = = b6:
            if b7[i:i+b3] == b8:
                b1.append(i)
                print("Substring found at index:", i)
        if i < b2 - b3:
            b6 = (a2 * (b6 - b4 * ord(b7[i])) + ord(b7[i + b3])) % a1
            b6 %= a1
    return b1
b7 = 'Get bit; set bit; clear bit; update bit'
b8 = 'bit'
print("Indices of b8 found using Rabin-Karp algorithm:", fonk1(b7, b8))