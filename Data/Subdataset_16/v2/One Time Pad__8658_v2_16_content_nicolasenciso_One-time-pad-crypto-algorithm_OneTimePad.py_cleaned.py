
b1 = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
b2 = {v: k for k, v in b1.items()}
def fonk1(key, msg):
    b3 = []
    if len(key) == len(msg):
        for i in range(len(key)):
            b4 = b1[key[i]]
            b5 = b1[msg[i]]
            b6 = (b4 + b5) % 26
            b3.append(b2[b6])
    return b3
def fonk2(key, msg):
    b7 = []
    if len(key) == len(msg):
        for i in range(len(key)):
            b8 = (int(key[i]) + int(msg[i])) % 10
            b7.append(b8)
    return b7
if b9 = = "__main__":
    b10 = fonk1("EVXLL", "MONTH")
    print("Encrypted message:", "".join(b10))
    b11 = fonk2("6", "6")
    print("Encrypted numeric message:", b11)
