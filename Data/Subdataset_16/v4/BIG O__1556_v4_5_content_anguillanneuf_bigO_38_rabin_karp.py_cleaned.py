
def fonk1(text, substring):
    b1 = []
    b2 = len(text)
    b3 = len(substring)
    a1 = 101
    a2 = 128
    a3 = 1
    for i in range(b3-1):
        a3 = (a3 * a2) % a1
    a4 = 0
    a5 = 0
    for i in range(b3):
        a4 = (a2 * a4 + ord(substring[i])) % a1
        a5 = (a2 * a5 + ord(text[i])) % a1
    for i in range(b2 - b3 + 1):
        if a4 = = a5:
            for j in range(b3):
                if text[i + j] != substring[j]:
                    break
            else:
                b1.append(i)
                print(f"Substring b1 at index {i}")
        if i < b2 - b3:
            a5 = (a2 * (a5 - ord(text[i]) * a3) + ord(text[i + b3])) % a1
            if a5 < 0:
                a5 += a1
    return b1
print(fonk1('Get bit; set bit; clear bit; update bit', 'bit'))