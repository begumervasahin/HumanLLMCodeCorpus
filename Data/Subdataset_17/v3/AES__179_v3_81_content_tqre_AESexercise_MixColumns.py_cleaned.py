import gf
def do(state):
    columns = [bytearray() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            columns[j].append(state[j + i * 4])
    new_state_matrix = b''.join(mix(column) for column in columns)
    return new_state_matrix
def inverse(state):
    return b''.join(inv(state[i:i+4]) for i in range(0, 16, 4))
def mix(column):
    fixed_matrix = bytearray([0x02, 0x03, 0x01, 0x01])
    return mix_helper(column, fixed_matrix)
def inv(column):
    fixed_matrix = bytearray([0x0e, 0x0b, 0x0d, 0x09])
    return mix_helper(column, fixed_matrix)
def mix_helper(column, fixed_matrix):
    mix_column_matrix = bytearray()
    rijndael = gf.makeblist(0x11b)
    for _ in range(4):
        resulting_list = []
        for j in range(4):
            fixed_byte_list = gf.makeblist(fixed_matrix[j])
            column_vector = gf.makeblist(column[j])
            resulting_byte = gf.mul(fixed_byte_list, column_vector)
            if gf.value(resulting_byte) > 255:
                resulting_byte = gf.div(resulting_byte, rijndael)[1]
            resulting_list.append(resulting_byte)
        final_value = resulting_list[0]
        for value in resulting_list[1:]:
            final_value = gf.add(final_value, value)
        mix_column_matrix.append(gf.value(final_value))
        fixed_matrix = gf.circrotateright(fixed_matrix)
    return mix_column_matrix
def blhex(bitlist):
    print(hex(gf.value(bitlist)))
if __name__ == "__main__":
    example_state = bytearray([
        0x32, 0x88, 0x31, 0xe0,
        0x43, 0x5a, 0x31, 0x37,
        0xf6, 0x30, 0x98, 0x07,
        0xa8, 0x8d, 0xa2, 0x34
    ])
    print("Original State:")
    print(example_state)
    mixed_state = do(example_state)
    print("Mixed State:")
    print(mixed_state)
    inverted_state = inverse(mixed_state)
    print("Inverted State:")
    print(inverted_state)