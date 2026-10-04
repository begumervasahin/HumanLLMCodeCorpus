import numpy as np
def shift_left(bits):
    final_shift = []
    for bit_string in bits:
        matrix = np.array(list(bit_string)).reshape(4, 4)
        shifted_matrix = np.array([np.roll(row, -count) for count, row in enumerate(matrix)])
        final_shift.append(''.join(shifted_matrix.flatten()))
    return final_shift
def shift_right(bits):
    final_shift = []
    for bit_string in bits:
        matrix = np.array(list(bit_string)).reshape(4, 4)
        shifted_matrix = np.array([np.roll(row, count) for count, row in enumerate(matrix)])
        final_shift.append(''.join(shifted_matrix.flatten()))
    return final_shift
def display_bits(title, bits):
    print(f"\n{title}:")
    for bit_string in bits:
        print(bit_string)
def main():
    bits = [
        "00010010001101000101011001111000",
        "11110000101010101111000010101010"
    ]
    left_shifted_bits = shift_left(bits)
    right_shifted_bits = shift_right(bits)
    display_bits("Original bits", bits)
    display_bits("Left shifted bits", left_shifted_bits)
    display_bits("Right shifted bits", right_shifted_bits)
if __name__ == "__main__":
    main()