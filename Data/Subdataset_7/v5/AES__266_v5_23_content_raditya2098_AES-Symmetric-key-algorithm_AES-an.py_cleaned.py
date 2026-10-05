
b1 = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
]
b2 = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]
def fonk1(hex_str):
    return hex_str[2:]
def fonk2(message):
    b3 = []
    for char in message:
        b4 = b1[ord(char)]
        b3.append(fonk1(hex(b4)))
    return b3
def fonk3():
    b5 = 'Thats my Kung Fu'
    print(f"Key length: {len(b5.encode('utf-8'))} bytes")
    b6 = 'Two One Nine Two'
    print(f"Message: {b6}")
    print(f"Message length: {len(b6.encode('utf-8'))} bytes")
    b7 = fonk2(b6)
    print("S-box b3 values:", b7)
    b8 = [b7[i:i+4] for i in range(0, len(b7), 4)]
    for i, block in enumerate(b8):
        print(f"Block {i+1}: {block}")
if b9 = = "__main__":
    fonk3()