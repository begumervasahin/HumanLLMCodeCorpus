
b1 = [
]
b2 = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]
def fonk1(hex_str):
    return hex_str[2:]
def fonk2(message):
    b3 = []
    for char in message:
        b4 = fonk1(hex(ord(char)))
        b5 = b1[int(b4, 16)]
        b3.append(fonk1(hex(b5)))
    return b3
def fonk3():
    b6 = 'Thats my Kung Fu'
    print(f"Key length: {len(b6.encode('utf-8'))} bytes")
    b7 = 'Two One Nine Two'
    print(f"Message: {b7}")
    print(f"Message length: {len(b7.encode('utf-8'))} bytes")
    b8 = fonk2(b7)
    print("S-box b3 values:", b8)
    b9 = [b8[i:i+4] for i in range(0, len(b8), 4)]
    for i, block in enumerate(b9):
        print(f"Block {i+1}: {block}")
if b10 = = "__main__":
    fonk3()