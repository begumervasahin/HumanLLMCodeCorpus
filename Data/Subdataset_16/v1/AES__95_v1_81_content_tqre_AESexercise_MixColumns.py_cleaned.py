import gf
def fonk1(state):
    b1 = bytearray([0x02, 0x03, 0x01, 0x01])
    b2 = [bytearray() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            b2[j].append(state[j + i * 4])
    b3 = b''.join([fonk3(b2[i]) for i in range(4)])
    return b3
def fonk2(m):
    b1 = bytearray([0x0e, 0x0b, 0x0d, 0x09])
    return b''.join([fonk4(m[i:i+4]) for i in range(0, 16, 4)])
def fonk3(column):
    b1 = bytearray([0x02, 0x03, 0x01, 0x01])
    b4 = bytearray()
    for i in range(4):
        b5 = []
        b6 = gf.makeblist(0x11b)
        for j in range(4):
            b7 = gf.makeblist(b1[j])
            b8 = gf.makeblist(column[j])
            b9 = gf.mul(b7, b8)
            if gf.value(b9) > 255:
                b9 = gf.div(b9, b6)[1]
            b5.append(b9)
        b10 = gf.add(b5[0], b5[1])
        b10 = gf.add(b10, b5[2])
        b10 = gf.add(b10, b5[3])
        b4.append(gf.value(b10))
        b1 = gf.circrotateright(b1)
    return b4
def fonk4(column):
    b1 = bytearray([0x0e, 0x0b, 0x0d, 0x09])
    b4 = bytearray()
    for i in range(4):
        b5 = []
        b6 = gf.makeblist(0x11b)
        for j in range(4):
            b11 = gf.makeblist(b1[j])
            b8 = gf.makeblist(column[j])
            b9 = gf.mul(b11, b8)
            while gf.value(b9) > 255:
                b9 = gf.div(b6, b9)[1]
            b5.append(b9)
        b10 = gf.add(b5[0], b5[1])
        b10 = gf.add(b10, b5[2])
        b10 = gf.add(b10, b5[3])
        b4.append(gf.value(b10))
        b1 = gf.circrotateright(b1)
    return b4
def fonk5(bitlist):
    print(hex(gf.value(bitlist)))
if b12 = = "__main__":
    b13 = bytearray([0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34])
    print("Original State:")
    print(b13)
    b14 = fonk1(b13)
    print("Mixed State:")
    print(b14)
    b15 = fonk2(b14)
    print("Inverted State:")
    print(b15)