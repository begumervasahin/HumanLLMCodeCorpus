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
def fonk2(buf, b6):
    b3 = 0xffffffff
    for k in buf:
        b3 = (b3 >> 8) ^ b6[(b3 & 0xff) ^ k]
    return b3 ^ 0xffffffff
def fonk3():
    b4 = 'FAFAFA'
    b5 = bin(int(b4, 16))[2:]
    print(f"Ulazna poruka je: {b5} (0x{b4})")
    b6 = fonk1()
    b7 = fonk2(codecs.decode(b4, 'hex'), b6)
    b8 = bin(b7)[2:]
    print(f"Rezultat je: {b8} ({hex(b7)})")
    b9 = b5 + b8
    print("Poruka koja se salje je:")
    print(b9)
if b10 = = "__main__":
    fonk3()