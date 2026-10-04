import gf
def do(state):
    fixedmatrix = bytearray([0x02, 0x03, 0x01, 0x01])
    columns = [bytearray() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            columns[j].append(state[j + i * 4])
    new_state_matrix = b''.join([mix(columns[i]) for i in range(4)])
    return new_state_matrix
def inverse(m):
    fixedmatrix = bytearray([0x0e, 0x0b, 0x0d, 0x09])
    return b''.join([inv(m[i:i+4]) for i in range(0, 16, 4)])
def mix(column):
    fixedmatrix = bytearray([0x02, 0x03, 0x01, 0x01])
    mixcolumnmatrix = bytearray()
    for i in range(4):
        resulting_list = []
        rijndael = gf.makeblist(0x11b)
        for j in range(4):
            fixedbytelist = gf.makeblist(fixedmatrix[j])
            columnvector = gf.makeblist(column[j])
            resultingbyte = gf.mul(fixedbytelist, columnvector)
            if gf.value(resultingbyte) > 255:
                resultingbyte = gf.div(resultingbyte, rijndael)[1]
            resulting_list.append(resultingbyte)
        finalvalue = gf.add(resulting_list[0], resulting_list[1])
        finalvalue = gf.add(finalvalue, resulting_list[2])
        finalvalue = gf.add(finalvalue, resulting_list[3])
        mixcolumnmatrix.append(gf.value(finalvalue))
        fixedmatrix = gf.circrotateright(fixedmatrix)
    return mixcolumnmatrix
def inv(column):
    fixedmatrix = bytearray([0x0e, 0x0b, 0x0d, 0x09])
    mixcolumnmatrix = bytearray()
    for i in range(4):
        resulting_list = []
        rijndael = gf.makeblist(0x11b)
        for j in range(4):
            fixedbitlist = gf.makeblist(fixedmatrix[j])
            columnvector = gf.makeblist(column[j])
            resultingbyte = gf.mul(fixedbitlist, columnvector)
            while gf.value(resultingbyte) > 255:
                resultingbyte = gf.div(rijndael, resultingbyte)[1]
            resulting_list.append(resultingbyte)
        finalvalue = gf.add(resulting_list[0], resulting_list[1])
        finalvalue = gf.add(finalvalue, resulting_list[2])
        finalvalue = gf.add(finalvalue, resulting_list[3])
        mixcolumnmatrix.append(gf.value(finalvalue))
        fixedmatrix = gf.circrotateright(fixedmatrix)
    return mixcolumnmatrix
def blhex(bitlist):
    print(hex(gf.value(bitlist)))
if __name__ == "__main__":
    example_state = bytearray([0x32, 0x88, 0x31, 0xe0, 0x43, 0x5a, 0x31, 0x37, 0xf6, 0x30, 0x98, 0x07, 0xa8, 0x8d, 0xa2, 0x34])
    print("Original State:")
    print(example_state)
    mixed_state = do(example_state)
    print("Mixed State:")
    print(mixed_state)
    inverted_state = inverse(mixed_state)
    print("Inverted State:")
    print(inverted_state)