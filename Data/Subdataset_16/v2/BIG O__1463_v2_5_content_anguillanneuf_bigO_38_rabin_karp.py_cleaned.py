
def fonk1(b8, b9):
    b1 = len(b8)
    b2 = len(b9)
    if b2 > b1:
        return []
    a1 = 101
    a2 = 128
    b3 = pow(a2, b2-1) % a1
    b4 = sum(ord(b9[i]) * pow(a2, b2-i-1) for i in range(b2)) % a1
    b5 = sum(ord(b8[i]) * pow(a2, b2-i-1) for i in range(b2)) % a1
    b6 = []
    for i in range(b1 - b2 + 1):
        if b5 = = b4:
            if b8[i:i+b2] == b9:
                b6.append(i)
                print(f"Substring b6 at index {i}")
        if i < b1 - b2:
            b5 = (a2 * (b5 - ord(b8[i]) * b3) + ord(b8[i + b2])) % a1
            if b5 < 0:
                b5 += a1
    return b6
if b7 = = "__main__":
    b8 = 'Get bit; set bit; clear bit; update bit'
    b9 = 'bit'
    print("Occurrences of b9:", fonk1(b8, b9))