
from GF2 import zero, one
import mat
import random
def str_to_bits(input_string):
    bit_list = [1 << i for i in range(8)]
    return [one if ord(char) & bit else zero for char in input_string for bit in bit_list]
def bits_to_str(input_bits):
    bit_list = [1 << i for i in range(8)]
    return ''.join(chr(sum(bit_val if bit else 0 for bit_val, bit in zip(bit_list, input_bits[i:i+8]))) for i in range(0, len(input_bits), 8))
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