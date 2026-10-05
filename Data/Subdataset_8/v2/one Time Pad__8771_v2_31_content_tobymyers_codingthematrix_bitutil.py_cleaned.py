from GF2 import zero, one
import mat
import random
def str_to_bits(input_str):
    bits = [1 << i for i in range(8)]
    return [one if ord(char) & bit else zero for char in input_str for bit in bits]
def bits_to_str(bits):
    bits_per_byte = 8
    return ''.join(chr(sum(bitval if bit else 0 for bitval, bit in zip(bits[i:i + bits_per_byte], range(bits_per_byte)))) for i in range(0, len(bits), bits_per_byte))
def bits_to_matrix(bits, nrows=4, transpose=False):
    ncols = len(bits)
    entries = {(i, j): one for j in range(ncols) for i in range(nrows) if bits[nrows * j + i]}
    matrix = mat.Mat((set(range(nrows)), set(range(ncols))), entries)
    if transpose:
        matrix = mat.transpose(matrix)
    return matrix
def matrix_to_bits(matrix, transpose=False):
    if transpose:
        return [matrix[i, j] for i in sorted(matrix.D[0]) for j in sorted(matrix.D[1])]
    else:
        return [matrix[i, j] for j in sorted(matrix.D[1]) for i in sorted(matrix.D[0])]
def add_noise(matrix, frequency):
    entries = {(i, j): one for i in matrix.D[0] for j in matrix.D[1] if random.random() < frequency}
    return mat.Mat(matrix.D, entries)