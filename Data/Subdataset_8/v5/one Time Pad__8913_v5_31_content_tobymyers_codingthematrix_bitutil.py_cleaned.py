from GF2 import zero, one
import mat
import random
def str_to_bits(input_string):
    bits = []
    for char in input_string:
        char_bits = [one if ord(char) & (1 << i) else zero for i in range(8)]
        bits.extend(char_bits)
    return bits
def bits_to_str(input_bits):
    chars = []
    for i in range(0, len(input_bits), 8):
        byte = input_bits[i:i+8]
        char = chr(sum(bit.val for bit in byte))
        chars.append(char)
    return ''.join(chars)
def bits_to_mat(bits, num_rows=4, transpose=False):
    num_cols = len(bits)
    f = {(i, j): one for j in range(num_cols) for i in range(num_rows) if bits[num_rows * j + i]}
    A = mat.Mat((set(range(num_rows)), set(range(num_cols))), f)
    if transpose:
        A = mat.transpose(A)
    return A
def mat_to_bits(matrix, transpose=False):
    if transpose:
        return [matrix[i, j] for i in sorted(matrix.D[0]) for j in sorted(matrix.D[1])]
    else:
        return [matrix[i, j] for j in sorted(matrix.D[1]) for i in sorted(matrix.D[0])]
def generate_noise(matrix, freq):
    f = {(i, j): one for i in matrix.D[0] for j in matrix.D[1] if random.random() < freq}
    return mat.Mat(matrix.D, f)