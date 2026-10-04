
b1 = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
b2 = {v: k for k, v in b1.items()}
def fonk1(key, message):
    b3 = []
    if len(key) == len(message):
        for k_char, m_char in zip(key, message):
            b4 = b1[k_char]
            b5 = b1[m_char]
            b6 = (b4 + b5) % 26
            b3.append(b2[b6])
    return b3
def fonk2(key, message):
    b7 = []
    if len(key) == len(message):
        for k_char, m_char in zip(key, message):
            b8 = (int(k_char) - int(m_char)) % 10
            b7.append(b8)
    return b7
print("Encrypted message:", fonk1("EVXLL", "MONTH"))
print("Encrypted numbers:", fonk2("6", "6"))