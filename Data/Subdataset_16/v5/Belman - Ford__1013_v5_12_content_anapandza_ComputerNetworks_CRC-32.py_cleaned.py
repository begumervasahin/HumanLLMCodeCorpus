import codecs
def fonk1():
    b1 = []
    b2 = 0xEDB88320
    for byte in range(256):
        b3 = byte
        for _ in range(8):
            if b3 & 1:
                b3 = (b3 >> 1) ^ b2
            else:
                b3 >>= 1
        b1.append(b3)
    return b1
def fonk2(data, b1):
    b4 = 0xFFFFFFFF
    for byte in data:
        b4 = (b4 >> 8) ^ b1[(b4 & 0xFF) ^ byte]
    return b4 ^ 0xFFFFFFFF
def fonk3(hex_string):
    return bin(int(hex_string, 16))[2:]
def fonk4():
    b5 = 'FAFAFA'
    b6 = fonk3(b5)
    print(f"Input message: {b6} (0x{b5})")
    b1 = fonk1()
    b7 = codecs.decode(b5, 'hex')
    b8 = fonk2(b7, b1)
    b9 = bin(b8)[2:].zfill(32)
    print(f"Checksum: {b9} ({hex(b8)})")
    b10 = b6 + b9
    print("Message to be sent:")
    print(b10)
if b11 = = "__main__":
    fonk4()