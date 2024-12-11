def fonk1(b4, b5):
    b1 = []
    b2 = len(b4)
    b3 = len(b5)
    a1 = 101
    a2 = 128
    a3 = 1
    for i in range(b3 - 1):
        a3 = (a3 * a2) % a1
    a4 = 0
    a5 = 0
    for i in range(b3):
        a4 = (a2 * a4 + ord(b5[i])) % a1
        a5 = (a2 * a5 + ord(b4[i])) % a1
    for i in range(b2 - b3 + 1):
        if a4 = = a5:
            if b4[i:i + b3] == b5:
                b1.append(i)
                print("Substring found at index:", i)
        if i < b2 - b3:
            a5 = (a2 * (a5 - a3 * ord(b4[i])) + ord(b4[i + b3])) % a1
            if a5 < 0:
                a5 += a1
    return b1
b4 = 'Get bit; set bit; clear bit; update bit'
b5 = 'bit'
print("Indices of b5 found using Rabin-Karp algorithm:", fonk1(b4, b5))