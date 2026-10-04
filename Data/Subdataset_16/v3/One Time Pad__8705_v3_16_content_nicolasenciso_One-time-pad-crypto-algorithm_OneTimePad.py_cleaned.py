b1 = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
b2 = {v: k for k, v in b1.items()}
def fonk1(key, msg):
    if len(key) != len(msg):
        raise ValueError("Key and message must be of the same length.")
    return [
        b2[(b1[key[i]] + b1[msg[i]]) % 26]
        for i in range(len(key))
    ]
def fonk2(key, msg):
    if len(key) != len(msg):
        raise ValueError("Key and message must be of the same length.")
    return [
        (int(key[i]) + int(msg[i])) % 10
        for i in range(len(key))
    ]
if b3 = = "__main__":
    b4 = fonk1("EVXLL", "MONTH")
    print("Encrypted message:", "".join(b4))
    b5 = fonk2("6", "6")
    print("Encrypted numeric message:", b5)
