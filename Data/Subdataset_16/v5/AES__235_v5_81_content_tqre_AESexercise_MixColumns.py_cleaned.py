import gf
def fonk1(state):
    b1 = [bytearray() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            b1[j].append(state[i * 4 + j])
    b2 = b''.join(fonk3(column) for column in b1)
    return b2
def fonk2(state):
    return b''.join(fonk4(state[i:i+4]) for i in range(0, 16, 4))
def fonk3(column):
    b3 = bytearray([0x02, 0x03, 0x01, 0x01])
    return fonk5(column, b3)
def fonk4(column):
    b3 = bytearray([0x0e, 0x0b, 0x0d, 0x09])
    return fonk5(column, b3)
def fonk5(column, b3):
    b4 = bytearray()
    b5 = gf.makeblist(0x11b)
    for _ in range(4):
        b6 = []
        for j in range(4):
            b7 = gf.makeblist(b3[j])
            b8 = gf.makeblist(column[j])
            b9 = gf.mul(b7, b8)
            if gf.value(b9) > 255:
                b9 = gf.div(b9, b5)[1]
            b6.append(b9)
        b10 = b6[0]
        for value in b6[1:]:
            b10 = gf.add(b10, value)
        b4.append(gf.value(b10))
        b3 = gf.circrotateright(b3)
    return b4
def fonk6(bitlist):
    print(hex(gf.value(bitlist)))
if b11 = = "__main__":
    b12 = bytearray([
        0x32, 0x88, 0x31, 0xe0,
        0x43, 0x5a, 0x31, 0x37,
        0xf6, 0x30, 0x98, 0x07,
        0xa8, 0x8d, 0xa2, 0x34
    ])
    print("Original State:")
    print(b12)
    b13 = fonk1(b12)
    print("Mixed State:")
    print(b13)
    b14 = fonk2(b13)
    print("Inverted State:")
    print(b14)