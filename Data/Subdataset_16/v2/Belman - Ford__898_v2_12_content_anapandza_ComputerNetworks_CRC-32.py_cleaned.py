import codecs
def fonk1():
    b1 = []
    for i in range(256):
        b2 = i
        for _ in range(8):
            if b2 & 1:
                b2 = (b2 >> 1) ^ 0xEDB88320
            else:
                b2 >>= 1
        b1.append(b2)
    return b1
def fonk2(buffer, b1):
    b3 = 0xFFFFFFFF
    for byte in buffer:
        b3 = (b3 >> 8) ^ b1[(b3 & 0xFF) ^ byte]
    return b3 ^ 0xFFFFFFFF
def fonk3():
    b4 = 'FAFAFA'
    b5 = bin(int(b4, 16))[2:]
    print(f"Input b4: {b5} (0x{b4})")
    b1 = fonk1()
    b6 = codecs.decode(b4, 'hex')
    b7 = fonk2(b6, b1)
    b8 = bin(b7)[2:]
    print(f"Checksum: {b8} ({hex(b7)})")
    b9 = b5 + b8
    print("Message to be sent:")
    print(b9)
if b10 = = "__main__":
    fonk3()